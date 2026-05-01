import os
from openai import OpenAI

class BaseAgent:
    def __init__(self, role_name):
        self.role_name = role_name
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        
        # 判断是否配置了真实的 API KEY
        self.is_mock = not self.api_key or self.api_key == "your_api_key_here"
        
        if not self.is_mock:
            self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def call_llm(self, system_prompt, user_prompt, mock_response="Mocked Response"):
        if self.is_mock:
            return mock_response
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo", # 也可以改为 gpt-4 或国内大模型
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"[API 调用失败] 请检查 API_KEY 或网络。错误信息: {e}"
