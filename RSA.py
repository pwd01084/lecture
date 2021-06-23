from random import randint


# 서로 다른 2개의 소수 고르기


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    prime1 = prim2 = 0
    while not is_prime(prime1):
        prime1 = randint(start, end -1)
    while not is_prime(prim2):
        prime2 = randint(start, end -1)
    return prime1, prime2


# phi를 구하고 서로소인 e를 준비
# 최대 공약수가 1 이니 유클리드 이용

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def find_e(phi):
    e = None
    for i in range(2, phi):
        if gcd(phi, i) == 1:
            e = i
            break
    return e


def find_d(phi, e):
    d = None
    for i in range(phi //e, phi):
        if e * i % phi == 1:
            d = i
            break
    return d


def generate_keys():
    n, e, d = 0, None, None
    while e is None or d is None:
        prime1, prime2 = find_primes(1000, 10000)
        n = prime1 * prime2
        phi = (prime1 -1) * (prime2 - 1)
        e = find_e(phi)
        d = find_d(phi, e)
    return n,e,d


def get_mod(message, exp, n):
    result = message
    for i in range(1, exp):
        result = (result * message) % n
    return result

def encrypt(message, e, n):
    return get_mod(message, e, n)


def decrypt(message, d, n):
    return get_mod(message, d, n)

def main():
    message : int = int(input("암호화할 숫자를 입력하세요 : "))
    n, e, d = generate_keys()
    print("공개키 : ",n,e,"개인키 : ",d)
    encrypted = encrypt(message, e, n)
    print("암호화된 숫자 : ", encrypted)
    decrypted = decrypt(encrypted, d, n)
    print("복호화된 숫자 : ", decrypted)



if __name__ == '__main__':
    main()