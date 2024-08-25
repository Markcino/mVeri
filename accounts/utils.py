# utils.py
import hashlib

def hash_url(url):
    hash_object = hashlib.sha256(url.encode('utf-8'))
    return hash_object.hexdigest()[:30]  # Shortened to 30 characters
