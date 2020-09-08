# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    if p==s:
        return 1
    if p>s:
        return 0
    counter=0
    while s>=m :
        if p>=m:
            if p>s:
                return counter
            s-=p
            p-=d
            counter+=1
        else:
            s-=m
            counter+=1
    return counter


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
