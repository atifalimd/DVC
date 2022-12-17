import argparse
import os
import logging
from src.utils.common import read_yaml, create_directories
import urllib.request as req

STAGE = "STAGE_01 get data" ## <<< change stage name 

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path):
    ## read config files
    config = read_yaml(config_path)
    source_data=config["source_data"]

    local_data_dir=config["source_download_dir"]["data_dir"]
    create_directories([local_data_dir])

    data_filename=config["source_download_dir"]["data_file"]
    local_data_file_path = os.path.join(local_data_dir, data_filename)

    logging.info("Download started")
    filename,header= req.urlretrieve(source_data, local_data_file_path)
    logging.info("Download completed")
    logging.info(("Download file is present at:{}").format(filename))
    logging.info(("Download file is present at:{}").format(header))


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e