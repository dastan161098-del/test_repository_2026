import json
import os


def load_settings():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as f:
            data = json.load(f)
    else:
        data = {
            "color": "red",
            "difficulty": "normal",
            "music": True
        }

    # safety fix
    if "music" not in data:
        data["music"] = True

    return data


def save_settings(s):
    with open("settings.json", "w") as f:
        json.dump(s, f)


def load_scores():
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as f:
            return json.load(f)
    return []


def save_score(name, score, dist, coins):
    data = load_scores()

    data.append({
        "name": name,
        "score": score,
        "dist": dist,
        "coins": coins
    })

    data.sort(key=lambda x: x["score"], reverse=True)

    with open("leaderboard.json", "w") as f:
        json.dump(data[:10], f)