#此语言按照python语言程序设计标准，只是将结尾限定为#
'''
句子应当是一句一句分析，每一句生成一个list。
如果碰到句子中包含有if的，应当在主程序中判断并决定是否输出if中包含的语句。
由于本语言没有缩进等方法，故如果结束if语句应输入endif
本语言都以浮点数进行运算和赋值
预想的几种报错：
1.输入格式不正确，比如a=14.5.6,数字有两个小数点应当是认为错误的
2.不在本语言识别内的字符
'''
keyWordDict={'if':'条件语句的开始','else':'条件语句的分支','elif':'条件语句的分支','endif':'条件语句的结束'}
virableDict={}
constantDict={}

def loadFile():
    dataMat = []; labelMat = []
    fr = open('code.txt')
    codes=fr.read().split('#')
    fr.close()
    codes.remove('')
    return codes



def analyseLine(code:str):
    strList=[]
    l=r=0
    if len(code)==0:
        return
    while r<len(code) and l<len(code):
        if code[l].isalpha():
            while r<len(code) and  (code[r].isdigit() or code[r].isalpha()):
                r+=1
            if code[l:r] not in keyWordDict.keys():#如果不是保留字
                if code[l:r] not in virableDict.keys():
                    virableDict[code[l:r]]=''
                    strList.append(('virableDict',code[l:r]))
                else:
                    strList.append(('virableDict',code[l:r]))
            else:
                strList.append(('virableDict',code[l:r]))
        elif code[l].isdigit() or (code[l+1].isdigit() and code[l]=='-'):
            while r<len(code) and  (code[r].isdigit() or code[r]=='.'):
                r+=1
            try:
                num=float(code[l:r])
            except BaseException:
                strList.append(('Error!','数字输入错误'))
            else:
                if code[l:r] not in constantDict.keys():
                    constantDict[code[l:r]]=num
                    strList.append(('constantDict',code[l:r]))
                else:
                    strList.append(('constantDict',code[l:r]))
        elif code[l]=='+' or code[l]=='*' or code[l]=='/':
            r+=1
            strList.append(('运算符号',code[l]))
        elif code[l]=='=' and code[l+1] !='=':
            r+=1
            strList.append(('赋值符号',code[l]))
        elif code[l]==' ':
            r+=1
        elif (code[l]=='>' ) or (code[l]=='<' ):
            r+=1
            strList.append(('比较符号',code[l:r]))
        elif (code[l]=='=' and code[l+1] =='=') or (code[l]=='>' and code[l+1] =='=') or (code[l]=='<' and code[l+1] =='=') or(code[l]=='<' and code[l+1] =='>'):
            r+=2
            strList.append(('比较符号',code[l:r]))
        else:
            strList.append(('Error','不在识别字符串内，请检查'))
            r+=1
        l=r
    return strList
        

codes= loadFile()
outputList=[]
for i in range(len(codes)):
    outputList.append(analyseLine(codes[i]))
fo=open("output.txt", "w")
fo.write('各检索表为:\n')
fo.write('keyWordDict:   '+str(keyWordDict)+'\n')
fo.write('virableDict:   '+str(virableDict)+'\n')
fo.write('constantDict:  '+str(constantDict)+'\n')
fo.write('识别的语句为:\n')
for i in range(len(outputList)):
    fo.write(str(outputList[i])+'\n')
fo.close()
#print(outputList)
