from flask import Flask
from flask import jsonify, request

import random

app = Flask(__name__)

IMAGE_PATH = "https://raw.githubusercontent.com/ishubhamsingh2e/project-hazard/main/data/card/"


def cards(red: bool = 0, chance: int = 10) -> dict:
    items = {
        "red": red
    }

    rand1 = random.randint(1, 322)
    rand2 = random.randint(1, 322)

    items["1"] = f"{IMAGE_PATH}{rand1}.jpg"
    items["2"] = f"{IMAGE_PATH}{rand2}.jpg"

    if random.randint(1, chance) == 1 or red == 1:
        rand3 = random.randint(1, 38)
        items["red"] = 1
    else:
        rand3 = random.randint(1, 322)

    items["3"] = f"{IMAGE_PATH}{rand3}.jpg"

    return items


@app.route("/", methods=['GET'])
def hello_world():
    args = request.args
    red = args.get("red", default=0, type=int)
    chance = args.get("chance", default=10, type=int)
    data = cards(red=bool(red), chance=chance)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
