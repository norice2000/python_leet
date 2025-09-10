import logging
from loguru import logger
import boto3
import json


def setup_builtin_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='log_test1.log',
        filemode='w'
    )
    logger_builtin = logging.getLogger()
    logger_builtin.info("This is an info message using builtin logging")

def setup_loguru_save_locally():
    logger.add("loguru_pipeline.log", rotation="500 MB")
    logger.info("This is an info using loguru")
    logger.debug("This is a debug by loguru")


# writing log to AWS S3

def log_to_s3():
    s3_client = boto3.client('s3')
    bucket_name = "testinglog" #change me
    log_file_name = "logs/testing_log.json"
    log_data = json.dump({
        "level": "INFO",
        "message": "Logging to S3"
    })

    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=log_file_name,
            Body=log_data,
        )
        logger.info("Succesfully logged to AWS S3")
    except Exception as e:
        logger.error(f"Failed to log to AWS S3: {e}")


if __name__ == "__main__":
    # setup_builtin_logging()
    setup_loguru_save_locally()
    # log_to_s3()

# setup_builtin_logging output
# 2025-09-10 21:40:17,609 - INFO - This is an infor message using builtin logging
# 2025-09-10 21:40:17,632 - INFO - Found credentials in shared credentials file: ~/.aws/credentials

# setup_loguru_save_locally output
# 2025-09-10 21:40:17.614 | INFO     | __main__:setup_loguru_save_locally:19 - This is an info using loguru
# 2025-09-10 21:40:17.615 | DEBUG    | __main__:setup_loguru_save_locally:20 - This is a debug by loguru
