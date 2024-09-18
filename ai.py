import json #un module

def load_memory (fileName = "memory.json"):
    with open (fileName , 'r') as file :
        data = json.load(file)
    return (data)

#load_memory()

def save_memory (memory , fileName = "memory.json"):
    with open (fileName , 'w') as file :
        json.dump (memory, file, indent = 4)
    

def add_memory (question, answer): 
    #reprondre les anciennes questions pour les reecrire
    memory =load_memory()
    
    #ajouter une nouvelle question/reponse
    memory[question] = answer

    #tout reecrire
    save_memory (memory)

    print ("the question and answer is added!")

#add_memory("hasband?", "Mahito")

def add_new_input ():
    question = input("what's your question?")
    answer = input ("what's the answer to this question?")

    add_memory (question, answer)

#add_new_input()

#fonction qui prend la question, qui la compare avec le fichier json et qui envoie la reponse si elle existe
#la fonction lance add_new_input si la question n'existe pas 

def compare_question (user_question):
    hasAnswer = False
    data = load_memory()
    for question, answer in data.items():
        if (user_question == question):
            hasAnswer = True
            print (answer)
    if (hasAnswer == False) :
        print ("je ne connais pas encore cette question :( ")
        add_new_input()        

def ask_for_question ():
    user_question = input ("hello! ask me a question!")
    compare_question (user_question)

ask_for_question()
