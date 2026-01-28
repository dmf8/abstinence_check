# AUTO EDIT USAGE
自动编辑临时方案, 使用python脚本, 通过命令行参数指定消息内容, 自动完成文件编辑

用法如下: 

1. 执行脚本, 传入消息内容

    ```bash
    python3 test.py <message>[ -n/--name <user name>]
    ```

    1. message必选, 没有消息时使用空字符串`""`
    1. user name可选, 默认使用`git config user.name`, 也可以手动指定
    1. 脚本会自动判断日期和文件是否存在

1. `git commit`

1. `git pull`

1. `git push`