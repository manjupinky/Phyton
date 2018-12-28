def check_kth_power(n, k):
        while n%k == 0:
            n = n/k

        if n != 1:
            return False
        return True


print check_kth_power(128, 5)
