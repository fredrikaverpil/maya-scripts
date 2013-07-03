# Delete all renderlayers (including imported ones from references, which do not show up in the render layer list)

import maya.cmds as cmds
renderLayers = cmds.ls(type='renderLayer')

for renderLayer in renderLayers:
    try:
        print 'Deleting ' + renderLayer
        cmds.delete(renderLayer)
    except:
        print 'Could not delete ' + renderLayer
