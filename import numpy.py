def nhapvao():
    return input("Nhap vao: ")
def bai_1():
    s = nhapvao()
    return len(s)
def bai_2():
    s = nhapvao()
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
def bai_3():
    s = nhapvao()
    if len(s) < 2:
        return ""
    return s[:2] + s[-2:]
def bai_4():
    s = nhapvao()
    return s[0] + s[1:].replace(s[0], "$")
def bai_5():
    a = nhapvao()
    b = nhapvao()
    return b[:2] + a[2:] + " " + a[:2] + b[2:]
def bai_6():
    s = nhapvao()
    if len(s) < 3:
        return s
    elif s.endswith("ing"):
        return s + "ly"
    else:
        return s + "ing"
def bai_7():
    s = nhapvao()
    n = s.find("not")
    p = s.find("poor")
    if n != -1 and p != -1 and n < p:
        return s[:n] + "good" + s[p+4:]
    return s
def bai_8():
    words = nhapvao().split()
    longest = max(words, key=len)
    return longest, len(longest)
def bai_9():
    s = nhapvao()
    n = int(input("Nhap vi tri can xoa: "))
    return s[:n] + s[n+1:]
def bai_10():
    s = nhapvao()
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]
def bai_11():
    s = nhapvao()
    return "".join([s[i] for i in range(len(s)) if i % 2 == 0])
def bai_12():
    s = nhapvao().split()
    freq = {}
    for w in s:
        freq[w] = freq.get(w, 0) + 1
    return freq
def bai_13():
    s = nhapvao()
    return s.upper(), s.lower()
def bai_14():
    s = nhapvao()
    words = list(set(s.split(",")))
    return ",".join(sorted([w.strip() for w in words]))
def bai_15():
    tag = nhapvao()
    word = nhapvao()
    return f"<{tag}>{word}</{tag}>"
def bai_16():
    a = nhapvao()
    b = nhapvao()
    mid = len(a) // 2
    return a[:mid] + b + a[mid:]
def bai_17():
    s = nhapvao()
    if len(s) < 2:
        return "Chuoi qua ngan."
    return s[-2]*4
def bai_18():
    s = nhapvao()
    if len(s) < 3:
     return s
    return s[0:3]
def bai_19():
    s = nhapvao()
    ch = input("Nhap ky tu can lay truoc: ")
    x = s.find(ch)
    if x != -1:
        return s[x:]
    return s
def bai_20():
    s = nhapvao()
    if len(s) % 4 == 0:
        return s[::-1]
    return s
def bai_21():
    s = nhapvao()
    a = sum(1 for ch in s[:4] if ch.isupper())
    if a >= 2:
        return s.upper()
    return s
def bai_22():
    s = nhapvao()
    return "".join(sorted(s))
def bai_23():
    s = nhapvao()
    return s.replace("\n", "")
def bai_24():
    s = nhapvao()
    p = input("Nhap ky tu ")
    return s.startswith(p)
def bai_25():
    text = nhapvao()
    shift = int(input("Nhap do dich Caesar: "))
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result
def bai_26():
    s = nhapvao()
    import textwrap
    s = textwrap
    return textwrap.fill(s, width=50)
def bai_27():
    s = nhapvao()
    return "\n".join(line.strip() for line in s.splitlines() if line.strip())
def bai_28():
    s = nhapvao()
    prefix = input("Nhap tien to: ")
    return "\n".join(prefix + line for line in s.splitlines())
def bai_29():
    s = nhapvao()
    indent = int(input("Nhap so khoang trang cho dong dau: "))
    lines = s.splitlines()
    if not lines: return ""
    lines[0] = " "* indent + lines[0]
    return "\n".join(lines)
def bai_31():
    num = float(input("Nhap so thuc: "))
    return f"{num:+.2f}"
def bai_30():
    num = float(input("Nhap so thuc: "))
    return f"{num:.2f}"
def bai_32():
    num = float(input("Nhap so thuc: "))
    return f"{num:.0f}"
def bai_33():
    num = int(input("Nhap so nguyen: "))
    width = int(input("Nhap do rong: "))
    return f"{num:0{width}d}"
def bai_34():
    num = int(input("Nhap so : ")) 
    width = int(input("Nhap do rong: "))
    return f"{num:*<{width}}"
def bai_35():
    num = float(input("Nhap so : "))
    return f"{num:,}"
def bai_36():
    num = float(input("Nhap so : "))
    return f"{num:.2%}"
