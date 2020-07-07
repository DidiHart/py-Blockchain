import hashlib
import json

def stringify(data):
    return json.dumps(data)

def crypto_hash(*args):
    '''
    Return a SHA-256 hash of the given arguments.
    '''
    #stringified_data = json.dumps(data)
    stringified_args = sorted(map(stringify, args)) #make sure the iput always gives the same result no matter the order.
    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest()

def main():
    print(f"crypto_hash('one',2,[3]): {crypto_hash('one',2,[3])}")
    print(f"crypto_hash(2,one,[3]): {crypto_hash(2,'one',[3])}")

if __name__ == '__main__':
    main()
