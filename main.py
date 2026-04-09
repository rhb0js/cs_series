from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


posts: list[dict] = [
    {
        "id": 1,
        "author": "Geek Dude",
        "title": "Awesome FastAPI Blog",
        "content": "The fast API Python Framework",
        "date_posted": "April 1, 2026",
    },
    {
        "id": 2,
        "author": "Tech Guy",
        "title": "Threat to DRF!",
        "content": "Serious competitor to the beloved DRF",
        "date_posted": "April 8, 2026",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['title']}</h1>"


@app.get("/api/posts")
def get_posts():
    return posts
