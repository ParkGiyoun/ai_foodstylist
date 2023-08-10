from prompt import openai_def
# system prompt
file = open("python/prompt/system.txt", "r", encoding="utf-8")
system_prompt = file.read()
file.close()

# assistant prompt
file = open("python/prompt/assistant.txt", "r", encoding="utf-8")
assistant_prompt = file.read()
file.close()

# 프롬프트 list생성 & 프롬프트 입력
role_li = ["system", "assistant"]
content_li = [system_prompt, assistant_prompt]

def DoChat (chat):
    #질문 내용 저장
    role_li.append("user")
    content_li.append(chat)

    # GPT에게 넘겨줄 메시지들 정리
    message_ = [{"role": role_li[i], "content": content_li[i]} for i in range(len(role_li))]

    # GPT대답 받아서 list에 집어 넣기
    role_li.append("assistant")
    answer = openai_def.get_answer(message_)
    content_li.append(answer)

    return answer

def SaveChat():
    # 채팅 내용 리스트를 리턴시켜서 model에 저장할 수 있게 할 생각임....
    pass
