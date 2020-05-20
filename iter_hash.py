import hashlib


def do_hash(file_path):
    with open(file_path) as f:
        for line in f:
            hashed_str = hashlib.md5(line.encode()).hexdigest()
            yield hashed_str
