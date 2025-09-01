import pandas as pd

comments = [
    "https://storage.googleapis.com/dataset_hosting/comments1.csv",
    "https://storage.googleapis.com/dataset_hosting/comments2.csv",
    "https://storage.googleapis.com/dataset_hosting/comments3.csv",
    "https://storage.googleapis.com/dataset_hosting/comments4.csv",
    "https://storage.googleapis.com/dataset_hosting/comments5.csv",
]

videos = "https://storage.googleapis.com/dataset_hosting/videos.csv"

class Dataset:
    @staticmethod
    def getAllComments():
        list_of_dfs = []
        for csv_file in comments:
            df = pd.read_csv(csv_file)
            list_of_dfs.append(df)

        return pd.concat(list_of_dfs, ignore_index=True)

    @staticmethod
    def getComments(dataset_id = 1):
        if dataset_id not in range(1, len(comments)):
            raise ValueError("dataset_id must be between 1 and 5")

        return pd.read_csv(comments[dataset_id - 1])

    @staticmethod
    def getVideos():
        return pd.read_csv(videos)






