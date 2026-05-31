#pragma once
#include <windows.h>
#include <vector>

namespace MemoryUtils {
    DWORD FindProcessId(const char* processName);
    uintptr_t GetModuleBase(DWORD pid, const char* moduleName);
    uintptr_t ReadPointer(HANDLE hProcess, uintptr_t address);
    bool WriteMemory(HANDLE hProcess, uintptr_t address, const void* value, SIZE_T size);
}