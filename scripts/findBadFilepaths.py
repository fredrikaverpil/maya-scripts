# This script searches all nodes for filepaths which begin with C:, R: or X: ...

import maya.cmds as cmds
errors = 0
log = []
nodeTypes = cmds.allNodeTypes()
for nodeType in nodeTypes:
  nodes = cmds.ls(type=nodeType)
	for node in nodes:
		attributes = cmds.listAttr(node, write=True, hasData=True )
		for attribute in attributes:
			try:
				if 'C:' in cmds.getAttr(node+'.'+attribute) or 'R:' in cmds.getAttr(node+'.'+attribute) or 'X:' in cmds.getAttr(node+'.'+attribute):
					#print 'Found invalid drive letter in : ' + cmds.getAttr(node+'.'+attribute)
					log.append(node +': ' +  cmds.getAttr(node+'.'+attribute) + ' (nodetype ' + nodeType + ')')
					errors += 1
			except:
				pass

print '\n-------Summary -------'
print 'Found ' + str(len(nodeTypes)) + ' possible node types.'
print 'Found ' + str(len(nodes)) + ' nodes in scene.'
print 'Found ' + str(errors) + ' invalid filepaths.'
for item in log:
    print item
