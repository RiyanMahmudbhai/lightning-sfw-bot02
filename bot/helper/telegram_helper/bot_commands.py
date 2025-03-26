from ...core.config_manager import Config


class BotCommands:
    StartCommand = "start2"
    LoginCommand = "login2"

    commands = {
        "Mirror": ["mirror2", "m2"],
        "QbMirror": ["qbmirror2", "qm2"],
        "JdMirror": ["jdmirror2", "jm2"],
        "Ytdl": ["ytdl2", "y2"],
        "NzbMirror": ["nzbmirror2", "nm2"],
        "Leech": ["leech2", "l2"],
        "QbLeech": ["qbleech2", "ql2"],
        "JdLeech": ["jdleech2", "jl2"],
        "YtdlLeech": ["ytdlleech2", "yl2"],
        "NzbLeech": ["nzbleech2", "nl2"],
        "Clone": ["clone2", "cl2"],
        "Count": "count2",
        "Delete": "del2",
        "List": "list2",
        "Search": "search2",
        "Users": "users2",
        "CancelTask": ["cancel2", "c2"],
        "CancelAll": ["cancelall2", "call2"],
        "ForceStart": ["forcestart2", "fs2"],
        "Status": ["status2", "s2"],
        "MediaInfo": ["mediainfo2", "mi2"],
        "SpeedTest": ["speedtest2", "stest2"],
        "Ping": "ping2",
        "Restart": ["restart2", "r2"],
        "RestartSessions": ["restartses2", "rses2"],
        "Broadcast": ["broadcast2", "bc2"],
        "Stats": ["stats2", "st2"],
        "Help": ["help2", "h2"],
        "Log": "log2",
        "Shell": "shell2",
        "AExec": "aexec2",
        "Exec": "exec2",
        "ClearLocals": "clearlocals2",
        "IMDB": "imdb2",
        "Rss": "rss2",
        "Authorize": ["authorize2", "a2"],
        "UnAuthorize": ["unauthorize2", "ua2"],
        "AddSudo": ["addsudo2", "as2"],
        "RmSudo": ["rmsudo2", "rs2"],
        "BotSet": ["bsetting2", "bs2"],
        "UserSet": ["usetting2", "us2"],
        "Select": ["select2", "sel2"],
    }

    for key, cmds in commands.items():
        vars()[f"{key}Command"] = (
            [f"{cmd}{Config.CMD_SUFFIX}" for cmd in cmds]
            if isinstance(cmds, list)
            else f"{cmds}{Config.CMD_SUFFIX}"
        )
