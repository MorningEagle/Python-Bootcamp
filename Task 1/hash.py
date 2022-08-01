import hashlib

s = "Python Bootcamp"

def hashing(string: str,
            method: str,
            encoding: str = 'utf-8'
            ) -> str:
    """Hashing function

    Args:
        string (str): input value
        method (str): type of method
        encoding (str, optional): Encoding format. Defaults to 'utf-8'.

    Returns:
        str: hash of input value
    """
    return hashlib.new(method, string.encode(encoding)).hexdigest()

print(hashing(s, 'md5'))
print(hashing(s, 'sha1'))
print(hashing(s, 'sha224'))
print(hashing(s, 'sha256'))
print(hashing(s, 'sha384'))
print(hashing(s, 'sha512'))