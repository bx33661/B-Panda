import base64

def encode_base64(input_string):
    """
    将字符串编码为 Base64
    :param input_string: 需要编码的字符串
    :return: Base64 编码后的字符串
    """
    try:
        # 将字符串编码为字节
        byte_data = input_string.encode('utf-8')
        # 使用 base64 编码
        base64_bytes = base64.b64encode(byte_data)
        # 将字节转换回字符串
        base64_string = base64_bytes.decode('utf-8')
        return base64_string
    except Exception as e:
        return f"编码错误: {str(e)}"

def decode_base64(base64_string):
    """
    将 Base64 字符串解码为原始字符串
    :param base64_string: Base64 编码的字符串
    :return: 解码后的原始字符串
    """
    try:
        # 将 Base64 字符串编码为字节
        base64_bytes = base64_string.encode('utf-8')
        # 使用 base64 解码
        byte_data = base64.b64decode(base64_bytes)
        # 将字节转换回字符串
        decoded_string = byte_data.decode('utf-8')
        return decoded_string
    except Exception as e:
        return f"解码错误: {str(e)}"