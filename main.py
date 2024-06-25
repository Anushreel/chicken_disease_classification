from chicken_disease_classification.logger import loggerr
from chicken_disease_classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from chicken_disease_classification.logger import loggerr
from chicken_disease_classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
STAGE_NAME = "Data Ingestion stage"
try:
   loggerr.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   loggerr.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        loggerr.exception(e)
        raise e




STAGE_NAME = "Prepare base model"
try: 
   loggerr.info(f"*******************")
   loggerr.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   loggerr.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        loggerr.exception(e)
        raise e

