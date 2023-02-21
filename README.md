# Min

Min is a Minimization Manager for any X Window Manager supporting EWMH.
It offers a daemon written in Python, which can be used externally to minimize and recover windows.

## Motivation
Well, spectrwm does not support minimizing windows, and I often come across situations where I want don't want a window cluttering up my screen space in a tiling Window Manager. \ 
As a dirty hack rather than a solution, I ended up moving those applications (e.g. a terminal window running a server) to a workspace I am currently not using, but since X offers the minimization capability, this solution is far more elegant.

## Requirements
- rofi (exchangeable for dwm, see below)
- xdotool
- python package: daemon

### Using dwm instead of rofi
Run the following command before installing using `make install`:
```shell
sed -i 's/rofi -dmenu/dmenu/' min-recover
```

## Installation
```shell
make install
```
Also, make sure to start the daemon on startup, e.g. by adding `min` to your xinitrc.
Finally, make sure to look at the Usage section for correct use in your Window Manager.

## Uninstallation
```shell
make uninstall
```

## Usage

The tool offers shell-commands, which can be triggered from within any window manager.
The following command minimizes the currently focused window, which can e.g. be mapped to `MOD+W`.
```shell
min-minimize
```
With the following command, rofi is used to select a window which was minimized in the current workspace.
After selecting, the corresponding window will be recovered. This can be mapped to e.g. `MOD+Shift+W`.
```shell
min-recover
```
In order to visualize currently minimized windows in e.g. a menubar, the following command can be triggered periodically in the menubar:
```shell
min-list
```
A convenient integration into the spectrwm bar would look something like this, only taking up space when there are any minimized windows in the current workspace.
```shell
num_minimized=$(min-list | sed '/^$/D' | wc -l)
if [[ $num_minimized -gt 0 ]]; then
    echo "󰻀 $num_minimized"
fi
```
