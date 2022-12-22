
# import json

def find721(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    # outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    # cleanLines = []
    for line in dirty:
        lowIdx = line.find("BEP-721") # 或 find 'ERC-721 or Compatible token type'
        if lowIdx != -1:
            print("找到'BEP-721': ",lowIdx)
            print(line)
            infopen.close()
            return True
            # print(line[lowIdx:lowIdx+42])
            # cleanLines.append(line[lowIdx:lowIdx+42]+'\n')
    
    # outfopen.writelines(cleanLines)
    infopen.close()
    # outfopen.close()
    return False

if __name__=='__main__':
    find721('res-era7-721.json')
