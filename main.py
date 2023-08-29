import uvicorn
from app import app
from config import site_ip, site_port


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=site_ip,
        port=site_port,
    )