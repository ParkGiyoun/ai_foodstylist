# openai import
import openai
openai.api_key = "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"

def get_answer(message_):

  # answer return
  answer = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages=message_,
    temperature = 0.8
    )

  # 대답 리턴
  return answer['choices'][0]['message']['content']
