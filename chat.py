from openai import OpenAI

client = OpenAI(api_key="sk-4f887bb879814b9ba9c972f635bc568e", base_url="https://api.deepseek.com")


def rewrite(messages):
    history_questions = []
    for i in range(len(messages)):
        history_questions.append("第%d轮: %s" % (i, messages[i][0]))
    history_questions = "\n".join(history_questions)
    user_prompt = f"你的任务是将如下多轮问题合并成一句话，要求保留原始对话的意图，并且去除不相关或重复的部分，使合成的新问题更加清晰、简洁和具有连贯性。\n\n多轮问题:\n{history_questions}\n\n合并后的问题:\n"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "system",
                   "content": "你是一个AI助手，叫做小秘，可以根据用户的问题给出准确的回答。"},
                  {"role": "user", "content": user_prompt}],
        stream=False
    )

    ans = response.choices[0].message.content
    return ans


def translate(prompt):
    prompt = f"你的任务是从问题中提取关键信息，最后将关键信息文字转换成英文。无需返回中间过程语句，仅返回最终转换后的英文关键信息即可。\n\n问题:\n{prompt}\n\n英文关键信息:\n"
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "system",
                   "content": "你是一个AI助手，叫做小秘，可以根据用户的问题给出准确的回答。"},
                  {"role": "user", "content": prompt}],
        stream=False
    )

    ans = response.choices[0].message.content
    return ans
