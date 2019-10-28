#!/usr/bin/python
# Prints list of windows in the current workspace.
import sys
from AppKit import NSWorkspace
from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)

curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()
curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
curr_app_name = curr_app.localizedName()
options = kCGWindowListOptionOnScreenOnly
windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
for window in windowList:
    pid = window['kCGWindowOwnerPID']
    windowNumber = window['kCGWindowNumber']
    ownerName = window['kCGWindowOwnerName']
    geometry = window['kCGWindowBounds']
    windowTitle = window.get('kCGWindowName', u'Unknown')
    if curr_pid == pid:
        print(windowTitle.encode('utf-8'))