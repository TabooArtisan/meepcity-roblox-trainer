#include "../src/memory_utils.h"
#include <cassert>

void TestFindProcessId() {
    DWORD pid = MemoryUtils::FindProcessId("explorer.exe");
    assert(pid != 0);
}

void TestGetModuleBase() {
    DWORD pid = MemoryUtils::FindProcessId("explorer.exe");
    if (pid) {
        uintptr_t base = MemoryUtils::GetModuleBase(pid, "explorer.exe");
        assert(base != 0);
    }
}

int main() {
    TestFindProcessId();
    TestGetModuleBase();
    return 0;
}