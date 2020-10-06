if __name__ == '__main__':
    n = int(input())
    phonebook = {}
    for i in range(n):
        name, phone = input().split()
        phonebook[name] = phone


    query, queries = input(), []
    try:
        while query != "":
            queries.append(query)
            query = input()
    except:
        for s in queries:
            print("Not found" if s not in phonebook else "{}={}".format(s,phonebook.get(s)))