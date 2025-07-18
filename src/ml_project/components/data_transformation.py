from ml_project import logger
from ml_project.entity.config_entity import DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
import os

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # All data transformation techniques such as normalization, encoding, Scalar, PCA, etc. can be implemented here.
    # For now, we will just read data and use it directly as it is already in a good format.

    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)
        
        # Splitting the data into train and test sets
        # 75% of the data will be used for training and 25% for testing
        train, test = train_test_split(data, test_size=0.25, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir ,'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir ,'test.csv'), index=False)

        logger.info(f"Train and test data saved at {self.config.root_dir}")
        logger.info(f"Train data shape: {train.shape}")
        logger.info(f"Test data shape: {test.shape}")   

        
