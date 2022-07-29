import pandas as pd
import nltk

#data cleaning
df = pd.read_csv('sms_spam.txt',sep = '\t', header=None, names=["label", "sms"])
print(df)

#preprocessing
nltk.download('stopwords')
nltk.download('punkt')
sw = nltk.corpus.stopwords.words('english') # this removes the stopwords for example ( “the”, “a”, “an”, “in”)
punc = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

print("\nstopwords are - ",sw[:5])
print("punctuation are -",punc)

def pre_process(sms):
    rem_punc = "".join([word.lower() for word in sms if word not in punc])
    tokenize = nltk.tokenize.word_tokenize(rem_punc) #removing punctuation
    rem_sw = [word for word in tokenize if word not in sw] # removing stop words
    return rem_sw

#adding a column to our data with our processed messages
df['processed'] = df['sms'].apply(lambda x: pre_process(x))

print("\n",df['processed'].head())

def categorize_words():
    spam_words = []
    ham_words = []
    #handling messages associated with spam
    for sms in df['processed'][df['label'] == 'spam']:
        for word in sms:
            spam_words.append(word)
    #handling messages associated with ham
    for sms in df['processed'][df['label'] == 'ham']:
        for word in sms:
            ham_words.append(word)
    return spam_words, ham_words

spam_words, ham_words = categorize_words()

print("\nspam words - ",spam_words[:5])
print("ham words - ",ham_words[:5])

def predict(sms):
    spam_count = 0
    ham_count = 0
    #count the occurances of each word in the sms string
    for word in sms:
        spam_count += spam_words.count(word)
        ham_count += ham_words.count(word)
    print('***RESULTS***')
    #if the message is ham
    if ham_count > spam_count:
        accuracy = round((ham_count / (ham_count + spam_count) * 100)) #predicting the accuraccy of the input not being spam
        print('your messege is not spam, with {}% certainty'.format(accuracy))
    #if the message could be equally spam and ham
    elif ham_count == spam_count:
        print('your message could be spam')
    #if the message is spam
    else:
        accuracy = round((spam_count / (ham_count + spam_count)* 100))
        print('your message is spam, with {}% certainty'.format(accuracy)) #predecting the accuracy of the input being spam

#giving the user input
user_input = input("\nPlease type a spam or ham message to check if our function predicts accurately\n")
#pre-processing the input before prediction
processed_input = pre_process(user_input)
predict(processed_input)



