import maya.cmds as cmds

def processAnimCurves( desiredFrame, currentFrame ):
    """
    Function that calculates the frame difference, selects the animCurves
    and proceeds to shift according to the timeshift value
    """
    timeshift = desiredFrame - currentFrame
    animCurves = cmds.ls(type='animCurve') #selects all animCurves
    cmds.keyframe(animCurves, edit=True, relative=True, option="over", timeChange=timeshift)

"""
currentFrame is the frame that will be shifted to the desiredFrame
    example: offset frame 180933 to 1033, desiredFrame is 1033, currentFrame is 180933
"""

processAnimCurves( desiredFrame, currentFrame )