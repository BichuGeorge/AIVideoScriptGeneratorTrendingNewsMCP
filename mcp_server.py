from fastmcp import FastMCP
from app import fetch_news, generate_video_transcription

mcp = FastMCP("This is for real time news ")

@mcp.tool()
def fetch_news_mcp(query):
    return fetch_news(query=query)


@mcp.tool()
def gen_video_transcript_mcp(query):
    news = fetch_news(query=query)
    return generate_video_transcription(news)


if __name__ == "__main__":
    mcp.run()