from ctypes import *
from ctypes.wintypes import *

PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_READWRITE = 0x04

class STARTUPINFO(Structure):
	_fields_ =[
		("cb",	DWORD),
		("lpReserved",	LPSTR),
		("lpDesktop",	LPSTR),
		("lpTitle",	LPSTR),
		("dwX",	DWORD),
		("dwY",	DWORD),
		("dwXSize",	DWORD),
		("dwYSize",	DWORD),
		("dwXCountChars", DWORD),
		("dwYCountChars",	DWORD),
		("dwFillAttribute",	DWORD),
		("dwFlags",	DWORD),
		("wShowWindow",	WORD),
		("cbReserved2",	WORD),
		("lpReserved2",	LPBYTE),
		("hStdInput",	HANDLE),
		("hStdOutput",	HANDLE),
		("hStdError",	HANDLE),
	]

class PROCESS_INFORMATION(Structure):
	_fields_ = [
		("hProcess",	HANDLE),
		("hThread",	HANDLE),
		("dwProcessId",	DWORD),
		("dwThreadId",	DWORD),
	]

class PROCESSENTRY32(Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ProcessID", DWORD),
        ("th32DefaultHeapID", POINTER(wintypes.ULONG)),
        ("th32ModuleID", DWORD),
        ("cntThreads", DWORD),
        ("th32ParentProcessID", DWORD),
        ("pcPriClassBase", LONG),
        ("dwFlags", DWORD),
        ("szExeFile", CHAR * 260),
    ]

class MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("th32ModuleID", DWORD),
        ("th32ProcessID", DWORD),
        ("GlblcntUsage", DWORD),
        ("ProccntUsage", DWORD),
        ("modBaseAddr", POINTER(wintypes.BYTE)),
        ("modBaseSize", DWORD),
        ("hModule", HMODULE),
        ("szModule", CHAR * 256),
        ("szExePath", CHAR * 260),
    ]

