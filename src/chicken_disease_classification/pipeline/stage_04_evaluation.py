from chicken_disease_classification.config.configuration import ConfigurationManager
from chicken_disease_classification.components.evaluation import Evaluation
from chicken_disease_classification.logger import loggerr

STAGE_NAME = "Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        loggerr.info(f"*******************")
        loggerr.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        loggerr.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        loggerr.exception(e)
        raise e