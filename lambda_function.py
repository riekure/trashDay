from datetime import datetime, timedelta, timezone
import json

def lambda_handler(event, context):
    JST = timezone(timedelta(hours=+9), 'JST')
    d = datetime.now(JST)
    trash = [
        "今日対象のゴミはありません。",
        "今日は可燃ゴミの日です。",
        "今日は不燃ゴミの日です。",
        "今日は資源ゴミの日です。",
        "今日は可燃ゴミの日です。",
        "今日対象のゴミはありません。",
        "今日対象のゴミはありません。"
        ]
    text = trash[d.weekday()]
    return {
        'statusCode': 200,
        'body': text
    }
