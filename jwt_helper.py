import jwt
import datetime

class JWTAuthenticator:

    def __init__(self, secret, algorithm):
        self.secret = secret
        self.algorithm = algorithm

    
    def encode_payload(self, payload, expiration=3600):
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration)
        encoded_token = jwt.encode(payload, self.secret, self.algorithm)
        return encoded_token

    def decode_token(self, token):
        try:
            decoded_token = jwt.decode(token, self.secret, self.algorithm)
        except (jwt.ExpiredSignatureError, jwt.DecodeError, jwt.InvalidTokenError) as e:
            raise e
            
        return decoded_token


if __name__ == "__main__":

    payload = {
        "username": "mohsin-ashraf",
        "role": "manager"
    }

    jwt_auth = JWTAuthenticator("yoursecretkeygoeshere", 'HS256')
    
    encoded_token = jwt_auth.encode_payload(payload)
    print (encoded_token)
    decoded_token = jwt_auth.decode_token(encoded_token)
    print (decoded_token)
