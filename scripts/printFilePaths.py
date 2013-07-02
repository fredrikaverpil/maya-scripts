# Print file paths of each file texture
files = cmds.ls(type='file')
for file in files:
    print file + ' loads:\n' + cmds.getAttr(file + '.fileTextureName') + '\n'
