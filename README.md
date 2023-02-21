# Min

This is a minimization-manager for any X Window Manager without the capability of minimizing windows.
It offers a daemon written in python, which can be triggered to minimize and recover windows.

## Requirements
- rofi
## Installation
```
make install
```

## Uninstallation
```
make uninstall
```

## Usage

The tool offers shell-commands, which can be triggered from within any window manager.
The following command minimizes the currently focused window, which can e.g. be mapped to `MOD+w`.
```
min-minimize
```
With the following command, rofi is used to select a window which was minimized in the current workspace.
After selecting, the corresponding window will be recovered. This can be mapped to e.g. `MOD+Shift+w`.
```
min-recover
```
In order to count currently minimized windows in e.g. a menubar, the following command can be triggered periodically in the menubar:
```
min-list
```
A convenient integration into the spectrwm bar would look something like this, only taking up space when any windows are minimized.
```shell
num_minimized=$(min-list | sed '/^$/D' | wc -l)
if [[ $num_minimized != 0 ]]; then
    echo "󰻀 $num_minimized"
fi
```
