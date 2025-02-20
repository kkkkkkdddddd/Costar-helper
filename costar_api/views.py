from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI
import os

class GenerateCostarView(APIView):
    def post(self, request):
        user_input = request.data.get('user_input', '')

        if not user_input:
            return Response({"error": "输入不能为空"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # 初始化 OpenAI 客户端
            client = OpenAI(
                api_key="sk-5024c换为自己的a9b3cfcd78bb2",  
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
            )

            # 构建提示词
            final_prompt = f"""
### Context
定义：提供详细的背景信息和具体情境，帮助模型理解任务的具体需求。
作用：确保生成的内容符合预期场景，避免偏离主题。
示例：如果需要生成关于环保的文章，可以提供背景信息，如“这篇文章将用于学校的环保宣传活动”。

### Objective
定义：明确生成内容的具体目标和预期结果。
作用：帮助模型聚焦于特定任务，避免生成无关内容。
示例：目标可以是“创建一个吸引人的产品描述，突出手机的创新特性，以吸引技术爱好者”。

### Style
定义：设定生成内容的写作风格，包括语言风格和格式。
作用：确保输出内容符合特定的风格要求。
示例：风格可以是“技术性且充满激情的，类似于史蒂夫·乔布斯的产品发布会演讲”。

### Tone
定义：指定生成内容的情感基调，如友好、严肃、幽默等。
作用：调整回答的情感色彩，使其符合预期的交流效果。
示例：语气可以是“兴奋和启发性的，传达出对最新技术进步的热情”。

### Audience
定义：明确生成内容的目标读者或观众。
作用：帮助模型调整内容的复杂度和适用性，使其更适合特定受众。
示例：受众可以是“专业技术人员”或“普通读者”。

### Response
定义：规定输出的格式和结构，如长度、格式等。
作用：确保生成的内容符合特定的格式要求，便于后续使用。
示例：格式可以是“列表、JSON格式的数据、专业报告”。

### 修改后的提示词
请将以下内容改写为COSTAR格式：
{user_input}
生成的内容中仅包含修改后的提示词，不要有其他内容。
"""

            # 调用 API
            completion = client.chat.completions.create(
                model="qwen-plus",  # 模型名称由于deepseek繁忙使用其他模型代替
                messages=[
                    {'role': 'system', 'content': '你是一个专业的提示词优化助手。'},
                    {'role': 'user', 'content': final_prompt}
                ]
            )

            # 提取结果
            result = completion.choices[0].message.content
            return Response({"result": result}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"请求失败：{str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
# Create your views here.
