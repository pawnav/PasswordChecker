import sys
import requests
import hashlib


class PasswordChecker(object):
    def __init__(self):

        self.checker_api = 'https://api.pwnedpasswords.com/range/'

    def pwnd_api_check(self, password):
        sha1_password = hashlib.sha1(
            password.encode('utf-8')).hexdigest().upper()
        print(f"sha1 pass: {sha1_password}")
        first5_char, tail = sha1_password[:5], sha1_password[5:]
        print(f"first 5: {first5_char}")
        print(f"rest: {tail}")
        response = self.requests_api_data(first5_char)
        print(f"response: {response}")
        return self.get_password_leaks_count(response, tail)

    def requests_api_data(self, query_char):
        url = self.checker_api + query_char

        try:
            out = requests.get(url)
        except RuntimeError as err:
            print(f"{err} Error, Please try again.")
            out = None
        return out

    def get_password_leaks_count(self, hashes, hash_to_check):
        print(f"hashes: {hashes.text}")
        print(f"hashes to check: {hash_to_check}")
        if hashes is not None:
            hashes = (line.split(':') for line in hashes.text.splitlines())
            for h, count in hashes:
                if h == hash_to_check:
                    return count
            return 0


if __name__ == "__main__":

    pwd = ""

    psw_check = PasswordChecker()

    times = psw_check.pwnd_api_check(password=pwd)

    print(f"This password ({pwd}) has been compromised more than {times} times.")


