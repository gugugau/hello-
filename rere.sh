#!/bin/bash
echo "====== 系统检查 ======"
echo "当前用户：$(whoami)"
echo "当前时间：$(date)"
echo "磁盘空间："
df -h /data
echo "====== 检查完毕 ======"
