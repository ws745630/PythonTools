# CreateApp-Message-Icon
创建iOS AppIcon和Message Icon脚本    
###使用方法：  
进入`createAppIcon.py`同级目录,在终端执行`python createAppIcon.py`  

该脚本有3种创建方式：

- 1.创建AppIcon
- 2.创建iMessageIcon
- 3.同时创建AppIcon和iMessageIcon

然后会提示输入项目路径,把项目路径输入里面就会自动生成所需要的icon

###注意事项
1.创建**AppIcon**和**iMessageIcon**,需要传入项目的目录,这里一定是`Assets.xcassets`所在的上级目录,比如`/Users/mac/Desktop/FlipCard/FlipCard`;同理iMessage也是如此  
2.选择**同时创建AppIcon和iMessageIcon**时，需传入的的项目所在的路径,比如上面的项目根路径 `/Users/mac/Desktop/FlipCard`;内部的项目命令需要遵循一定的规则,例如项目的工程名字叫`FlipCard ``iMessage`应该命令为`FlipCardMessage`  
3.如果需要修改命名规则需修改`iMessageName`为项目Message文件夹的名称,比如上面的Message文件夹叫`FlipCardMessage`就把名称改过去

