import maya.cmds as cmds

'''
Must have selected the objets in outliner to be shifted
'''

def shiftAnimOnSelected( desiredFrame, currentFrame ):
    timeshift = desiredFrame - currentFrame
    selection = cmds.ls(selection=True)
    for s in selection:
        buffer = cmds.listConnections(type='animCurve')
        cmds.keyframe(buffer, edit=True, relative=True, option="over", timeChange=timeshift)

'''
currentFrame is the frame that will be shifted to the desiredFrame
example: offset frame 180933 to 1033, desiredFrame is 1033, currentFrame is 180933
'''

shiftAnimOnSelected( desiredFrame, currentFrame )