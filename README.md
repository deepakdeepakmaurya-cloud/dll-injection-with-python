# DLL Injection using Python ctypes

This project demonstrates a basic DLL injection technique using Python `ctypes` and native Windows APIs.
The injector allocates memory inside a remote process, writes the DLL path into that process, and creates a remote thread to load the DLL using `LoadLibraryA`.

**APIs Used**

- `OpenProcess`
- `VirtualAllocEx`
- `WriteProcessMemory`
- `GetModuleHandleA`
- `GetProcAddress`
- `CreateRemoteThread`

**Files**

| File | Description |
|---|---|
| `Process_Enum.py` | Enumerate Processes |
| `dll_injector.py` | Python DLL injector |
| `mal.dll` | Simple DLL showing MessageBox |
| `mal.cpp` | Source code for mal.dll |
| `winStruct.py` | Needed Structure |

**Example Usage**

Identify the traget process and its PID.

<img width="927" height="161" alt="image" src="https://github.com/user-attachments/assets/8034cbba-a10e-436d-b485-4c84a96e4bbb" />

**Run dll_injector.py**

<img width="540" height="207" alt="image" src="https://github.com/user-attachments/assets/e1ae94d3-f178-4259-ad8f-8dc97df3151b" />

**On Success**

<img width="594" height="387" alt="image" src="https://github.com/user-attachments/assets/4693eb99-48d7-4f15-bf9c-3a3dfdd9cfcb" />

Enjoy injection!:)

