# Min

Min is a Minimization Manager for any X Window Manager without the capability of minimizing windows.
It offers a daemon written in Python, which can be triggered to minimize and recover windows.

## Requirements
- rofi
- xdotool
- python package: daemon

## Installation
```
make install
```
Also, make sure to start the daemon on startup, e.g. by adding `min` to your xinitrc.
Finally, make sure to look at the Usage section for correct use in your Window Manager.

## Uninstallation
```
make uninstall
```

## Usage

The tool offers shell-commands, which can be triggered from within any window manager.
The following command minimizes the currently focused window, which can e.g. be mapped to `MOD+W`.
```
min-minimize
```
With the following command, rofi is used to select a window which was minimized in the current workspace.
After selecting, the corresponding window will be recovered. This can be mapped to e.g. `MOD+Shift+W`.
```
min-recover
```
In order to visualize currently minimized windows in e.g. a menubar, the following command can be triggered periodically in the menubar:
```
min-list
```
A convenient integration into the spectrwm bar would look something like this, only taking up space when there are any minimized windows in the current workspace.
```shell
num_minimized=$(min-list | sed '/^$/D' | wc -l)
if [[ $num_minimized != 0 ]]; then
    echo "󰻀 $num_minimized"
fi
```
