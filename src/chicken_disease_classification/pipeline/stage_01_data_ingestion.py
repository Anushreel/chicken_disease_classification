from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.data_ingestion import DataIngestion
from chicken_disease_classification.logger import loggerr


STAGE_NAME="Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()



if __name__=='__main__':
    try:
        loggerr.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        loggerr.info(f">>>> stage {STAGE_NAME} completed <<<< \n ****** \n")
    except Exception as e:
        loggerr.exception(e)
        raise e

