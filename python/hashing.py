

def my_hash(string, table_size):

    sum_ = 0
    for pos in range(len(string)):
        sum_ += ord(string[pos])

    return sum % table_size


astring = 'asdfghijkl'

print(hash(astring, len(astring)))