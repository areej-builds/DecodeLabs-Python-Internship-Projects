import string
import secrets
import math

def calculate_entropy(length, pool_size):
    """Calculates the information entropy of the password in bits."""
    if pool_size <= 0 or length <= 0:
        return 0
    return length * math.log2(pool_size)

def generate_enterprise_password():
    print("=== DecodeLabs Enterprise Password Generator ===")
    
    # Phase 1: Input & Validation
    try:
        length = int(input("Enter desired password length (Recommended: 15+): "))
        if length <= 0:
            print("Error: Password length must be a positive integer.")
            return
        elif length < 8:
            print("Warning: Passwords shorter than 8 characters are highly insecure.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return

    # Phase 2: Process (Character Classification & Secure Selection)
    # Combining uppercase letters, lowercase letters, digits, and symbols
    character_pool = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(character_pool)
    
    # Using secrets.choice() for cryptographic security (Hardware-level OS entropy)
    # Using list comprehension + ''.join() for optimal linear O(N) memory efficiency
    password_list = [secrets.choice(character_pool) for _ in range(length)]
    secure_password = ''.join(password_list)

    # Phase 3: Output & Entropy Validation
    entropy = calculate_entropy(length, pool_size)
    
    print("\n--- Generation Report ---")
    print(f"Generated Password : {secure_password}")
    print(f"Password Length    : {length} characters")
    print(f"Character Pool Size: {pool_size} unique characters")
    print(f"Calculated Entropy : {entropy:.2f} bits")
    
    # Simple security threshold feedback based on entropy bits
    if entropy < 60:
        print("Security Status    : WEAK (Easily crackable)")
    elif entropy < 80:
        print("Security Status    : MEDIUM (Moderate resistance)")
    else:
        print("Security Status    : STRONG (Enterprise Grade Secure)")
    print("--------------------------")

if __name__ == "__main__":
    generate_enterprise_password()
