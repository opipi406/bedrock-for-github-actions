import boto3
import datetime

# Amazon Bedrock クライアントのセットアップ
client = boto3.client('bedrock-runtime')

# ファイル読み込み
with open("document.md", "r") as file:
    input_text = file.read()

# Bedrock 解析リクエスト
response = client.invoke_model(
    modelId="claude3.5-sonnet",
    body={"inputText": input_text}
)

# 解析結果の取得
result_text = response['body']['outputText']

# 新しいファイルに出力
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = "result.md"
with open(output_filename, "w") as output_file:
    output_file.write(result_text)

print(f"Analysis completed: {output_filename}")
