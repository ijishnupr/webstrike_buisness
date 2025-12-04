from argon2 import PasswordHasher

def create_hashed_password():
    ph = PasswordHasher()
    plain_password = "admin"
    hashed_password = ph.hash(plain_password)
    print("\nHashed Password:")
    print(hashed_password)

if __name__ == "__main__":
    create_hashed_password()
