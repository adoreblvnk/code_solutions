import re

def comfortable_word(word):
    uncomfortable = re.compile("([qwerasdfgzxcvb]{2}|[yuiophjklnm]{2})+")
    return False if uncomfortable.search(word) else True
            
