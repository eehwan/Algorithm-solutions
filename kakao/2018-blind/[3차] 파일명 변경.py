def getMetaData(file):
    number_begin, number_end = 0, len(file)
    for i, char in enumerate(file):
        try:
            int(char)
            if not (number_begin):
                number_begin = i
        except:
            if number_begin:
                number_end = i
                break
            
    print(number_begin, number_end, type(number_begin), type(number_end))
    return [file[0:number_begin].lower(), int(file[number_begin: number_end])]

def solution(files):
    return sorted(files, key=getMetaData)

if __name__ == '__main__':
    samples = [
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
    ]
    results = [solution(x) for x in samples]
    print(*results, sep='\n')
