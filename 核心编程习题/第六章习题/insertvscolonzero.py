from  time import  time
REPS = 17500

def insert():
    m = [None]
    i = 0
    now = time()
    while i < REPS:
        m.insert(0,i)
        print(m)
        i+=1000
        print('Elapsed (insert):', time() - now)

def colonzero():
    m = [None]
    i = 0
    now = time()
    while i < REPS:
        m[:0] = [i]
        print(m)
        i+=1000
        print('Elapsed (colon-0):', time() - now)



def main():
    insert()
    colonzero()

if __name__ == "__main__":
    main()
