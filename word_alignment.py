import re

# ฟังก์ชันการแปลง list เป็น string
def listToString(s):
    string = ""
    for char in s:
        string += char
    return string


# ฟังก์ชันการแปลง list เป็น string พร้อมเครื่องหมายทับ ( / ) ่ต่อท้าย
def listToStringWithSlash(s):
    string = ""
    for char in s:
        string += char + "/"
    return string


def listToStringWithSpace(s):
    string = ""
    for char in s:
        string += char + " "
    if string[-1] == " ":
        string = string[:-1]
    return string


# การตัดตัวอักษรภาษาอังกฤษ
def alignment_en(text_en):

    # กำหนดการตัดพยัญชนะภาษาอังกฤษเมื่อพบพยัญชนะต่อไปนี้
    consonant_en = "thm|sch|ch|ck|gh|gn|kh|ph|qu|rh|sh|th|wh|b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z"
    # กำหนดการตัดสระภาษาอังกฤษเมื่อพบสระต่อไปนี้
    vowel_en = "ai|ee|ea|eau|ei|eu|ie|io|oa|oe|oo|ou|ui|aea|ae|eou|aa|ao|au|eo|eu|ia|iu|oi|ua|ue|a|e|i|o|u|y"

    convo_en = "r'" + consonant_en + "|" + vowel_en + "'"  # กำหนดรูปแบบในการค้นหา

    result = re.findall(convo_en, text_en)  # เป็นคำสั่งที่ใช้ค้นหา โดย return กลับมาเป็น list ของผลลัพท์ทุกตัว
    if len(result) == 1:
        return result
    if result[0] == "sch":
        result[0] = "s"
        result.insert(1, "ch")
    if result[0] == "p" and result[1] in {"n", "t", "s"}:
        result[0] = "p" + result[1]
        del result[1]
    if result[0] == "k" and result[1] == "n":
        result[0] = "k" + result[1]
        del result[1]
    return result


# การตัดตัวอักษรไทย
def alignment_th(words):
    words = re.findall(
        r"[ก-ฮ]|ะ|า|ิ|ี|ุ|ู|เ|แ|โ|ไ|ใ|์|็|ั|ึ", words
    )  # กำหนดการตัดพยัญชนะและสระภาษาไทย พร้อมทั้งกำหนดรูปแบบการค้นหา

    # ย้ายตำแหน่งการันต์ให้อยู่บนตัวอักษรก่อนหน้า ค/า/ร/ ์ > ค/า/ร์
    index = 0
    for char in words:
        if char in "์":
            words[index - 1] = words[index - 1] + words[index]
            words.remove("์")
        index += 1

    words = words + [
        "",
        "",
    ]  # เติมค่าว่าง 2 ค่าลงใน list เพื่อป้องกัน loop index out of range เพราะมี index+2 ในขั้นตอนถัดไป

    size = len(words) - 1  # กำหนดจำนวนรอบที่จะ loop ตามขนาดของ list-1

    for index in range(size):  # ย้ายตำแหน่งสระประสม

        if index != 0 and index < size - 1:  # ค้นหาสระประสม 2 ตัวอักษร
            currentChar = words[index]
            previousChar = words[index - 1]
            nextChar = words[index + 1]
            nextChar2 = words[index + 2]

            if (
                (previousChar == "เ" and nextChar == "อ")
                or (previousChar == "เ" and nextChar == "า")
                or (previousChar == "เ" and nextChar == "็")
                or (previousChar == "แ" and nextChar == "็")
                or (previousChar == "เ" and nextChar == "ิ")
            ):  # สระประสม 2 ตัวอักษรในภาษาอังกฤษ เ.อ > ไทเกอร์ , เ.า > เบราว์เซอร์, เ.็ > เจ็ต, แ.็ > แบล็ก, เ.ิ > เลิฟ
                # ย้ายตำแหน่งของสระประสมให้ไปอยู่หลังพยัญชนะของสระนั้น เช่น เ/ล/  ิ/ฟ > ล/เ.ิ>ฟ
                words[index] = previousChar + "." + nextChar
                words[index - 1] = currentChar
                words.append("")
                del words[index + 1]

            if (
                previousChar == "เ" and nextChar == "ี" and nextChar2 == "ย"
            ):  # ค้นหาสระประสม 3 ตัวอักษรในภาษาอังกฤษ เ.ีย > นาตาเลีย
                # ย้ายตำแหน่งของสระประสมให้ไปอยู่หลังพยัญชนะของสระนั้น เช่น  เ/ม/  ี/ย/ร์ > ม/เ.ีย/ร์
                words[index] = previousChar + "." + nextChar + nextChar2
                words[index - 1] = currentChar
                del words[index + 2]
                del words[index + 1]
                words.append("")
                words.append("")

            if currentChar == "ิ" and nextChar == "ว":
                words[index] = "." + currentChar + nextChar
                del words[index + 1]
                words.append("")

    # ย้ายตำแหน่งสระเดี่ยว
    index = 0
    for char in words:
        if char in {"เ", "แ", "โ", "ไ"}:  # สระเดี่ยวในภาษาอังกฤษ เ. > เดย์, แ. > แคต, โ. > โซโลมอน, ไ. > ไอโอดีน
            # ย้ายตำแหน่งของสระเดี่ยวให้ไปอยู่หลังพยัญชนะของสระนั้น เช่น  แ/ค/ต > ค/แ./ต
            temp = words[index]
            words[index] = words[index + 1]
            words[index + 1] = temp + "."
        index += 1

    #     #คำสั่งลบค่าว่างใน list
    #     size = len(words)-1
    #     for index in range(size+1,0,-1):
    #         if words[index-1] == '':
    #             words.remove('')

    # สระที่มีพยัญชนะต้นเป็น 'อ'
    if words[0] == "อ":
        if words[1] in {"เ.", "แ.", "ไ.", "โ."}:
            words[0] = words[1] + "อ"
            removeDot = re.findall(r"[ก-ฮ]|ะ|า|ิ|ี|ุ|ู|เ|แ|โ|ไ|ใ|์|็|ั", words[0])
            words[0] = listToString(removeDot)
            del words[1]
        elif words[1] in {"ะ", "า", "อ", "ิ", "ี", "ั"}:
            words[0] = "อ" + words[1]
            del words[1]
    index = 0

    # คำสั่งลบค่าว่างใน list
    size = len(words) - 1
    for index in range(size + 1, 0, -1):
        if words[index - 1] == "":
            words.remove("")
    return words
