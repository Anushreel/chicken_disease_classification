from chicken_disease_classification.config.configuration import *
from chicken_disease_classification.components.training import Training
from chicken_disease_classification.components.prepare_callbacks import PrepareCallbacks
from chicken_disease_classification.logger import loggerr

STAGE_NAME="Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        prepare_callbacks_config=config.get_prepare_callback_config()
        prepare_callbacks=PrepareCallbacks(prepare_callbacks_config)
        callback_list=prepare_callbacks.get_tb_ckpt_callbacks()

        training_config=config.get_training_config()
        training=Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )

if __name__ == '__main__':
    try:
        loggerr.info(f"*******************")
        loggerr.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        loggerr.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        loggerr.exception(e)
        raise e
    

# tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/ # to run tensorboard log file on browser