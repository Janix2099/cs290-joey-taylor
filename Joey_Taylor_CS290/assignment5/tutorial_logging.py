# type python -m uvicorn tutorial_logging:app --reload to host!
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import logging
from io import StringIO

app = FastAPI()

# Set up logging
log_stream = StringIO()
logging.basicConfig(level=logging.DEBUG, stream=log_stream, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# A custom logger for the application
app_logger = logging.getLogger("app_logger")

# Function to escape HTML to ensure no code weirdness when inserting logs
def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#039;")

# Tutorial content
logging_tutorial = [
    {
        "title": "Introduction to Python Logging",
        "content": "The Python logging module offers a standard way for applications to log messages. It is flexible and easy to use, allowing for both simple logging and complex logging configurations.",
        "example": "",
        "log_example": lambda: None
    },
    {
        "title": "Creating a Basic Logger",
        "content": "You can create a basic logger using logging.getLogger(name), and then set its level with logger.setLevel(logging.DEBUG).",
        "example": "logger = logging.getLogger('example_logger')\nlogger.setLevel(logging.DEBUG)",
        "log_example": lambda: app_logger.debug("This is a debug message created by the basic logger.")
    },
    {
        "title": "Adding Handlers",
        "content": "Handlers send the log records (created by loggers) to the appropriate destination.",
        "example": "handler = logging.StreamHandler()\nformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')\nhandler.setFormatter(formatter)\nlogger.addHandler(handler)",
        "log_example": lambda: app_logger.info("Logging with a handler that formats messages.")
    },
    {
        "title": "Logging Messages",
        "content": "You can log messages with different severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) using the logger.",
        "example": "logger.debug('This is a debug message')\nlogger.info('This is an info message')\nlogger.warning('This is a warning message')\nlogger.error('This is an error message')\nlogger.critical('This is a critical message')",
        "log_example": lambda: [app_logger.warning("A warning message"), app_logger.error("An error message")]
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    index = int(request.query_params.get("index", 0))
    current_tutorial = logging_tutorial[index % len(logging_tutorial)]

    # Execute the logging example
    log_stream.truncate(0)  # Clear previous logs
    log_stream.seek(0)
    current_tutorial["log_example"]()

    log_output = escape_html(log_stream.getvalue())

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Python Logging Tutorial</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                pre {{
                    background-color: #f5f5f5;
                    padding: 15px;
                }}
                .log-output {{
                    background-color: #eee;
                    border-left: 3px solid #f90;
                    padding: 10px;
                    margin-top: 20px;
                    white-space: pre-wrap;
                }}
                button {{
                    display: block;
                    margin: 20px auto;
                    padding: 10px 20px;
                    font-size: 16px;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <h1>{current_tutorial['title']}</h1>
            <p>{current_tutorial['content']}</p>
            <pre>{escape_html(current_tutorial['example'])}</pre>
            <div class="log-output">{log_output}</div>
            <button onclick="location.href='/?index={index + 1}'">Next Lesson</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
