# Author:  Brett Bittola
# GitHub username: brettbittola
# Date: 11/18/2023
# Description: A generator function that generates a sequence of numbers from counting the terms in the previous
# sequence of numbers indefinitely.

def count_seq():
    """Generates a sequence of numbers from counting the terms in the previous sequence of numbers"""
    loops = 0

    while True:

        if loops == 0:
            seq_n = "2"

        elif loops == 1:
            seq_n = "12"

        else:
            new_seq = []
            i = 0
            while i <= (len(seq_n) - 2):
                count = 1
                while seq_n[i] == seq_n[i+1]:
                    count += 1
                    i += 1
                new_seq.append(str(count))
                new_seq.append(seq_n[i])
                i += 1
            new_seq.append("12")
            seq_n = ''.join(new_seq)
        yield seq_n
        loops += 1
