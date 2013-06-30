# Check for V-Ray shaders with high tracing depth settings
import maya.cmds as cmds
def checkTracingDepth():
	shaders = cmds.ls(type='VRayMtl')
	for shader in shaders:
		if cmds.getAttr(shader+'.refractionsMaxDepth') > 5:
			print 'refr: ' + shader
		if cmds.getAttr(shader+'.reflectionsMaxDepth') > 5:
			print 'refl: ' + shader
checkTracingDepth()