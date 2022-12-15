
# import json

def find1155(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    # outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    # cleanLines = []
    for line in dirty:
        lowIdx = line.find("ERC-1155 or Compatible token type")
        if lowIdx != -1:
            print("找到'1155': ",lowIdx)
            print(line)
            return True
            # print(line[lowIdx:lowIdx+42])
            # cleanLines.append(line[lowIdx:lowIdx+42]+'\n')
    
    # outfopen.writelines(cleanLines)
    infopen.close()
    return False
    # outfopen.close()

if __name__=='__main__':
    find1155('res-Momo-1155.json')
