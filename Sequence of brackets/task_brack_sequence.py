import sys

n = int(sys.stdin.readline().strip())

def brackets(n, open_count=0, close_count=0, sequence=""):
    if open_count + close_count == 2*n:
        print(sequence)
        return
    if open_count < n:
        brackets(n, open_count+1, close_count, sequence+"(")
    if open_count > close_count:
        brackets(n, open_count, close_count+1, sequence+")")

