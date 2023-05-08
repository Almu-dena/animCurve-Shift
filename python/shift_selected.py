import maya.cmds as cmds

#must have selected the objets in outliner to be shifted

def shiftAnimOnSelected( desiredFrame, currentFrame ):
    timeshift = desiredFrame - currentFrame
    selection = cmds.ls(selection=True)
    for s in selection:
        buffer = cmds.listConnections(type='animCurve')
        cmds.keyframe(buffer, edit=True, relative=True, option="over", timeChange=timeshift)


shiftAnimOnSelected( desiredFrame, currentFrame ) #currentFrame is the frame that will be shifted to the desiredFrame