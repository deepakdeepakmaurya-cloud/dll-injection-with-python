import ctypes
from ctypes import *
from ctypes.wintypes import *
from winStruct import *

kernel32 = windll.kernel32

snapshot = kernel32.CreateToolhelp32Snapshot(2, 0)

pe = PROCESSENTRY32()
pe.dwSize = sizeof(PROCESSENTRY32)

print(f"{'PID':<10}{'Process Name':<35}{'ParentPID':<15}{'Threads':<10}")
print("-" * 70)

if kernel32.Process32First(snapshot, byref(pe)):
	while True:
		process_name = pe.szExeFile.decode(errors="ignore")

		print(
            f"{pe.th32ProcessID:<10}"
            f"{process_name:<35}"
            f"{pe.th32ParentProcessID:<15}"
            f"{pe.cntThreads:<10}"
        )
		if kernel32.Process32Next(snapshot, byref(pe)) == False:
			break

kernel32.CloseHandle(snapshot)