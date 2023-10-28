"""
My solution to "Pattern Permutations"
"""
import itertools

def contained_in_words(perm, word_list):
    """Checks if a permutation is contained in any of the words in a list of words"""
    for word in word_list:
        if perm in word:
            return True
    return False


def main():
    """Main Function"""
    # reads input
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        # get all necessary input
        special_word, num_words = input().split()
        words =[]
        for _ in range(int(num_words)):
            words.append(input())
        
        # generate permutations of special word and stores them all in a list
        permutations = list(itertools.permutations(special_word))
        
        #joins each permutation into one string
        permutations = [''.join(p) for p in permutations]
        
        # this variable will keep track of each permutation being contained in the list
        contains_permutations = True
        for perm in permutations:
            contains_permutations = contains_permutations and contained_in_words(perm, words)
            if not contains_permutations:
                print('no')
                break
        if contains_permutations:
            print('yes')
            
        
if __name__=="__main__":
    main()
    