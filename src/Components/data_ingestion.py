import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.Components.data_transformation import DataTransformation,DataTransformationConfig
from src.Components.model_trainer import ModelTrainer
from src.Components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")#Constructors using dataclass of train, test and raw data paths
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()#train test and raw data paths created(Constructor)

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion")
        try:
            df = pd.read_csv('notebook\data\stud.csv')#data read from csv(can be done via api, mongodb etc)
            logging.info("Read dataset using pandas")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            df.to_csv(self.ingestion_config.raw_data_path,index = False, header = True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size = 0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index = False, header = True)#Made train_data path equal to the train set from train test split
            test_set.to_csv(self.ingestion_config.test_data_path,index = False, header = True)

            logging.info("Ingestion of Data Comopleted")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
            
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,_ = data_transformation.initiate_data_transformation(train_data,test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))