# type python -m uvicorn star_wars_app:app --reload to host!

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

sources_with_images = [
    {"source": "Revenge of the Sith Adult Novelization", "image": "https://media.discordapp.net/attachments/727263150055096453/1218459121402249266/IMG_2051.jpg?ex=6607bd7c&is=65f5487c&hm=f2d30920fcb7eb58f73ed83d1f042af5bd82d90193cee10ff6cf352e8aca975c&=&format=webp&width=890&height=663"},
    {"source": "Tales of the Bounty Hunters", "image": "https://media.discordapp.net/attachments/1164661323431432302/1218680685829820487/EQYToGDXkAErRBB.jpg?ex=66088bd5&is=65f616d5&hm=eee0e93a6abfc9313186ecf15f85d058f01e2b4303f3423b8d7906a5fa72c716&=&format=webp"},
    {"source": "Jedi Apprentice: The Rising Force", "image": "https://media.discordapp.net/attachments/1164661323431432302/1218682256810573954/image.png?ex=66088d4c&is=65f6184c&hm=057a9e9b706a9c12eefe5a129fd4ff2d973348940d6b14ae65dca11ff9a39941&=&format=webp&quality=lossless"},
    {"source": "Republic - The Rainmakers", "image": "https://media.discordapp.net/attachments/1164661323431432302/1218693138709876746/RCO003_1467446308.jpg?ex=6608976e&is=65f6226e&hm=5a7dc9cb8b49894c7a104526c7a4a97bd087e76fe2aebb2db8af93e3ed7d6185&=&format=webp&width=849&height=663"},
    {"source": "Republic - The Devaronian Version", "image": "https://media.discordapp.net/attachments/1164661323431432302/1218695199426085005/2021-03-20_2.png?ex=66089959&is=65f62459&hm=3e381281841037c5050bf6782fe9e9fdb963e3ec104a5c8eb52db712f14778e8&=&format=webp&quality=lossless&width=795&height=663"}
]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    index = int(request.query_params.get("index", 0))
    current_quote = sources_with_images[index % len(sources_with_images)]

    html_content = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Galactic Sources</title>
            <link href="https://fonts.cdnfonts.com/css/star-wars" rel="stylesheet">
            <style>
                body {{
                    background-color: black;
                    color: yellow;
                    font-family: 'Star Wars', sans-serif;
                    text-align: center;
                }}
                img {{
                    margin-top: 20px;
                    max-width: 100%;
                    height: auto;
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
            <h1>STAR WARS Book Quotes</h1>
            <p>{current_quote['source']}</p>
            <img src="{current_quote['image']}" alt="Star Wars Image">
            <!-- Update the button to cycle through quotes -->
            <button onclick="location.href='/?index={index + 1}'">Next Quote</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
