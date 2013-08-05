from nltk.corpus import stopwords
corpus = "I went to the park." #This will be replaced by the lectures
filtered_words = [w for w in word_list if not w in stopwords.words('english')]
print filtered_words