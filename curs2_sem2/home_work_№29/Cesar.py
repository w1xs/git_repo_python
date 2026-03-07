class Cesar:
    """
    Описание:
        Шифрует/дешифрует латинские буквы в строке при помощи шифра Цезаря

    Параметры:
        data: строка, в которой необходимо провести шифрование/дешифрование
        \n
        side: направление шифрования/дешифрования по алфавиту\n
        (default) side = 0: шифрование/дешифрование производится слева направо\n
        side = 1: шифрование/дешифрование производится справа налево\n
        \n
        step_size: размер сдвига в направлении side\n
        (default) step_size = 0
    """
    __base_structure: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    data: str
    side: int
    step_size: int

    def __init__(self, data: str, side: int = 0, step_size: int = 0):
        self.data = data
        self.side = side
        self.step_size = step_size

    def __encrypt_symbol_from_base(self, char) -> str:
        row_case = char.isupper()
        char = char.lower()
        row_index = self.__base_structure.index(char)
        if self.side == 0:
            base_index = (row_index + self.step_size) % len(self.__base_structure)
        else:
            if self.step_size > row_index:
                base_index = len(self.__base_structure) - (abs(row_index - self.step_size) % len(self.__base_structure))
            else:
                base_index = row_index - self.step_size
        result = self.__base_structure[base_index]
        if row_case:
            return result.upper()
        return result

    def __decrypt_symbol_from_base(self, char) -> str:
        row_case = char.isupper()
        char = char.lower()
        row_index = self.__base_structure.index(char)
        if self.side == 0:
            if self.step_size > row_index:
                base_index = len(self.__base_structure) - (abs(row_index - self.step_size) % len(self.__base_structure))
            else:
                base_index = row_index - self.step_size
        else:
            base_index = (row_index + self.step_size) % len(self.__base_structure)
        result = self.__base_structure[base_index]
        if row_case:
            return result.upper()
        return result

    def encrypt(self) -> str:
        encrypted_data = ""
        for i in range(len(self.data)):
            char = self.data[i]
            if char.isalpha():
                char = self.__encrypt_symbol_from_base(char)
                encrypted_data += char
            else:
                encrypted_data += char
        return encrypted_data

    def decrypt(self) -> str:
        decrypted_data = ""
        for i in range(len(self.data)):
            char = self.data[i]
            if char.isalpha():
                char = self.__decrypt_symbol_from_base(char)
                decrypted_data += char
            else:
                decrypted_data += char
        return decrypted_data

