def main():
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    print(word_search(doc_list, "casino"))
    print(multi_word_search(doc_list, ["casino", "car"]))

    
def word_search(doc_list: list, keyword: str) -> list:
    """
    Args:
    a list of documents (each document is a string) and a keyword. 

    Returns: 
    list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    idx_list = []
    for idx, doc in enumerate(doc_list):
        tokens = doc.split()
        for token in tokens:
            if token.lower().strip(",.") == keyword.lower():
                idx_list.append(idx)
    return list(set(idx_list))


def multi_word_search(doc_list: list, keywords: list) -> dict:
    """
    Args:
    list of documents (each document is a string) and a list of keywords.  

    Returns:
    a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    Example:
    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    return {keyword: word_search(doc_list, keyword) for keyword in keywords}

if __name__ == "__main__":
    main()