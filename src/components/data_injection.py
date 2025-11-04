import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logger
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import Datatransformation
from src.components.model_trainer import ModelTrainer

@dataclass
class DataInjectionConfig:
    train_data_path:str = os.path.join("artifacts",'train.csv')
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","data.csv")


class DataInjection:
    def __init__(self):
        self.injection_config = DataInjectionConfig()

    def initiate_data_injection(self):
        logger.info("Enter the data injection or components")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            os.makedirs(os.path.dirname(self.injection_config.train_data_path),exist_ok=True)
            df.to_csv(self.injection_config.raw_data_path,index=False,header=True)

            logger.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.injection_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injection_config.test_data_path,index=False,header=True)

            logger.info("injection of data complete")
            return (
                self.injection_config.train_data_path,
                self.injection_config.test_data_path
            )

    
        except Exception as e:  
            raise CustomException(e,sys)




if __name__=="__main__":
    obj = DataInjection()
    train_path,test_path = obj.initiate_data_injection()
    train_arr,test_arr,preprocessor_ob_file_path = Datatransformation().initiate_data_transformation(train_path,test_path)
    print(ModelTrainer().initiate_model_trainer(train_arr,test_arr))
