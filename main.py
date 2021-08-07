import json
import random
import bisect
from itertools import accumulate

def calc_accum_weights(neko_json):
    # calc standardization constant
    std_const = sum([v for v in neko_json.values()])

    # calc weights
    weights = [v / std_const for v in neko_json.values()]

    # calc accumulated weights
    accum_weights = list(accumulate(weights))

    return accum_weights

def execute_gacha(accum_weights):
    # search correct index by bisect
    random_value = random.random()
    target_index = bisect.bisect_left(accum_weights, random_value)

    return target_index    

def main():
    # load json
    neko_json = json.load(open('neko.json', 'r'))
    neko_names = [k for k in neko_json.keys()]

    # fetch accmulated weights
    accum_weight = calc_accum_weights(neko_json)

    # execute gacha
    while True:
        print("Type Enter key")
        input_str = input()
        if input_str == "exit":
            exit()
        print(neko_names[execute_gacha(accum_weight)])
        print("If you want to exit, type exit")

if __name__ == "__main__":
    main()