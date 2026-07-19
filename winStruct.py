from ctypes import *
from ctypes.wintypes import *

PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_READWRITE = 0x04
PAGE_EXECUTE_READWRITE = 0x00000040

kernel32 = windll.kernel32

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
class MEMORY_BASIC_INFORMATION(Structure):
       _fields_ = [
        ("BaseAddress", LPVOID),
        ("AllocationBase", LPVOID),
        ("AllocationProtect", DWORD),
        ("RegionSize", c_size_t),
        ("State", DWORD),
        ("Protect", DWORD),
        ("Type", DWORD),
        ]

kernel32.VirtualAllocEx.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
    wintypes.DWORD,
]
kernel32.VirtualAllocEx.restype = wintypes.LPVOID

kernel32.WriteProcessMemory.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    wintypes.LPCVOID,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t),
]
kernel32.WriteProcessMemory.restype = wintypes.BOOL

kernel32.CreateRemoteThread.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,  # LPSECURITY_ATTRIBUTES
    ctypes.c_size_t,
    wintypes.LPVOID,  # LPTHREAD_START_ROUTINE
    wintypes.LPVOID,
    wintypes.DWORD,
    wintypes.LPDWORD,
]
kernel32.CreateRemoteThread.restype = wintypes.HANDLE

kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.CloseHandle.restype = wintypes.BOOL



class THREADENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", DWORD),
        ("cntUsage", DWORD),
        ("th32ThreadID", DWORD),
        ("th32OwnerProcessID", DWORD),
        ("tpBasePri", LONG),
        ("tpDeltaPri", LONG),
        ("dwFlags", DWORD),
    ]


THREAD_SUSPEND_RESUME = 0x0002
THREAD_GET_CONTEXT    = 0x0008
THREAD_SET_CONTEXT    = 0x0010
THREAD_QUERY_INFORMATION = 0x0040

kernel32.OpenThread.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
kernel32.OpenThread.restype = wintypes.HANDLE

DWORD64 = ctypes.c_uint64


SuspendThread = kernel32.SuspendThread
SuspendThread.argtypes = [wintypes.HANDLE]
SuspendThread.restype = wintypes.DWORD

class PROCESS_BASIC_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("ExitStatus",      wintypes.LONG),
        ("PebBaseAddress",  ctypes.c_void_p),
        ("AffinityMask",    ctypes.c_size_t),
        ("BasePriority",    wintypes.LONG),
        ("UniqueProcessId", ctypes.c_size_t),
        ("InheritedFromUniqueProcessId", ctypes.c_size_t),
    ]


kernel32.VirtualAllocEx.argtypes = (
	wintypes.HANDLE,   # hProcess
	wintypes.LPVOID,   # lpAddress
	ctypes.c_size_t,   # dwSize (SIZE_T)
	wintypes.DWORD,    
	wintypes.DWORD     # flProtect
	)

kernel32.VirtualAllocEx.restype = wintypes.LPVOID

kernel32.VirtualProtectEx.argtypes = (HANDLE, LPVOID, c_size_t, DWORD,POINTER(DWORD) )

kernel32.VirtualProtectEx.restype = BOOL


class ImageDosHeader(Structure):
	_fields_ =[
		("e_magic",	WORD),
		("w_cblp",	WORD),
		("e_cp",	WORD),
		("e_crlc",	WORD),
		("e_cparhdr",	WORD),
		("e_minalloc",	WORD),
		("e_maxalloc",	WORD),
		("e_ss",	WORD),
		("e_sp", WORD),
		("e_csum",	WORD),
		("e_ip",	WORD),
		("e_cs",	WORD),
		("e_lfarlc",	WORD),
		("e_ovno",	WORD),
		("e_res",	WORD*4),
		("e_oemid",	WORD),
		("e_oeminfo",	WORD),
		("e_res2",	WORD*10),
		("e_lfanew",	LONG),
	]

kernel32.CreateProcessA.argtypes = (
    LPCSTR,               # lpApplicationName
    LPSTR,                # lpCommandLine
    c_void_p,             # lpProcessAttributes
    c_void_p,             # lpThreadAttributes
    BOOL,                 # bInheritHandles
    DWORD,                # dwCreationFlags
    LPVOID,               # lpEnvironment
    LPCSTR,               # lpCurrentDirectory
    ctypes.POINTER(STARTUPINFO),
    ctypes.POINTER(PROCESS_INFORMATION),
)
kernel32.CreateProcessA.restype = BOOL

kernel32.QueueUserAPC.argtypes = (
    c_void_p,             # pfnAPC
    HANDLE,               # hThread
    c_size_t,             # dwData (ULONG_PTR)
)
kernel32.QueueUserAPC.restype = DWORD


