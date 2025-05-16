import re

def getMetaData(file):
    match = re.match(r'([^\d]+)(\d+)', file)
    head, number = match.group(1), match.group(2)
    return (head.lower(), int(number))

def solution(files):
    return sorted(files, key=getMetaData)

if __name__ == '__main__':
    samples = [
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
        ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
    ]
    results = [solution(x) for x in samples]
    print(*results, sep='\n')
