import nltk
from nltk.tokenize import sent_tokenize
from heapq import nlargest


def summarize(text, n):
    #tokenizing
    sentences = sent_tokenize(text)

    #sentence_score
    scores = {sentence: len(sentence.split()) for sentence in sentences}

    #select_imp_sentences
    top_n = nlargest(n, scores, key=scores.get)
    summary = ' '.join(top_n)

    return summary

text = "The campaign-finance system is built to police who puts money into politics, legal experts say. These groups embodied a flaw: The system is poorly prepared to stop those who raise money and channel it somewhere other than candidates and causes."
summary = summarize(text, n=2)
print(summary)