import pandas as pd

class Dataset:
    @staticmethod
    def getAllComments():
        comments5 = "https://storage.googleapis.com/dataset_hosting/comments5.csv"
        comments4 = "https://storage.googleapis.com/dataset_hosting/comments4.csv"
        comments3 = "https://storage.googleapis.com/dataset_hosting/comments3.csv"
        comments2 = "https://storage.googleapis.com/dataset_hosting/comments2.csv"
        comments1 = "https://storage.googleapis.com/dataset_hosting/comments1.csv"
        commentLinks = [comments1, comments2, comments3, comments4, comments5]

        list_of_dfs = []
        for csv_file in commentLinks:
            df = pd.read_csv(csv_file)
            list_of_dfs.append(df)

        return pd.concat(list_of_dfs, ignore_index=True)

    @staticmethod
    def getVideos():
        videos = "https://storage.googleapis.com/dataset_hosting/videos.csv"
        return pd.read_csv(videos)
