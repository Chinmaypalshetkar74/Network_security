import os
import sys
import pandas as pd

import certifi
import pymongo

from dotenv import load_dotenv

from fastapi import (
    FastAPI,
    Request,
    UploadFile,
    File
)

from fastapi.middleware.cors import (
    CORSMiddleware
)

from fastapi.responses import (
    Response
)

from fastapi.templating import (
    Jinja2Templates
)

from starlette.responses import (
    RedirectResponse
)

from uvicorn import run as app_run

from Networksecurity.Exception.exception import (
    NetworkSecurityException
)

from Networksecurity.Pipeline.Training_pipline import (
    TrainPipeline
)

from Networksecurity.Logging.logger import (
    logging
)

from Networksecurity.utils.main_utils.utils import (
    load_object
)

from Networksecurity.utils.ml_utils.model.estimator import (
    NetworkSecurityModel
)

from Networksecurity.Constants.Training_pipeline import (
    Data_Ingestion_Database_Name,
    Data_Ingestion_Collection_Name
)

# ==========================================
# Environment Variables
# ==========================================

load_dotenv()

mongodb_url = os.getenv(
    "MONGO_DB_KEY"
)

# ==========================================
# MongoDB Connection
# ==========================================

client = pymongo.MongoClient(
    mongodb_url,
    tlsCAFile=certifi.where()
)

database = client[
    Data_Ingestion_Database_Name
]

collection = database[
    Data_Ingestion_Collection_Name
]

# ==========================================
# FastAPI App
# ==========================================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(
    directory="./templates"
)

# ==========================================
# Home Route
# ==========================================

@app.get(
    "/",
    tags=["authentication"]
)
async def index():

    return RedirectResponse(
        url="/docs"
    )

# ==========================================
# Training Route
# ==========================================

@app.get("/train")
async def train_route():

    try:

        training_pipeline = (
            TrainPipeline()
        )

        training_pipeline.run_pipeline()

        return Response(
            content="Training Successful"
        )

    except Exception as e:

        raise NetworkSecurityException(
            e,
            sys
        )

# ==========================================
# Prediction Route
# ==========================================

@app.post("/predict")
async def predict_route(
    request: Request,
    file: UploadFile = File(...)
):

    try:

        df = pd.read_csv(
            file.file
        )

        # Load Preprocessor

        preprocessor = load_object(
            "Final_models/preprocessor.pkl"
        )

        # Load Model

        final_model = load_object(
            "Final_models/model.pkl"
        )

        # Create Prediction Model
        

        network_model = (
            NetworkSecurityModel(
                preprocessor=preprocessor,
                model=final_model
            )
        )

        y_pred = (
            network_model.predict(df)
        )

        df[
            "predicted_column"
        ] = y_pred

        os.makedirs(
            "prediction_output",
            exist_ok=True
        )

        df.to_csv(
            "prediction_output/output.csv",
            index=False
        )

        table_html = df.to_html(
            classes="table table-striped"
        )

        return templates.TemplateResponse(
            "table.html",
            {
                "request": request,
                "table": table_html
            }
        )

    except Exception as e:

        raise NetworkSecurityException(
            e,
            sys
        )

# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    app_run(
        app,
        host="0.0.0.0",
        port=8000
    )