from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request, "home.html", {"posts": posts, "title": "Home"}
    )


@app.get("/api/posts")
def get_posts():
    return posts
