import pyperclip
import re

# 这些字符需要使用空字符串代替
CharacterToBeDiscarded = ['.', '/', '(', ')', '，', '>', '<', ',']

# 这些字符需要使用 - 代替
CharacterToBeCross = [' ']

# 去除首尾空格
def trimSpace(rawMaterial):
    temp = rawMaterial.strip()
    return temp

# 大写转小写
def lower(rawMaterial):
    return rawMaterial.lower()

# 将部分字符使用 `-` 代替
def toCross(rawMaterial):
    targets = ''.join(CharacterToBeCross)
    return re.sub('[%s]' % targets, '-', rawMaterial)

# 将部分字符去掉
def discardCharacter(rawMaterial):
    targets = ''.join(CharacterToBeDiscarded)
    return re.sub('[%s]' % targets, '', rawMaterial)

def transferToItem(rawMaterial):
    if len(rawMaterial) > 0:
        temp = trimSpace(rawMaterial)
        temp = lower(temp)
        temp = toCross(temp)
        temp = discardCharacter(temp)
        return temp

    return None

if __name__ == '__main__':
    rawMaterial = pyperclip.paste()
    target = transferToItem(rawMaterial)
    if target:
        pyperclip.copy(target)
