#include <windows.h>
#include <iostream>
#include "memory_utils.h"
#include "roblox_offsets.h"

int main() {
    DWORD pid = MemoryUtils::FindProcessId("RobloxPlayerBeta.exe");
    if (!pid) {
        std::cerr << "Roblox process not found!" << std::endl;
        return 1;
    }

    HANDLE hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
    if (!hProcess) {
        std::cerr << "Failed to open process!" << std::endl;
        return 1;
    }

    uintptr_t moduleBase = MemoryUtils::GetModuleBase(pid, "RobloxPlayerBeta.exe");
    if (!moduleBase) {
        std::cerr << "Failed to get module base!" << std::endl;
        CloseHandle(hProcess);
        return 1;
    }

    uintptr_t localPlayer = MemoryUtils::ReadPointer(hProcess, moduleBase + Offsets::LocalPlayer);
    if (!localPlayer) {
        std::cerr << "Failed to find local player!" << std::endl;
        CloseHandle(hProcess);
        return 1;
    }

    std::cout << "MeepCity Trainer initialized!" << std::endl;
    std::cout << "Local Player Address: 0x" << std::hex << localPlayer << std::endl;

    CloseHandle(hProcess);
    return 0;
}