def solution1(phone_book):
    dic = {}
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) >= len(phone_book[i+1]):
            continue

        dic[phone_book[i]] = 1
        if phone_book[i + 1][0:len(phone_book[i])] in dic:
            return False

    return True


def solution2(phone_books):
    phone_books = sorted(phone_books)
    for idx, phone_book in enumerate(phone_books[:-1]):
        if len(phone_book) < len(phone_books[idx+1]):
            if phone_books[idx+1][0:len(phone_book)] == phone_book:
                return False
        else:
            continue
    return True


print(solution2(["12", "123", "1235", "567", "88"]))
print(solution2(["119", "97674223", "1195524421"]))
