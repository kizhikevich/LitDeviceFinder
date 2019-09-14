import io
file = io.open("Chapter.txt", encoding="utf8") 
paragraphs=file.read()
print('Welcome to the Literary Device finder. The code can tell you how many instances of like or as appear \
in your textfile (as long as it\'s in the same directory) and ask you to confirm which sentences actually \
contain similies. The code can tell you if there is repitition of any other words, and if you have an anaphora \
(repetition of a series of phrases at the beginning of consecutive sentences).')

print('')

newParagraph=paragraphs.replace('?','.')
newParagraph=newParagraph.replace('!','.')
newParagraph=newParagraph.replace('\n',' ')

sentenceBank=newParagraph.split('. ')
sentenceBank
print('')

def simile(sentenceBank):
    #edgecase: will not count if there is a period attached. Does not matter bc in no simile will "as" or "like" occur at the end of a sentence."
    simileBank=[]
    alreadyRepeated=[]
    for sentence in sentenceBank:
        wordsInSentence=sentence.lower().split(' ')
        for words in wordsInSentence:
            if words=='like' or words=='as': 
                if words not in alreadyRepeated:
                    alreadyRepeated.append(words)
                    print('Is the following a simile?', sentence)
                    if input().lower().startswith('y'):
                        simileBank.append(sentence)
        alreadyRepeated=[]       

    print('So here are your similes:', simileBank)


def repetition(sentenceBank):
    dictionary={}
    repeatedWords=[]
    for sentence in sentenceBank:
        words=sentence.lower().split(' ')
        for word in words:
                 if word!= 'as' and word!='like':
                     if word in dictionary:
                        dictionary[word]+=1
                     else:
                         dictionary[word]=1
          
                     if dictionary[word]>=2:
                         if word not in repeatedWords:
                            repeatedWords.append(word)

    print('There is repetition of the word(s)', str(repeatedWords),'.')
                

def anaphora(sentenceBank):
    # sentencebank = ["sent","sent"...]
    alreadyAnaphoraed=[]
    for index in range(0,len(sentenceBank)-1):
        sentence = sentenceBank[index]
        nextSentence = sentenceBank[index+1]
   
        wordsInSentence = sentence.lower().split(' ')
        wordsInNextSentence = nextSentence.lower().split(' ')

        if wordsInSentence[0]==wordsInNextSentence[0]:
                 if wordsInSentence[1]==wordsInNextSentence[1]:
                     if wordsInSentence[0] and wordsInSentence[1] not in alreadyAnaphoraed:
                         alreadyAnaphoraed.append(str(wordsInSentence[0]))
                         alreadyAnaphoraed.append(str(wordsInSentence[1]))
                         print('')
                         if wordsInSentence[2]!=wordsInNextSentence[2]:
                             print('You have an anaphora. The phrase "', wordsInSentence[0], wordsInSentence[1],'" was repeated.')

                         else:
                             print('You have an anaphora. The phrase "', wordsInSentence[0], wordsInSentence[1], wordsInSentence[2],'" was repeated.')

                         

simile(sentenceBank)
print('')
repetition(sentenceBank)
anaphora(sentenceBank)

file.close()
