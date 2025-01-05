import sys

import boto3
import json
import datetime
from pprint import pprint

# Amazon Bedrock クライアントのセットアップ
client = boto3.client("bedrock-runtime")

# ファイル読み込み
with open("document.md", "r") as file:
    document_text = file.read()

prompt = f"""
以下のドキュメントを解析してください。

<document>
{document_text}
</document>
"""

body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
    }
)

# Bedrock 解析リクエスト
response = client.invoke_model(modelId="anthropic.claude-3-5-sonnet-20240620-v1:0", body=body)

# 解析結果の取得
response_body = json.loads(response.get('body').read())

print("=== response")
pprint(response_body)

output_text = response_body["content"][0]["text"]

with open("result.md", "w") as output_file:
    output_file.write(output_text)

print(f"Analysis completed")
