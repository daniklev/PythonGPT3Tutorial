import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('openaiapikey.txt')
#define events every event has a name, date and time
events = [{'name': 'gym', 'date': '01/01/2021', 'time': '12:00', 'done': 'no'}, {'name': 'work', 'date': '02/02/2021', 'time': '13:00', 'done': 'no'}]
#1print(events[0]['name'])


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.3, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['Bot:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text

def addEvent():
    user_input = input('Enter event: ')
    prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', user_input)
    response = gpt3_completion(prompt)
    
    #parse response by delimiter $
    response = response.split('$')

    #define event
    event = {'name': response[0], 'date': response[1], 'time': response[2], 'done': 'no'}
    events.append(event)

if __name__ == '__main__':
    while True:
        user_input = input('1. Add event\n2. View events\n3. Mark event as done\n4. Exit\n')
        if user_input == '1':
            addEvent()
        if user_input == '2':
            for event in events:
                print(event)
        if user_input == '3':
            user_input = input('Enter event name: ')
            for event in events:
                if event['name'] == user_input:
                    event['done'] = 'yes'
        if user_input == '4':
            break
        
