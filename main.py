import re # regular expression
import random as rd

response_data = {
    "hello" : ["Hello, how can I help you."],
    "hi" : ["Hi, how can I help you."],
    r"how are you\??" : ["I am fine, thank you.","I doing good, thank you."],
    "i feel (.*)": ["Why do you feel {0}?","Do you often feel {0}?","What makes you feel {0}?"],
    "i want (.*)": ["Why do you want {0}?","What would it mean to have {0}?","Do you think getting {0} will help?"],
    "my (mother|father|family) (.*)": ["Tell me more about your family.","How does your family make you feel?","Do you often think about your family?"],
    "i can't (.*)": ["What makes you think you can't {0}?","Have you tried to {0}?","Why do you believe you can't {0}?"],
    "i am (.*)": ["How long have you been {0}?","Why do you think you are {0}?","Does being {0} bother you?"],
    "why (.*)": ["What do you think the reason is?","Why do you think that?","Does that question worry you?"],
    "because (.*)": ["Is that the only reason?","What other reasons might there be?","Does saying 'because' help you explain?"],
    "you (.*)": ["What makes you think I {0}?","Why do you believe I {0}?","Does it matter if I {0}?"],
    "i'm worried (.*)": ["What worries you about that?","Why does that make you worried?","Have you felt worried for long?"],
    "i need (.*)": ["Why do you need {0}?","Do you really need {0}?","What would happen if you didn't get {0}?"],
    "(.*) sorry (.*)":["There is no need to apologize.","what are you apologizing for?"],
    "i (.*) myself": ["Why do you {0} yourself?", "what makes you think you {0} yourself?"],
    "(.*) friend (.*)": ["Tell me more about your friends.","Why don't you tell me more about your friends?"],
    "yes" : ["You seem to be quite positive.","You seem to be quite sure.","Okay, but can you elaborate."],
    "no" : ["You seem to be quite negative.","Why not?","Okay, but can you elaborate."]
}


def match_response(input_text):
    for patterns, response_list in response_data.items():
        matches = re.search(patterns, input_text, re.IGNORECASE)
        if matches:
          chosen_response = rd.choice(response_list)
          return chosen_response.format(*matches.groups())

    return "Sorry, I did not understand what you're saying."


def __main__():
    print("Tom the reflex model based chatbot")
    while True:
        user_input = input("You: ")
        if user_input.strip().casefold() == "bye":
            print("Tom: Good bye, Have a great day!")
            break
        print("Tom:", match_response(user_input))


if __name__ == "__main__":
    __main__()

    