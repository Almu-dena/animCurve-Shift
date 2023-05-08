import maya.cmds as cmds

def processAnimCurves( desiredFrame, currentFrame ):
    timeshift = desiredFrame - currentFrame
    animCurves = cmds.ls(type='animCurve') #selects all animCurves
    cmds.keyframe(animCurves, edit=True, relative=True, option="over", timeChange=timeshift)


processAnimCurves( desiredFrame, currentFrame ) #currentFrame is the frame that will be shifted to the desiredFrame