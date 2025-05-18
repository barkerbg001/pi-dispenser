import decimal
import math

def compute_pi(digits):
    decimal.getcontext().prec = digits + 2  # extra digits for accuracy
    a = decimal.Decimal(1)
    b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(0.25)
    p = decimal.Decimal(1)
    for _ in range(int(math.log2(digits)) + 1):
        an = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - an) ** 2
        a = an
        p *= 2
    pi = (a + b) ** 2 / (4 * t)
    return str(pi)[:digits + 2]  # 3. + digits

if __name__ == "__main__":
    digits = int(input("Enter number of digits to calculate for Pi: "))
    pi_digits = compute_pi(digits)
    print(f"Pi to {digits} digits:")
    print(pi_digits)
