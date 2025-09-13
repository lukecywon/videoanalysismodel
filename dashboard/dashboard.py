import streamlit as st
import pandas as pd
import requests
from urllib.parse import urlparse, parse_qs
import os
from dotenv import load_dotenv 
load_dotenv()


# Extract video ID
def get_video_id(youtube_url):
    parsed_url = urlparse(youtube_url)
    if parsed_url.hostname == "youtu.be":
        return parsed_url.path[1:]
    if parsed_url.hostname in ("www.youtube.com", "youtube.com"):
        if parsed_url.path == "/watch":
            return parse_qs(parsed_url.query)["v"][0]
    return None

st.set_page_config(page_title="NoogAI Analysis", layout="wide")
st.title("Dashboard Prototype")

# Your API key
if "YOUTUBE_API_KEY" in os.environ:
    API_KEY = os.getenv("YOUTUBE_API_KEY")
else:
    st.warning("YOUTUBE_API_KEY environment variable not set. Please set a valid API key to use this application.")
    st.stop()

with st.form("video_form"):
    link = st.text_input("Enter YouTube Video Link:")
    submitted = st.form_submit_button("Analyze")

original_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

if get_video_id(link) is None and submitted:
    st.error("Invalid YouTube Video URL. Please try again.")
    st.stop()
elif get_video_id(link) is None and not submitted:
    video_id = get_video_id(original_link)
else:
    video_id = get_video_id(link)

st.subheader("Video Details")

# Get video details
video_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={API_KEY}"
video_response = requests.get(video_url).json()

video_details = pd.DataFrame(columns=["Title", "Description", "Views", "Likes", "Comments"])
video_details["Title"] = [video_response["items"][0]["snippet"]["title"]]
video_details["Description"] = [video_response["items"][0]["snippet"]["description"]]
video_details["Views"] = [video_response["items"][0]["statistics"].get("viewCount", 0)]
video_details["Likes"] = [video_response["items"][0]["statistics"].get("likeCount", 0)]
video_details["Comments"] = [video_response["items"][0]["statistics"].get("commentCount", 0)]

# Get comments (first 20)
comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={API_KEY}&maxResults=20"
comments_response = requests.get(comments_url).json()

comments = pd.DataFrame(columns=["textOriginal", "likeCount"])
for item in comments_response.get("items", []):
    comment = item["snippet"]["topLevelComment"]["snippet"]
    comments = pd.concat([comments, pd.DataFrame([{
        "textOriginal": comment["textOriginal"],
        "likeCount": comment["likeCount"]
    }])], ignore_index=True)


st.write(video_details)
st.write(comments)


