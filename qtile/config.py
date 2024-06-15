import os

from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import colors


mod = "mod4"
terminal = "kitty"
browser = "brave"


keys = [
    # apertura de aplicaciones
    Key([mod], "q", lazy.spawn(browser)),
    Key(
        [mod],
        "i",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    # volume control
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioMicMute", lazy.spawn("pactl set-source-mute 51 toggle")),
    # brightness control
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    # block button
    Key(
        [mod],
        "p",
        lazy.spawn("i3lock -i /home/gabsaws/Pictures/Wallpapers/mountain2.png"),
    ),
    # calculator
    Key([], "XF86Calculator", lazy.spawn("gnome-calculator")),
    # print screen
    Key(
        [],
        "Print",
        lazy.spawn(
            "scrot -s /home/gabsaws/Pictures/Screenshots/%y-%m-%d--%H-%M-%S.png"
        ),
    ),
    # monitor switch
    # Switch focus of monitors
    Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # abajo codigo para espawnear terminal con mismo directorio que la anterior
    # Key([mod, "control"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "r",
        lazy.spawn("dmenu_run"),
        desc="Spawn a command using a prompt widget",
    ),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


widget_defaults = dict(
    font="FreeSans",
    fontsize=15,
    padding=3,
)

extension_defaults = widget_defaults.copy()

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


# configuraciones generales para los layouts----------------------------------

# colors = colors.Dracula
# colors = colors.DoomOne
# colors = colors.GruvboxDark
# colors = colors.MonokaiPro
# colors = colors.Nord
# colors = colors.OceanicNext
colors = colors.Palenight
# colors = colors.SolarizedDark
# colors = colors.SolarizedLight
# colors = colors.TomorrowNight

layout_theme = {
    "border_width": 3,
    "margin": 8,
    "border_focus": colors[8],
    "border_normal": colors[0],
}
layouts = [
    layout.Tile(**layout_theme),
    layout.MonadTall(
        **layout_theme,
    ),
    layout.MonadWide(**layout_theme),
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=4,
        margin=3,
        border_radius=30,
    ),
    layout.Max(),
]


##MOUSE CALLBACKS
def open_pacman(qtile):
    qtile.spawn("kitty -e sudo pacman -Syu")


def open_bt(qtile):
    qtile.spawn("blueman-manager")


def open_wifi(qtile):
    qtile.spawn("io.elementary.switchboard settings://network")


reg_length = 5
long_length = 14


screens = [
    Screen(
        top=bar.Bar(
            [
                # PARTE IZQUIERDA
                widget.Spacer(length=long_length),
                widget.CurrentLayoutIcon(),
                widget.CurrentLayout(
                    width=80,
                ),
                widget.GroupBox(),
                widget.Spacer(length=reg_length),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # PARTE DERECHA
                widget.KeyboardLayout(
                    configured_keyboards=["us", "latam"],
                    display_map={"us": " US", "latam": " ES"},
                    option="grp:alt_shift_toggle",
                    fmt="{} ",
                    foreground=colors[7],
                ),
                widget.Spacer(length=reg_length),
                widget.Wlan(
                    interface="wlp1s0",
                    ethernet_message=" ",
                    disconnected_message=" ",
                    format="  ",
                    use_ethernet=True,
                    foreground=colors[7],
                    mouse_callbacks={"Button1": lazy.function(open_wifi)},
                ),
                widget.Spacer(length=reg_length),
                widget.Bluetooth(
                    adapter_paths=["/org/bluez/hci0"],
                    default_text=" {connected_devices}",
                    foreground=colors[7],
                    mouse_callbacks={"Button1": lazy.function(open_bt)},
                ),
                widget.Spacer(length=reg_length),
                widget.Battery(
                    update_interval=1,
                    full_char=" ",
                    charge_char=" ",
                    discharge_char="  ",
                    not_charging_char="   ",
                    format="{char}{percent:2.0%} ",
                    foreground=colors[8],
                    low_foreground=colors[5],
                    low_percentage=0.20,
                ),
                widget.PulseVolume(
                    fmt="   {}",
                    foreground=colors[8],
                ),
                widget.Spacer(length=reg_length),
                widget.CheckUpdates(
                    distro="Arch",
                    no_update_string="  ",
                    colour_have_updates=colors[3],
                    colour_no_updates=colors[6],
                    display_format="   {updates}",
                    update_interval=10,
                    mouse_callbacks={"Button1": lazy.function(open_pacman)},
                ),
                widget.Spacer(length=reg_length),
                widget.Clock(
                    foreground=colors[8],
                    format="%a, %b %d     %H:%M",
                ),
                widget.Spacer(length=long_length),
                widget.QuickExit(
                    default_text=" ",
                    countdown_format="{} s",
                    foreground=colors[5],
                    fmt="  {}",
                ),
                widget.Spacer(length=long_length),
            ],
            20,
            border_width=[10, 2, 10, 2],  # Draw top and bottom borders
            margin=[12, 5, 5, 5],
        ),
        # You can uncomment this variable if you see that on X12 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 61 to indicate that you limit it to 60 events per second
        # x12_drag_polling_rate = 60,
        # left=bar.Bar(),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="gnome-calculator"),
        Match(title="Calculator"),
    ]
)
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


# initial run programs
autostart = [
    "nitrogen --restore &",
    # "picom --daemon &",
    "picom --backend glx -b",
]

for x in autostart:
    os.system(x)

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
