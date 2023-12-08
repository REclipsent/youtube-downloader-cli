def verb_print(text: str = None, verbose: bool = None):
    if not verbose:
        return
    if text is None:
        raise ValueError
    print(f'INFO | {text}')