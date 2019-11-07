from .token import Token

def combine(*tokens):
    res = []
    for token in tokens:  
        children = token.children
        res.extend(children)

    return Token(res)