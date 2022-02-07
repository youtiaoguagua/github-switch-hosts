# github自动刷新hosts

## mac设置

使用crontab自动刷新，`0 */1 * * * python3 /Users/youtiao/PycharmProjects/github-switch-hosts/main.py>>/Users/youtiao/PycharmProjects/github-switch-hosts/log.txt && killall -HUP mDNSResponder`
每小时自动刷新。

## win使用计划任务