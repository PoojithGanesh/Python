def is_isogram(sentence):
  cleaned_sentence=sentence.replace(" ", "").lower()
  return len(cleaned_sentence)==len(set(cleaned_sentence))
sentence="abcdefghijklmnopqrstuvwxyz"
print(is_isogram(sentence))
