# AIVideoScriptGeneratorTrendingNewsMCP

# 📰 AI Video Transcript Generator for Trending News

This project is an **AI-powered video transcript generator** designed to fetch **real-time trending news** and generate **engaging short-form video scripts** for platforms like YouTube Shorts or Instagram Reels.

## 🚀 Features

- 🔍 **Real-time News Fetching**  
  Retrieves the latest updates based on a user-defined query using **Gemini-2.0-Flash-001** from EURI AI.

- ✍️ **Video Transcript Generation**  
  Converts the news content into a short, natural-sounding, script-style format using **GPT-4.1-Mini**.

- 🛠️ **Modular MCP Tools**  
  Exposed as **FastMCP** tools, which can be easily accessed and orchestrated through the **Inspector UI**.

## 🧩 Components

- **`fetch_news_mcp`** – Fetches the latest news based on a query.
- **`gen_video_transcript_mcp`** – Generates a video script from the news content.

## 🖥️ Usage

You can interact with this project using the **Inspector UI** via the MCP tool interface.

1. Run the main script:
   ```bash
   python main.py

2. Access the tools:

fetch_news_mcp: Provide a topic to get the latest news.

gen_video_transcript_mcp: Input a topic and get a ready-to-use video script.

## pip install -r requirements.txt

## Sample Latest News Based On User Query
![IPL_news](https://github.com/user-attachments/assets/8354505c-9e3d-4ea2-84d7-0a47adb4e80f)


## Sample Video Transcript Based On News 
![Video_Transcript_IPL_News](https://github.com/user-attachments/assets/c77f2b7a-8fb2-407a-80f8-2ac9d76b97ce)


## We can use flikki.ai to Create a Video From The Generated Transcripts
![fikki](https://github.com/user-attachments/assets/4f30f39c-e234-4975-a389-400bfe1278bf)

