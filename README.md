## NekoFishy
### What does it do?
It is a proxy, which opens a socket listening for NekoAtsume HTTP-Requests (such as the news tab or the password feature) and modifies the password responds by a given user input.
The password feature is meant to be an addition to the general gameplay, that gives you a small amount of silver fish and sometimes gold fish for entering a daily password.
NekoFishy interrupts these requests and modifies them to add or deduct a custom amount of ingame resources.
### Why does this exist?
As game progress is non-transferable (except for manually extracting the save game and injecting it, which requires root access) losing or simply changing your smartphone means losing all of your progress. Obviously providing yourself with unlimited resources destroys every aspect of the game, so I do not advise to use this tool for the purpose of destroying your experience.
This tool can not recover your cat visits, but your overall wealth in the game without the user having root access. The game features ingame-purchases for the exact same function, which in my defense are probably used by few. If you want to support the developer of the game, please continue purchasing through ingame-payments. If you simply lost your progress and don't want to start it all over, use this little tool.
### Requirements
Latest **Python 2** runtimes and a device with access to its' proxy settings.
### Usage
Start the script with your Python 2 interpreter. This will create a connection listening on port 12345. If this port is in use, you can start the script with the first command line parameter being your desired port. On Windows you may encounter a Firewall Access Request, which I think is needed for creating a listening socket.
Once launched, the tool is pretty straight forward. Connect to the proxy address and port specified in the terminal. Any traffic that is not related to NekoAtsume will be blocked, so you may get a warning, that your Network Configuration is wrongly configured. Ignore it for now. If you are very paranoid running a unknown proxy (which you should be), disconnect your router from your ISP for the process.
When in-game, open the news tab. The daily password, which the game provides you should be _Connected_. If so, you are good to go and should be seeing a new line in the application console. In NekoAtsume head over to _Connect_ -> _Daily Password_ and Enter any daily password you like. The game will be stuck on _Sending_, while the command line interface requests you to enter a silver and gold fish amount. These should be any signed integer. Once you typed in your values and hit enter, the proxy will send you your fish. You can then close the application and change your proxy settings to your default.
#### End Notes
Please use this tool responsively and only for restoring your progress. Thank you.