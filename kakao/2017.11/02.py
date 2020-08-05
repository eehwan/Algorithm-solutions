alphb = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

text_list = list(str(input()))
def convert(i:int,text):
    if i+1<len(text_list):
        if((text+text_list[i+1]) in alphb):
            # print(f"{text+text_list[i+1]} in alphb")
            return convert(i+1, text+text_list[i+1])
        # print(f"{text+text_list[i+1]} NOT in alphb")
        alphb.append(text+text_list[i+1])
    # print(f"text_list :{text_list}   {len(text_list)}개")
    for _ in range(len(text)):
        text_list.pop(0)
        # print(f"pop:{text_list.pop(0)}")
    # print(text)
    # print(alphb.index(text)+1)
    # print("-----------------------------")
    return text



result=[]
while len(text_list):
    result.append(alphb.index(convert(0,text_list[0]))+1)
print(result)
