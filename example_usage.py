from client import KZG10Scheme

def main():
    print("=== Testing KZG10 Polynomial Commitment Scheme ===")
    kzg = KZG10Scheme(s=5, modulus=10007)
    
    # Polynomial P(x) = 3 + 2x + x^2
    poly = [3, 2, 1]
    commitment = kzg.commit(poly)
    print(f"Polynomial P(x) = 3 + 2x + x^2")
    print(f"Commitment C = {commitment}")

    # Open at point z = 2
    z = 2
    y, pi = kzg.open(poly, z)
    print(f"Evaluated P({z}) = {y}, Opening Proof pi = {pi}")
    
    valid = kzg.verify(commitment, z, y, pi)
    print(f"KZG Proof Verification: {valid}")
    assert valid, "KZG verification failed"

    # Test tampering
    invalid = kzg.verify(commitment, z, y + 1, pi)
    print(f"Tampered Verification (should be False): {invalid}")
    assert not invalid, "Tampered verification succeeded unexpectedly"

    print("=== KZG10 Commitment Verification Complete ===")

if __name__ == "__main__":
    main()
