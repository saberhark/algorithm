import time

# 이전코드보다 이게 빠름 이유는 봐야됨
def solution(numbers):
    answer = []
    arr = set()

    permutation(arr, [int(i) for i in numbers])

    prime = aristo(max(arr)+1)

    for n in arr:
        if prime[n]:
            answer.append(n)
    return len(answer)


def permutation(arr, nums, prefix=0):
    for idx in range(len(nums)):
        if nums[idx] < 0:
            continue
        arr.add(prefix * 10 + nums[idx])
        tmp = nums[idx]
        nums[idx] = -1
        permutation(arr, nums, prefix*10+tmp)
        nums[idx] = tmp


def aristo(n):
    nums = [True] * n
    nums[0] = False
    nums[1] = False

    l = int(len(nums) ** 0.5)

    for idx in range(2, l+1):
        if not nums[idx]:
            continue
        for j in range(idx+idx, n, idx):
            nums[j] = False
    #return [idx for idx in range(2,n) if nums[idx] == True]
    return nums


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

def solution1(numbers):
    answer = 0
    arr = [int(i) for i in numbers]
    prime = [1]*(10**len(numbers))

    prime[0] = 0
    prime[1] = 0
    for i in range(2,int(len(prime)**(1/2))):
        if prime[i]==1:
            for i in range(i*2,len(prime), i):
                prime[i]=0
    #for i in range(len(prime)):
    #    print(i,prime[i])

    permutation1(0, arr, prime)
    answer=prime.count(2)

    return answer

def permutation1(num, arr, prime):
    check(num, prime)
    for _ in arr:
        tmp = arr[0]
        permutation1(num*10 + arr.pop(0), arr, prime)
        arr.append(tmp)

def check(num, prime):
    if prime[num]==1:
        prime[num]=2
        return 1
    else:
        return 0

st = time.time()
solution1("1234567")
ed = time.time()

st1 = time.time()
solution("1234567")
ed1 = time.time()

print(ed - st, ed1 - st1)
