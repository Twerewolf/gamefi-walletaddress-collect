

def find20(infile):
    infopen = open(infile, 'r', encoding="utf-8")
    # outfopen = open(outfile, 'w', encoding="utf-8")
    dirty = infopen.readlines()
    for line in dirty:
        lowIdx = line.find("BEP-20 or Compatible token type")
        if lowIdx != -1:
            print("找到'BEP-20': ",lowIdx)
            print(line)
            infopen.close()
            return True
    
    infopen.close()
    return False

if __name__=='__main__':
    projectPath = '/home/tjw/gamefi-walletaddress-collect'
    dataPath = "/data/bscscan-token-"
    contract = "0x97667aeb10b6916001b5431f980c30fb8a9ce4b4"
    tail = ".html"
    file = projectPath+dataPath+contract+tail
    find20(file)