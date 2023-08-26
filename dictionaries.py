import string
def word_frequency(sentence):
    new_sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    words = new_sentence.split()
    dict = {}
    for word in words:
        dict[word] = dict[word] + 1 if word in dict else 1    
    
    print(dict)
    return dict    

word_frequency("This is a test sentence. This sentence is a test.")