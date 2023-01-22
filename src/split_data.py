import os
import yaml
import pandas as pd
import argparse
from pkgutil import get_data
from get_data import get_data, read_params
from sklearn.model_selection import train_test_split

def split_and_saved_data(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    raw_data_path=config["load_data"]["raw_data_csv"]
    split_ratio=config["split_data"]["test_size"]
    random_state=config["base"]["random_state"]

    df=pd.read_csv(raw_data_path, sep=",")
    #print(df.head())
    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    train.to_csv(train_data_path, sep=",", index= False, encoding="utf-8")
    test.to_csv(test_data_path, sep=",", index= False, encoding="utf-8")


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)
