Drive="C:"

import os

import ctypes

 

 

 

class disable_file_system_redirection:

    _disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection

    _revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection

    def __enter__(self):

        self.old_value = ctypes.c_long()

        self.success = self._disable(ctypes.byref(self.old_value))

    def __exit__(self, type, value, traceback):

        if self.success:

            self._revert(self.old_value)

 

 

import subprocess

path = 'C:\\Windows\\System32\\manage-bde.exe -on '+Drive + ' -RecoveryPassword'

 

with disable_file_system_redirection():

    path=subprocess.Popen((path),shell=True,stdout=subprocess.PIPE);

result=path.communicate()[0]

 

print result

 

sysdown=subprocess.Popen(('shutdown /r '),shell=True,stdout=subprocess.PIPE);

for line in iter(sysdown.stdout.readline,''):

    print line.rstrip();