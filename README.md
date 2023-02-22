# Min

Min is a Minimization Manager for any X Window Manager supporting EWMH.
It offers a daemon written in Python, which can be used externally to minimize and recover windows.

## Motivation
Some Window Managers do not support minimizing windows, and I often come across situations where I don't want a window to clutter up my screen space in the tiling Window Manager. \
As a dirty hack rather than a solution, I ended up moving those applications (e.g. a terminal window running a server) to a workspace I am currently not using, but since X offers the minimization capability, Min elegantly adds this feature in a Window Manager agnostic way.

## Requirements
If some of the requirements are not met, you are notified upon installing Min.

- rofi or dwm (rofi is preferred for visualization reasons)
- xdotool

### Using dwm or rofi?
When installing Min, the two programs are automatically detected.
By default, Min uses rofi.
This is due to the titles of the windows can get quite lengthy and are more suitably visualized in rofi.

## Installation
```shell
sudo make install
```
Also, make sure to start the daemon on startup, e.g. by adding `min &` to your xinitrc.
The `&` is important in this case! \
Finally, make sure to look at the Usage section for correct usage in your Window Manager.

## Uninstallation
```shell
sudo make uninstall
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
A convenient integration into a menubar would look something like this, only taking up space when there are any minimized windows in the current workspace.
```shell
num_minimized=$(min-list | sed '/^$/D' | wc -l)
if [[ $num_minimized -gt 0 ]]; then
    echo " $num_minimized"
fi
```
