def solution(phone_book):
    s = set(phone_book)
    for phone in s:
        for i in range(len(phone)):
            prefix = phone[:i]
            if prefix in s:
                return False
    return True