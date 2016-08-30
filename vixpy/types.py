import ctypes

VixHandle = ctypes.c_int
VixEventType = ctypes.c_int
VixEventProc = ctypes.CFUNCTYPE(None, VixHandle, VixEventType, VixHandle, ctypes.c_void_p)