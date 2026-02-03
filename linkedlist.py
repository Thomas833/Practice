def main(array, target):
    hashmap = {}
    complement = 0;
    for i,num in enumerate(array):
        complement = target - num;
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i
        
    return []


print(main([2,5,5,9,7], 9))