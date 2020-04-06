
import norm_punc
# used the toolkit phrasal nomalizer, info:https://pypi.org/project/phrasal/
def processQuestion(text):
    standardText= "abcdefghijklmnopqrstuvwsyz- "
    temp=""
    normalizedText = norm_punc.normalize_text(str(text.lower()), fix_encoding=True, strip_emojis=True)
    for char in normalizedText:
        for standardchar in standardText:
            if standardchar==char:
                temp+=char
                break
    return temp
