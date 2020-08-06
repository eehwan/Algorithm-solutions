import sys

num=["0","1","2","3","4","5","6","7","8","9"]

files = list(map(str,input().replace("[","").replace("]","").replace("\"","").split(", ")))
# print(files)

def depart(file):
    agu1,agu2,agu3 = "","",""
    file_alp = list(file)
    length = len(file_alp)
    # print(file_alp,length)
    for i in range(length):
        if file_alp[i] in num:
            # print(f"{i}번째에 숫자")
            agu1 = file_alp[:i]
            for j in range(i+1,length):
                if not(file_alp[j] in num):
                    # print(f"{j}번째에 숫자끝")
                    agu2 = file_alp[i:j]
                    break
            break
        else:
            continue
    return (agu1,agu2)

def merge(x:list):
    result = ""
    for i in x:
        result+=i
    return result

files.sort(key=lambda x:(merge(depart(x.upper())[0]),int(merge(depart(x)[1]))))
print(files)


"""
입력: [“img12.png”, “img10.png”, “img02.png”, “img1.png”, “IMG01.GIF”, “img2.JPG”]
출력: [“img1.png”, “IMG01.GIF”, “img02.png”, “img2.JPG”, “img10.png”, “img12.png”]

입력: [“F-5 Freedom Fighter”, “B-50 Superfortress”, “A-10 Thunderbolt II”, “F-14 Tomcat”]
출력: [“A-10 Thunderbolt II”, “B-50 Superfortress”, “F-5 Freedom Fighter”, “F-14 Tomcat”]
"""
