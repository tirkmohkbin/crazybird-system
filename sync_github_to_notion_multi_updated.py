from notion_client import Client
import os
from dotenv import load_dotenv
import requests

load_dotenv()

notion = Client(auth=os.getenv("NOTION_TOKEN"))
database_id = os.getenv("NOTION_DATABASE_ID")
github_token = os.getenv("GH_TOKEN")
repo = os.getenv("REPO_NAME")
file_paths = os.getenv("SYNC_FILE_PATHS").split(",")

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3.raw"
}

def get_file_content(path):
    url = f"https://api.github.com/repos/{repo}/contents/{path.strip()}"
    res = requests.get(url, headers=headers)
    return res.text if res.status_code == 200 else f"Error: {res.status_code}"

for path in file_paths:
    content = get_file_content(path)
    title = os.path.basename(path)

    notion.pages.create(
        parent={"database_id": database_id},
        properties={"Name": {"title": [{"type": "text", "text": {"content": title}}]}},
        children=[{
            "object": "block",
            "type": "paragraph",
            "paragraph": {"rich_text": [{"type": "text", "text": {"content": content[:2000]}}]}
        }]
    )
