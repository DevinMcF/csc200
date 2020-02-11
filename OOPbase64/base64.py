class Base64Converter:
    def __init__(self):
        """
        Create a string containing the Base64 digits for encoding and a
        dictionary containing the numerical value of each digit character
        for decoding.
        """
        self.digits = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        self.digpos = {}
        for pos, dig in enumerate(self.digits):
            self.digpos[dig] = pos
