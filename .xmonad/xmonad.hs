-- Data
import XMonad
import System.Exit (exitSuccess)
import XMonad.Actions.CopyWindow (kill1)

-- Hooks
import XMonad.Hooks.EwmhDesktops

-- Layouts
import qualified XMonad.StackSet as W

-- Utilities
import XMonad.Util.EZConfig (additionalKeysP)

myModMask = mod4Mask :: KeyMask

myTerminal = "alacritty" :: String

myBorderWidth = 1 :: Dimension

myNormColor = "#292d3e" :: String

myFocusColor = "#c792ea" :: String



myKeys :: [(String, X ())]
myKeys = 
    [
    ------------------ Window configs ------------------

    -- Move focus to the next window
    ("M-T", windows W.focusDown),
    -- Kill window
    ("M-S-q", kill1),
    -- Restart xmonad
    ("M-S-r", spawn "xmonad --restart"),
    -- Quit xmonad
    ("M-C-q", io exitSuccess),

    -------------------- App configs --------------------

    -- Menu
    ("M-d", spawn "dmenu_run"),
    -- Browser
    ("M-m", spawn "firefox"),
    -- File explorer
    ("M-n", spawn "thunar"),
    -- VSCode
    ("M-c", spawn "code"),
    -- Terminal
    ("M-<Return>", spawn myTerminal),
    -- Scrot
    ("M-s", spawn "scrot"),

    --------------------- Hardware ---------------------

    -- Volume
    ("<XF86AudioLowerVolume>", spawn "amixer set Master 5%-"),
    ("<XF86AudioRaiseVolume>", spawn "amixer set Master 5%+"),
    ("<XF86AudioMute>", spawn "amixer set master 0%" ),

    -- Brightness
    ("<XF86MonBrightnessUp>", spawn "brightnessctl set +10%"),
    ("<XF86MonBrightnessDown>", spawn "brightnessctl set 10%-")
    ]

main :: IO ()
main = do
    -- Xmonad
    xmonad $ ewmh def {
        modMask = myModMask,
        terminal = myTerminal,
        borderWidth = myBorderWidth,
        normalBorderColor = myNormColor,
        focusedBorderColor = myFocusColor
        }`additionalKeysP` myKeys
