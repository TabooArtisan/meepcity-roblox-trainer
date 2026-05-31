#include "memory_utils.h"
#include <tlhelp32.h>
#include <psapi.h>

DWORD MemoryUtils::FindProcessId(const char* processName) {
    DWORD pid = 0;
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (hSnapshot != INVALID_HANDLE_VALUE) {
        PROCESSENTRY32 pe32;
        pe32.dwSize = sizeof(PROCESSENTRY32);
        if (Process32First(hSnapshot, &pe32)) {
            do {
                if (!_stricmp(pe32.szExeFile, processName)) {
                    pid = pe32.th32ProcessID;
                    break;
                }
            } while (Process32Next(hSnapshot, &pe32));
        }
        CloseHandle(hSnapshot);
    }
    return pid;
}

uintptr_t MemoryUtils::GetModuleBase(DWORD pid, const char* moduleName) {
    uintptr_t moduleBase = 0;
    HANDLE hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid);
    if (hSnapshot != INVALID_HANDLE_VALUE) {
        MODULEENTRY32 me32;
        me32.dwSize = sizeof(MODULEENTRY32);
        if (Module32First(hSnapshot, &me32)) {
            do {
                if (!_stricmp(me32.szModule, moduleName)) {
                    moduleBase = (uintptr_t)me32.modBaseAddr;
                    break;
                }
            } while (Module32Next(hSnapshot, &me32));
        }
        CloseHandle(hSnapshot);
    }
    return moduleBase;
}

uintptr_t MemoryUtils::ReadPointer(HANDLE hProcess, uintptr_t address) {
    uintptr_t value = 0;
    ReadProcessMemory(hProcess, (LPCVOID)address, &value, sizeof(value), nullptr);
    return value;
}

bool MemoryUtils::WriteMemory(HANDLE hProcess, uintptr_t address, const void* value, SIZE_T size) {
    return WriteProcessMemory(hProcess, (LPVOID)address, value, size, nullptr);
}