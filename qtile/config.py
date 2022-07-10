# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
import os, subprocess
from libqtile import hook

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, EzKey as EK
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

mod = "mod4"
browser = "brave"
file_manager = "nautilus"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser("~/.config/qtile/autostart.sh")
	subprocess.call([home])

keys = [
    # Switch between windows
    EK("M-h", lazy.layout.left(), desc="Move focus to left"),
    EK("M-l", lazy.layout.right(), desc="Move focus to right"),
    EK("M-j", lazy.layout.down(), desc="Move focus down"),
    EK("M-k", lazy.layout.up(), desc="Move focus up"),
    EK("M-<Tab>", lazy.layout.next(), desc="Move window focus to other window"),
    EK("M-z", lazy.window.toggle_fullscreen()),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    EK("M-S-h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    EK("M-S-l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    EK("M-S-j", lazy.layout.shuffle_down(), desc="Move window down"),
    EK("M-S-k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    EK("M-C-h", lazy.layout.grow_left(), desc="Grow window to the left"),
    EK("M-C-l", lazy.layout.grow_right(), desc="Grow window to the right"),
    EK("M-C-j", lazy.layout.grow_down(), desc="Grow window down"),
    EK("M-C-k", lazy.layout.grow_up(), desc="Grow window up"),
    EK("M-n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    EK("M-S-<Return>", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    EK("M-<Return>", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    EK("M-<space>", lazy.next_layout(), desc="Toggle between layouts"),
    EK("M-q", lazy.window.kill(), desc="Kill focused window"),

    EK("M-<F5>", lazy.restart(), desc="Restart Qtile"),
    EK("M-S-q", lazy.shutdown(), desc="Shutdown Qtile"),
    EK("M-r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # my shortcuts
    EK("M-s", lazy.spawn("spotify")),
    EK("M-b", lazy.spawn("blender")),
    EK("M-e", lazy.spawn(file_manager)),
    EK("M-f", lazy.spawn(browser)),

    # powershortcuts
    EK("M-S-x", lazy.spawn("systemctl poweroff")),
    EK("M-S-z", lazy.spawn("systemctl reboot")),

    # rofi launcher
    EK("C-<space>",  lazy.spawn("rofi -show drun")),
    EK("M-S-p",  lazy.spawn("rofi-pass --last-used")),
    
    # Screenshot
    EK("<Print>", lazy.spawn("flameshot full")),
    EK("S-<Print>", lazy.spawn("flameshot gui")),

    # audio and brightness
    EK("M-S-<Right>", lazy.spawn("amixer set Master 5%+ unmute")),
    EK("M-S-<Left>", lazy.spawn("amixer set Master 5%- unmute")),
    EK("M-S-<Up>", lazy.spawn("lux -a 5%")),
    EK("M-S-<Down>", lazy.spawn("lux -s 5%")),

    # colorpicker
    EK("M-x", lazy.spawn('xcolor-pick')),

    # Function keys
    EK("<F3>", lazy.spawn("systemctl suspend")),
    EK("<F6>", lazy.spawn("amixer set Master 5%- unmute")),
    EK("<F7>", lazy.spawn("amixer set Master 5%+ unmute")),
    EK("<F9>", lazy.spawn("lux -s 5%")),
    EK("<F10>", lazy.spawn("lux -a 5%")),
]


groups = [Group(i) for i in [
    "", "", "", "", "", "",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

layouts = [
    #layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    # layout.Max(),
    layout.MonadTall(
        fontsize = 10,
        margin = 2,
        name = 'Xmonad Tall',
        border_focus = 'C74045',
    ),
    layout.TreeTab(
        active_bg = 'b00000',
        vspace = 5,
        fontsize = 14,
        name = 'TreeTab',
        sections = ['FIRST'],
        panel_width = 150,
        place_right = True,
        bg_color = '000000aa',
        font = 'alsina',
        padding_left = 0,
    ),
    # layout.MonadWide(
    #   fontsize = 10,
    #   margin = 8,
    #     name = 'Xmonad Wide'
    # ),
    layout.Bsp(
        name = 'Grid',
        border_focus = '0597F2',
    ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Floating(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

screens = []

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "mutter"