def bai_37():
    num = (input("Nhap so : "))
    return f"{num:<10}{num:^10}{num:>10}"
def bai_38():
    s = nhapvao()
    sub = input("Nhap chuoi con: ")
    return s.count(sub)
def bai_39():
    s = nhapvao()
    return s[::-1]
def bai_40():
    s = nhapvao()
    return " ".join(reversed(s.split()))
def bai_41():
    s = nhapvao()
    x =input("Nhap ky tu can xoa: ")
    return  "".join(ch for ch in s if ch not in x)
def bai_42():
    s = nhapvao()
    from collections import Counter
    c = Counter(s)
    return {k: v for k, v in c.items() if v > 1}
def bai_43():
    import math
    l = float(input("Nhap do dai: "))
    w = float(input("Nhap do rong: "))
    r = float(input("Nhap ban kinh hinh tru: "))
    h = float(input("Nhap chieu cao hinh tru: "))
    area = l * w
    volume = math.pi * r**2 * h
    return f"Area of the rectangle: {area:.2f} cm^2, Volume of the cylinder: {volume:.3f}cm^3"
def bai_44():
    s = nhapvao()
    return [(ch, i) for i, ch in enumerate(s)]
def bai_45():
    import string 
    s = nhapvao().lower()
    return set(string.ascii_lowercase).issubset(set(s))
def bai_46():
    s = nhapvao()
    return s.split()
def bai_47():
    s = nhapvao()
    n = int(input("Nhap so ky tu : "))
    return s[:n].lower() + s[n:]
def bai_48():
    s = nhapvao()
    return s.replace(",","tmp").replace(".",",").replace("tmp", ".")
def bai_49():
    s = nhapvao().lower()
    vowels = "aeiou"
    return {v: s.count(v) for v in vowels if v in s}
def bai_50():
    s = nhapvao()
    delim = input("Nhap ky tu phan cach: ")
    return s.rsplit(delim, 1)
def main():
    while True:
        print("\n===== MENU =====")
        for i in range(1, 51):
            print(f"{i}. Bai {i}")
        print("0. Thoat")
        chon = input("Chon bai: ").strip()
        if chon == "0":
            break
        elif chon == "1": print(bai_1())
        elif chon == "2": print(bai_2())
        elif chon == "3": print(bai_3())
        elif chon == "4": print(bai_4())
        elif chon == "5": print(bai_5())
        elif chon == "6": print(bai_6())
        elif chon == "7": print(bai_7())
        elif chon == "8": print(bai_8())
        elif chon == "9": print(bai_9())
        elif chon == "10": print(bai_10())
        elif chon == "11": print(bai_11())
        elif chon == "12": print(bai_12())
        elif chon == "13": print(bai_13())
        elif chon == "14": print(bai_14())
        elif chon == "15": print(bai_15())
        elif chon == "16": print(bai_16())
        elif chon == "17": print(bai_17())
        elif chon == "18": print(bai_18())
        elif chon == "19": print(bai_19())
        elif chon == "20": print(bai_20())
        elif chon == "21": print(bai_21())
        elif chon == "22": print(bai_22())
        elif chon == "23": print(bai_23())
        elif chon == "24": print(bai_24())
        elif chon == "25": print(bai_25())
        elif chon == "26": print(bai_26())
        elif chon == "27": print(bai_27())
        elif chon == "28": print(bai_28())
        elif chon == "29": print(bai_29())
        elif chon == "30": print(bai_30())
        elif chon == "31": print(bai_31())
        elif chon == "32": print(bai_32())
        elif chon == "33": print(bai_33())
        elif chon == "34": print(bai_34())
        elif chon == "35": print(bai_35())
        elif chon == "36": print(bai_36())
        elif chon == "37": print(bai_37())
        elif chon == "38": print(bai_38())
        elif chon == "39": print(bai_39())
        elif chon == "40": print(bai_40())
        elif chon == "41": print(bai_41())
        elif chon == "42": print(bai_42())
        elif chon == "43": print(bai_43())
        elif chon == "44": print(bai_44())
        elif chon == "45": print(bai_45())
        elif chon == "46": print(bai_46())
        elif chon == "47": print(bai_47())
        elif chon == "48": print(bai_48())
        elif chon == "49": print(bai_49())
        elif chon == "50": print(bai_50())            
        else:
            print("Lua chon khong hop le.")

if __name__ == "__main__":
    main()
