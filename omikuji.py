import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/omikuji")
def mikuji():
    return render_template("omikuji.html")


if __name__ == "__main__":
    omikuji = ["大吉", "凶"]

    # omikuj　というリストからランダムに一つの値を取る

    # result = random.choice(omikuji)

    # print(result[0])
    # print(result[1])

    index = random.randint(0, 1)
    result = omikuji[index]
    print(result)
