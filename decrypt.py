from encrypt import create_matrix, find_position

#Giải mã
def decrypt(ciphertext, key):
    matrix = create_matrix(key)
    cleaned_text = ""
    for char in ciphertext.upper().replace('J', 'I'):
        if char.isalpha():
            cleaned_text += char
    # Chuẩn bị ciphertext thành các cặp 2 ký tự
    pairs = []
    for i in range(0, len(cleaned_text), 2):
        pairs.append(cleaned_text[i:i+2])
    plaintext = ""
    for pair in pairs:
        if len(pair) < 2:
            break
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        # Quy luật ngược: 
        # Cùng hàng -> Dịch sang trái 1 (quay vòng)
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
        # Cùng cột -> Dịch lên trên 1 (quay vòng)
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
        # Khác hàng, khác cột -> Lấy góc đối xứng hình chữ nhật (giữ nguyên hàng)
        else:
            plaintext += matrix[r1][c2] + matrix[r2][c1]
    return plaintext
