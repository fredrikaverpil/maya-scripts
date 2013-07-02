# Remove mental ray nodes
def deleteNode(nodeName):
    if cmds.objExists(nodeName):
        try:
            cmds.delete(nodeName)
            print nodeName + ' was deleted.'
        except:
            print nodeName + ' could not be deleted...'

deleteNode('miDefaultOptions')
deleteNode('miContourPreset')
deleteNode('Draft')
deleteNode('DraftMotionBlur')
deleteNode('DraftRapidMotion')
deleteNode('Preview')
deleteNode('PreviewMotionblur')
deleteNode('PreviewRapidMotion')
deleteNode('PreviewCaustics')
deleteNode('PreviewGlobalIllum')
deleteNode('PreviewFinalGather')
deleteNode('Production')
deleteNode('ProductionMotionblur')
deleteNode('ProductionRapidMotion')
deleteNode('ProductionFineTrace')
deleteNode('ProductionRapidFur')
deleteNode('ProductionRapidHair')

deleteNode('miDefaultFramebuffer')
deleteNode('mentalrayItemsList')
