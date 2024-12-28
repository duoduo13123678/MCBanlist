# MCBanlist  

一个用Python编写，在网页上查看的MC服务器玩家封禁列表  
**注意**:本项目大量使用了ai编写，我只是作了修改，可能会有很多bug，请指出  

**已测试过这些服务端 均可正常使用**  
1.Paper  
2.Vanila（原版）  
3.Leaves  
4.Spigot  

- ### 使用教程  
1.下载zip文件（Github的zip需要再把python.zip解压到python文件夹下，建议直接下载MCBanlist.zip或Release），解压到你服务器存放banned-players.json文件的目录（不要放进文件夹）
文件结构一般为下方所示  
MC服务器文件夹  
|__服务器文件  
|__banned-players.json  
|__从zip解压出来的文件(非文件夹）  
2.确定结构为上方所示后，双击server.py启动(需要Python环境并安装flask库)  
或者双击bat启动(无需安装任何东西，但要确定有Python文件夹)  
**请不要复制zip里的banned-players.json，不要用它替换原有的**  

- 对网页**内容，颜色，排版**不满意请到这些地方修改：  
中文HTML文件：templates/chinese.html
英语HTML文件: templates/english.html   
css文件：static/css/index.css  
图标文件：static/favicon.ico  

- 修改图标：  
1.准备一张图片  
2.转换成ico格式并改名成favicon.ico  
3.放进static文件夹里，替换掉原文件  
不想要图标直接删除这个叫favicon.ico的文件并编辑html就可以！  

- 修改设置：  
1.设置文件：settings.json，是个文本编辑器就能打开  
2.name后填写服务器名称，会显示在网页上  
3.ip后填写监听IP，可以是0.0.0.0  
4.port后填写端口  

- 添加语言：  
1.打开templates文件夹，从上面复制一个文件，改名成你喜欢的名字  
2.修改这个文件，把里面的注释，标签里的文字全部翻译成你想要的语言  
3.打开server.py，从上方复制，文件内已经说明了从哪里复制到哪里，粘贴到哪里  
4.把@app.route('/')里的“/”改成“/你想要的名字”（注意：改的是你复制的，不是原来的）  
5.把return render_template('chinese.html', data=extracted_data, config=server_name)中的“chinese.html”改成“你在步骤1里为html取的名字.html”  
6.在所有html里添加超链接，通向/你在步骤4里取的名字，类设置为lang_a，添加到哪里文件也说了  
7.在你复制的html文件内的p标签处加上 | 你的语言名，类设置为lang_p，哪个p标签也在文件内  
8.打开网页，看看效果  

- 其他提示：  
1.基于python，需要python环境  
2.有了python之后运行这个命令  
`pip install flask`  
来安装库，提示没有pip命令请单独安装pip  
3.完成以上步骤直接双击server.py打开（不行的试试命令行或者修改解释器）  
4.懒人直接用内置的脚本启动，已安装好了全部库（仅适用于Windows）  
