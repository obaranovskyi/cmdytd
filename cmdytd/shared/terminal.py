def replace_terminal_encoding(value_to_decode: str):
    return value_to_decode   \
        .replace('\\&', '&') \
        .replace('\\@', '@') \
        .replace('\\?', '?') \
        .replace('\\=', '=') \
        .replace('\\(', '(') \
        .replace('\\)', ')')
