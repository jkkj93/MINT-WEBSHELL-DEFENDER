# MINT-WEBSHELL-DEFENDER
薄荷WEBSHELL防御系统，是一款WEBSHELL查杀/防御软件，采用PYTHON编写。不同于依靠特征库进行查杀的传统WEBSHELL扫描软件。本软件以防御为主，经过适当配置后可以100%防御，并清除任何WEBSHELL后门。
</br>
</br>
系统支持:</br>
1.支持WINDOWS与LINUX平台，需安装PYTHON 2.7。
</br>
</br>
使用方法:
</br>
1.先按照config_simple目录中的样例（包括WINDOWS与LINUX下的配置实例），对config目录中的配置文件进行配置。
</br>
config/scan_dir：配置要扫描的目录，支持一个路径。要扫描多个路径，需要配置并运行多个程序实例。
</br>
config/scan_extensions：配置要扫描的文件后缀名，每行配置一个后缀。
</br>
config/whitelist_dir：配置扫描白名单，每行配置一个路径，路径中的文件不会被扫描。
</br>
</br>
2.首次使用时，必须执行Mint.py -record命令进行WEB目录中文件的SHA1值记录，执行完成后才能进行后续扫描、查杀操作。最好在网站程序上传后立即进行，这样可以保证目录中不存在WEBSHELL。WEB程序被修改后也必须执行Mint.py -record命令进行SHA1值更新。
</br>
</br>
3.执行Mint.py -scan命令进行WEBSHELL扫描，扫描结果会在命令执行完成后显示，也会记录在log/log日志文件中，此命令仅显示可能的WEBSHELL，不会进行查杀。
</br>
</br>
4.执行Mint.py -kill命令进行WEBSHELL查杀，查杀结果会在命令执行完成后显示，也会记录在log/log日志文件中。（找到WEBSHELL后直接查杀，不会询问）。
</br>
</br>
5.执行Mint.py -status命令查询当前配置情况。
</br>
</br>
6.执行Mint.py -about命令查询当前程序版本。
</br>
</br>
7.直接执行Mint.py显示程序使用说明。
</br>
</br>
8.配置完成后可以将Mint.py -kill加入LINUX的CRONTAB，或WINDOWS的任务计划中，以进行定时查杀。
</br>
</br>
作者:jkkj93
