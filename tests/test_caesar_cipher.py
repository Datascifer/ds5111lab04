import sys
sys.path.append('.')

from scripts import caesar_cipher

def test_encode_decode():
    original = "hello!"
    encoded = caesar_cipher.encode(original)
    decoded = caesar_cipher.decode(encoded)
    assert decoded == original  
