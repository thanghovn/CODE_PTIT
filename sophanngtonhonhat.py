import sys
import bisect

anti_primes = [
    1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260,
    1680, 2520, 5040, 7560, 10080, 15120, 20160, 25200, 27720, 45360, 50400,
    55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400,
    665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320,
    6486480, 7207200, 8648640, 10810800
]


def main():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    results = []

    for i in range(1, t + 1):
        x = int(input_data[i])
        # Tìm số phản nguyên tố nhỏ nhất >= x
        idx = bisect.bisect_left(anti_primes, x)
        results.append(str(anti_primes[idx]))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    main()