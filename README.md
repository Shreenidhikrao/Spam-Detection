# Email Spam Detection

## Installing required tools:

pip install nltk
pip install pandas


## To run the code :
python3 email_spam.py


## Expected Output:
python3 email_spam.py 3.22s
label sms
0 ham Go until jurong point, crazy.. Available only ...
1 ham Ok lar... Joking wif u oni...
2 spam Free entry in 2 a wkly comp to win FA Cup fina...
3 ham U dun say so early hor... U c already then say...
4 ham Nah I don't think he goes to usf, he lives aro...
... ... ...
5567 spam This is the 2nd time we have tried 2 contact u...
5568 ham Will ü b going to esplanade fr home?
5569 ham Pity, * was in mood for that. So...any other s...
5570 ham The guy did some bitching but I acted like i'd...
5571 ham Rofl. Its true to its name

[5572 rows x 2 columns]
[nltk_data] Downloading package stopwords to
[nltk_data] /home/shreenidhi/nltk_data...
[nltk_data] Unzipping corpora/stopwords.zip.
[nltk_data] Downloading package punkt to /home/shreenidhi/nltk_data...
[nltk_data] Unzipping tokenizers/punkt.zip.

stopwords are - ['i', 'me', 'my', 'myself', 'we']
punctuation are - !#$%&'()*+,-./:;<=>?@[]^_`{|}~

0 [go, jurong, point, crazy, available, bugis, n...
1 [ok, lar, joking, wif, u, oni]
2 [free, entry, 2, wkly, comp, win, fa, cup, fin...
3 [u, dun, say, early, hor, u, c, already, say]
4 [nah, dont, think, goes, usf, lives, around, t...
Name: processed, dtype: object

spam words - ['free', 'entry', '2', 'wkly', 'comp']
ham words - ['go', 'jurong', 'point', 'crazy', 'available']

Please type a spam or ham message to check if our function predicts accurately
Here are the latest projects and contests matching your skills:
RESULTS
your message is spam, with 90% certainty

