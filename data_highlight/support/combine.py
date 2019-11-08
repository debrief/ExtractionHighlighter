from .token import Token

def combine_tokens(*tokens):
    res = []
    for token in tokens:  
        children = token.children
        res.extend(children)

    return Token(res)
