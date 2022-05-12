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
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import qtile

mod = "mod4"
terminal = guess_terminal()

@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser("~/.config/qtile/autostart.sh")
	subprocess.call([home])

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "z", lazy.window.toggle_fullscreen()),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod], "q", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # my shortcuts
    Key([mod], "s", lazy.spawn("snap run spotify")),
    Key([mod], "e", lazy.spawn("nautilus")),
    Key([mod], "b", lazy.spawn("blender")),
    Key([mod], "f", lazy.spawn("brave")),
    Key([mod], "v", lazy.spawn("midori")),
    Key([mod, "shift"], "x", lazy.spawn("systemctl poweroff")),
    Key([mod, "shift"], "z", lazy.spawn("systemctl reboot")),
    Key(["control"], "space",  lazy.spawn("rofi -show drun")),
    Key([mod], "u", lazy.spawn("~/Applications/UnityHub.AppImage")), 
    Key([mod, "shift"], "l", lazy.spawn("quicklinks")),
    Key([mod], "a", lazy.spawn("apps")),
    
    # Screenshot
    Key([],   "Print", lazy.spawn("flameshot gui")),

    # audio and brightness
    Key([mod, "shift"], "Right", lazy.spawn("amixer set Master 5%+ unmute")),
    Key([mod, "shift"], "Left", lazy.spawn("amixer set Master 5%- unmute")),
    Key([mod, "shift"], "Up", lazy.spawn("lux -a 5%")),
    Key([mod, "shift"], "Down", lazy.spawn("lux -s 5%")),

    # colorpicker
    Key([mod], 'x', lazy.spawn('xcolor-pick')),

    # Function keys
    Key([], "F3", lazy.spawn("systemctl suspend")),
    Key([], "F6", lazy.spawn("amixer set Master 5%- unmute")),
    Key([], "F7", lazy.spawn("amixer set Master 5%+ unmute")),
    Key([], "F9", lazy.spawn("lux -s 5%")),
    Key([], "F10", lazy.spawn("lux -a 5%")),
]

# Colors
colors = [["#23202A", "#23202A"], # panel background
          ["#44414B", "#44414B"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#101015", "#101015"], # border line color for current tab
          ["#CCFF00", "#CCFF00"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#121015", "#121015"], # color for the 'even widgets'
          ["#AEDA01", "#AEDA01"], # window name
          ["#ffffff", "#ffffff"]] # backbround for inactive screens

WHITE='#FFFFFF'

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
        border_focus = '0597F2',
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
    # 	fontsize = 10,
    # 	margin = 8,
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

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=2,
    background='000000aa',
)
extension_defaults = widget_defaults.copy()

# This is the bar, or the panel, and the widgets within the bar.
def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0],
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 14,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = '#ff4444',
                       inactive = colors[7],
                       rounded = True,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[4],
                       this_screen_border = colors[6],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0,
                       font = "Ubuntu Mono Bold",
                       fontsize = 14
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
             widget.Net(
                       interface = "wlo1",
                       format = '{down}↓↑{up}',
                       foreground = "#121015",
                       background = colors[4],
                       padding = 5,
                       font = "Ubuntu Mono Bold",
                       fontsize = 12,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('gnome-control-center wifi')},
                       ),
              widget.TextBox(
                       text = " ⟳",
                       padding = 2,
                       foreground = WHITE, 
                       background = colors[3],
                       font = "Ubuntu Mono Bold",
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       font = "Ubuntu Mono Bold",
                       display_format = "{updates}",
                       foreground = WHITE,
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e sudo pacman -Syu')},
                       background = colors[3],
                       ),
                widget.TextBox(
                         text = " 🖬",
                         foreground = "#121015",
                         background = colors[4],
                         padding = 0,
                       font = "Ubuntu Mono Bold",
                         fontsize = 14
                         ),
                widget.Memory(
                		   update_interval = 10,
                         foreground = "#121015",
                         background = colors[4],
                         mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('alacritty -e bpytop')},
                       font = "Ubuntu Mono Bold",
                         padding = 5
                         ),
              widget.TextBox(
                      text = " Vol:",
                       foreground = WHITE,
                       background = colors[3],
                       font = "Ubuntu Mono Bold",
                       padding = 0
                       ),
              widget.Volume(
                       foreground = WHITE,
                       background = colors[3],
                       font = "Ubuntu Mono Bold",
                       padding = 5
                       ),
              widget.CurrentLayout(
                       foreground = "#121015",
                       background = colors[4],
                       padding = 5,
                       font = "Ubuntu Mono Bold",
                       fontsize = 14
                       ),
              widget.Clock(
                       foreground = WHITE,
                       background = colors[3],
                       format = "%a, %b %_d (%I:%M) %p ",
                       font = "Ubuntu Mono Bold",
                       fontsize = 14
                       ),
              widget.Battery(
              	       foreground = "#121015",
                       background = colors[4],
                       format = '{char} {percent:2.0%} ',
                       font = "Ubuntu Mono Bold",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('gnome-control-center power')},
              	       ),
              ]
    return widgets_list

screens = [
    Screen(top=bar.Bar(widgets=init_widgets_list(), opacity=0.85, size=18)),
]

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
