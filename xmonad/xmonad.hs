import XMonad
import Data.Monoid
import System.Exit

import qualified XMonad.StackSet as W
import qualified Data.Map        as M

--aditional import 
import XMonad.Util.SpawnOnce
import XMonad.Util.Run
import XMonad.Hooks.ManageDocks
import XMonad.Layout.Spacing
import XMonad.Layout.NoBorders

--to config xmobar
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.StatusBar
import XMonad.Hooks.StatusBar.PP
import XMonad.Hooks.EwmhDesktops


myTerminal      = "kitty"
myBrowser       = "brave-browser"

-- Whether focus follows the mouse pointer.
myFocusFollowsMouse :: Bool
myFocusFollowsMouse = True

-- Whether clicking on a window to focus also passes the click to the window
myClickJustFocuses :: Bool
myClickJustFocuses = False

myBorderWidth   = 3
myModMask       = mod4Mask

myWorkspaces    = ["1","2","3","4","5"]
myNormalBorderColor  = "#191A25"
myFocusedBorderColor = "#ffff00"

audioMute       = (0, 0x1008ff12)
raiseVolume     = (0, 0x1008ff13)
lowerVolume     = (0, 0x1008ff11)
muteMic         = (0, 0x1008ffb2) 
brightnessDown  = (0, 0x1008ff03)
brightnessUp    = (0, 0x1008ff02)
calculator      = (0, 0x1008ff1d)

printScreen     = 0xff61

myKeys conf@(XConfig {XMonad.modMask = modm}) = M.fromList $

    [(audioMute,                           spawn "amixer set Master toggle" )
    ,(lowerVolume,                         spawn "amixer set Master 5%- unmute" )
    ,(raiseVolume,                         spawn "amixer set Master 5%+ unmute" )
    ,(muteMic,                             spawn "amixer set Capture toggle")
    ,(brightnessDown,                      spawn "brightnessctl s 5%-")
    ,(brightnessUp,                        spawn "brightnessctl s +5%")
    ,(calculator,                          spawn "gnome-calculator")
    --Print whole screen
    ,((0, printScreen),                    spawn "scrot $HOME/Pictures/Screenshots/%y-%m-%d--%H-%M-%S.png; scrot -e") 
    --Print selection
    ,((modm , printScreen),                spawn "scrot -s $HOME/Pictures/Screenshots/%y-%m-%d--%H-%M-%S.png -e 'xclip -selection clipboard -t image/png -i $f'")
    --Print focused window
    ,((modm .|. shiftMask, printScreen),   spawn "scrot -u $HOME/Pictures/Screenshots/%y-%m-%d--%H-%M-%S.png -e 'xclip -selection clipboard -t image/png -i $f'")
    ]
    ++
    [
      ((modm,               xK_Return), spawn $ XMonad.terminal conf)
    , ((modm,               xK_r     ), spawn "dmenu_run")
    , ((modm,               xK_w     ), kill)
    , ((modm,               xK_Tab ), sendMessage NextLayout)
    , ((modm .|. shiftMask, xK_space ), setLayout $ XMonad.layoutHook conf)
    , ((modm,               xK_n     ), refresh)
    , ((modm,               xK_space   ), windows W.focusDown)
    , ((modm,               xK_j     ), windows W.focusDown)
    , ((modm,               xK_k     ), windows W.focusUp  )
    , ((modm,               xK_m     ), windows W.focusMaster  )
    , ((modm .|. shiftMask, xK_j     ), windows W.swapDown  )
    , ((modm .|. shiftMask, xK_k     ), windows W.swapUp    )
    , ((modm,               xK_h     ), sendMessage Shrink)
    , ((modm,               xK_l     ), sendMessage Expand)
    -- Push window back into tiling
    , ((modm,               xK_t     ), withFocused $ windows . W.sink)
    , ((modm,               xK_q     ), spawn (myBrowser))
--    , ((modm .|. shiftMask, xK_q     ), io (exitWith ExitSuccess))
    , ((modm .|. shiftMask, xK_q     ), sequence_ [ spawn "mpv --no-video Templates/starting_sounds/sutdown-1.mp3", io (exitWith ExitSuccess)])
    , ((modm .|. shiftMask, xK_r     ), spawn "xmonad --recompile; xmonad --restart")
    , ((modm,               xK_i     ), spawn "setxkbmap -layout latam")
    , ((modm,               xK_u     ), spawn "setxkbmap -layout us")
    ]
    ++
    -- mod-[1..9], Switch to workspace N
    -- mod-shift-[1..9], Move client to workspace N
    --
    [((m .|. modm, k), windows $ f i)
        | (i, k) <- zip (XMonad.workspaces conf) [xK_1 .. xK_5]
        , (f, m) <- [(W.greedyView, 0), (W.shift, shiftMask)]]
    ++
    -- mod-{w,e,r}, Switch to physical/Xinerama screens 1, 2, or 3
    -- mod-shift-{w,e,r}, Move client to screen 1, 2, or 3
    [((m .|. modm, key), screenWorkspace sc >>= flip whenJust (windows . f))
        | (key, sc) <- zip [ xK_comma, xK_period] [0..]
        , (f, m) <- [(W.view, 0), (W.shift, shiftMask)]]
 
myMouseBindings (XConfig {XMonad.modMask = modm}) = M.fromList $
    [ ((modm, button1), (\w -> focus w >> mouseMoveWindow w
                                       >> windows W.shiftMaster))
    , ((modm, button2), (\w -> focus w >> windows W.shiftMaster))
    , ((modm, button3), (\w -> focus w >> mouseResizeWindow w
                                       >> windows W.shiftMaster))
    ]
--

myLayout = smartBorders(avoidStruts(tiled)  ||| avoidStruts(Mirror tiled) ||| noBorders Full)
  where
     tiled   = Tall nmaster delta ratio
     nmaster = 1
     ratio   = 6/10
     delta   = 3/100

myManageHook = composeAll
    [ className =? "MPlayer"        --> doFloat
    , className =? "Gimp"           --> doFloat
    , className =? "gnome-calculator"           --> doFloat
    , resource  =? "desktop_window" --> doIgnore
    , resource  =? "kdesktop"       --> doIgnore ]

myEventHook = mempty

myLogHook = return ()
--
myStartupHook = do
  spawnOnce "picom"
  spawnOnce "nitrogen --restore"
  spawnOnce "xinput set-prop 12 'libinput Tapping Enabled' 1"
  spawn "mpv --no-video Templates/starting_sounds/sutdown-1.mp3"

main = do 
  xmproc <- spawnPipe "xmobar -x 0 $HOME/.config/xmobar/xmobarrc"
  xmonad $ docks defaults

defaults = def {
      -- simple stuff
        terminal           = myTerminal,
        focusFollowsMouse  = myFocusFollowsMouse,
        clickJustFocuses   = myClickJustFocuses,
        borderWidth        = myBorderWidth,
        modMask            = myModMask,
        workspaces         = myWorkspaces,
        normalBorderColor  = myNormalBorderColor,
        focusedBorderColor = myFocusedBorderColor,

      -- key bindings
        keys               = myKeys,
        mouseBindings      = myMouseBindings,

      -- hooks, layouts
        layoutHook         = spacingRaw True (Border 0 10 10 10) True (Border 10 10 10 10) True $ myLayout,
        manageHook         = myManageHook,
        handleEventHook    = myEventHook,
        startupHook        = myStartupHook,
        logHook            = myLogHook
    }
