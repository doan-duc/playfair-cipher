#Tạo ma trận mã hóa
def create_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix_chars = []
    # Thêm các ký tự của khóa vào ma trận
    for char in key:
        if char.isalpha() and char not in matrix_chars:
            matrix_chars.append(char)
    # Chữ cái còn lại
    for i in range(26):
        char = chr(i + 65)
        if char == 'J':
            continue
        if char not in matrix_chars:
            matrix_chars.append(char)   
    # Định dạng matrix 5x5
    matrix = []
    for i in range(5):
        matrix.append(matrix_chars[i*5 : i*5 + 5])
        
    return matrix

#In ma trận
def print_matrix(matrix):
    print("Playfair Matrix (5x5):")
    for row in matrix:
        print(" ".join(row))
    print()

#Xử lý văn bản
def preprocess_text(text):
    # Chuyển thành in hoa, thay J bằng I
    text = text.upper().replace('J', 'I')
    cleaned_text = ""
    for char in text:
        if char.isalpha():
            cleaned_text += char
    # Chia thành các cặp
    pairs = []
    i = 0
    while i < len(cleaned_text):
        if i == len(cleaned_text) - 1:
            pairs.append(cleaned_text[i] + 'X')
            i += 1
        elif cleaned_text[i] == cleaned_text[i+1]:
            pairs.append(cleaned_text[i] + 'X')
            i += 1
        else:
            pairs.append(cleaned_text[i] + cleaned_text[i+1])
            i += 2
            
    return pairs

def find_position(matrix, char):
    #Tìm vị trí (hàng, cột) của một ký tự trong ma trận
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

#Mã hóa chuỗi ký tự
def encrypt(plaintext, key):
    matrix = create_matrix(key)
    pairs = preprocess_text(plaintext)
    ciphertext = ""
    for pair in pairs:
        r1, c1 = find_position(matrix, pair[0])
        r2, c2 = find_position(matrix, pair[1])
        #Cùng hàng -> Dịch sang phải 1 (quay vòng)
        if r1 == r2:
            ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        #Cùng cột -> Dịch xuống dưới 1 (quay vòng)
        elif c1 == c2:
            ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        #Khác hàng, khác cột -> Lấy góc đối xứng hình chữ nhật (giữ nguyên hàng)
        else:
            ciphertext += matrix[r1][c2] + matrix[r2][c1]   
    return ciphertext
