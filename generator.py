import random
import os


def parse(path):
    with open(os.path.join('data', path)) as file:
        return [line.strip() for line in file.readlines()]


def build_chain(data, n=2):
    chain = {
        '_start': {},
        '_names': set(data)
    }
    [add_word(word + '.', chain, n) for word in data]
    [add_word(word + '.', chain, n + 1) for word in data]
    return chain


def add_word(word, chain, n):
    weight = 2 if n == 2 else 1
    for i in range(0, len(word) - n):
        tuple = word[i:i + n]
        next = word[i + 1:i + n + 1]
        chain.setdefault(tuple, {})
        entry = chain[tuple]
        if i == 0:
            chain['_start'][tuple] = chain['_start'].get(tuple, 0) + 1
        entry[next] = entry.get(next, 0) + weight


def generate(chain):
    tuple = random.choice(list(chain['_start'].keys()))
    result = [tuple]
    while True:
        tuple = random.choices(
            list(chain[tuple].keys()),
            list(chain[tuple].values())
        )[0]
        last = tuple[-1]
        if last == '.':
            break
        else:
            result.append(last)

    generated = ''.join(result)
    if generated not in chain['_names']:
        return generated
    else:
        return generate(chain)


for i in range(10):
    # print(generate(build_chain(parse('dwarf.txt'))))
    # print(generate(build_chain(parse('tolkien-names.txt'))))
    # print(generate(build_chain(parse('tiefling.txt'))))
    print(generate(build_chain(parse('greek-mythology.txt'))))
