import hashlib

class Mining:
    @staticmethod
    def sha256(message):
        return hashlib.sha256(message.encode('ascii')).hexdigest()

    @staticmethod
    def mine(message, difficulty=1):
        assert difficulty >= 1
        sha256 = Mining.sha256
        prefix = '0' * difficulty
        for i in range(1000):
            digest = sha256(str(hash(message)) + str(i))
            if digest.startswith(prefix):
                print("After " + str(i) + " iterations, found nonce: " + digest)
                return digest
        print("After " + str(i) + " iterations, no nonce found for difficulty: " + str(difficulty))
    
        