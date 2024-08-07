from openai import OpenAI

client = OpenAI(api_key="sk-4f887bb879814b9ba9c972f635bc568e", base_url="https://api.deepseek.com")


def chat(messages):
    instruction = "你的任务是将历史问题和当前问题合并成一句话，使当前问题意图更清晰、明确，然后从合并后的问题中提取关键信息，最后将关键信息文字转换成英文。无需返回中间过程语句，仅返回最终转换后的英文关键信息即可。\n"
    history_questions = []
    for message in messages[:-1]:
        history_questions.append(message[0])
    history_questions = "\n".join(history_questions)
    user_prompt = f"历史问题:\n{history_questions}\n\n当前问题:\n{messages[-1][0]}\n\n{instruction}"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "system", "content": "你是一个AI小助手，叫做小咪，由汪洋开发和创建的。"},
                  {"role": "user", "content": user_prompt}],
        stream=False
    )

    ans = response.choices[0].message.content
    return ans
