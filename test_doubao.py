import os
from arkruntime import Ark

client = Ark(
    base_url='https://ark.cn-beijing.volces.com/api/v3',
    api_key=os.getenv('ARK_API_KEY'),
)

response = client.responses.create(
    model="doubao-seed-2-1-lite-260915",
    input="hello"
)

for item in response.output:
    if item.type == "message":
        for content in item.content:
            if content.type == "output_text":
                print(content.text)