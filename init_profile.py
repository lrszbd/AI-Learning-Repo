
import os
import json
from datetime import datetime

# ==========================================
# 自动创建项目目录
# ==========================================

folders = ["docs", "src", "data", "outputs"]

for folder in folders:

    if not os.path.exists(folder):

        os.makedirs(folder)

# ==========================================
# 检查 JSON 配置文件
# ==========================================

json_file = "learning_plan.json"

# 如果不存在则自动创建默认 JSON
if not os.path.exists(json_file):

    default_data = {
        "name": "李茹",
        "12_week_goal": "完成 AI 学习与项目实践",
        "weekly_tasks": [
            "Week01 Git 与 GitHub",
            "Week02 Python 数据分析",
        ]
    }

    with open(json_file, "w", encoding="utf-8") as f:

        json.dump(default_data, f, ensure_ascii=False, indent=4)

# ==========================================
# 读取 JSON 数据
# ==========================================

with open(json_file, "r", encoding="utf-8") as f:

    data = json.load(f)

# JSON 默认信息
default_name = data.get("name", "未知")

default_interest = data.get("research_interest", "AI")

goal_12week = data.get("12_week_goal", "")

weekly_tasks = data.get("weekly_tasks", [])

# ==========================================
# 命令行输入（挑战任务）
# ==========================================

print("====================================")
print("      AI 学习日志自动生成工具")
print("====================================")

week = input("请输入周次（例如 1 或 2）：")

name = input(f"请输入姓名（默认：{default_name}）：").strip()

interest = input(f"请输入研究兴趣（默认：{default_interest}）：").strip()

goal = input("请输入本周学习目标：").strip()

summary = input("请输入本周学习总结：").strip()

# 如果直接回车，则使用 JSON 默认值
if name == "":
    name = default_name

if interest == "":
    interest = default_interest

# ==========================================
# 自动生成日期
# ==========================================

today = datetime.now().strftime("%Y-%m-%d")

# ==========================================
# weekXX 格式
# ==========================================

week_str = f"week{int(week):02d}"

# ==========================================
# 自动生成 README.md
# ==========================================

readme_content = f"""
# AI Learning Repo

## 学生信息

- 姓名：{name}
- 研究兴趣：{interest}

---

## 12周总目标

{goal_12week}

---

## 当前学习周次

{week_str}

---

## 项目目录结构

docs/      学习日志与文档

src/       Python源代码

data/      数据集

outputs/   输出结果

---

## 每周学习任务

"""

# 添加 weekly_tasks
for task in weekly_tasks:

    readme_content += f"- {task}\n"

readme_content += f"""

---

## 本周学习目标

{goal}

---

## 项目简介

这是一个持续维护的 AI 学习仓库，
用于记录 Python、数据分析、机器学习、
深度学习与计算机视觉相关学习过程。

后续将持续更新：

- 学习日志
- Python 项目
- 数据分析实验
- AI 模型训练代码
- 实验结果与报告

---

GitHub 仓库持续更新中
"""

# 写入 README.md
with open("README.md", "w", encoding="utf-8") as f:

    f.write(readme_content.strip())

# ==========================================
# 自动生成 weekXX.md
# ==========================================

log_file = os.path.join("docs", f"{week_str}.md")

log_content = f"""
# {week_str.capitalize()} 学习日志

> {name} | {today}

---

## 研究兴趣

{interest}

---

## 本周学习目标

{goal}

---

## 本周完成内容

- 完成本周 AI 学习任务
- 学习 Python 编程
- 学习 Git 与 GitHub 项目管理
- 学习 Markdown 文档编写
- 持续维护 AI 学习仓库

---

## 项目目录结构

AI-Learning-Repo/

docs/        学习日志与文档

src/         Python源代码

data/        数据集

outputs/     输出结果

---

## 本周学习总结

{summary}

---

## 下一步计划

- 继续完善 AI 学习仓库
- 学习新的 Python 数据分析与 AI 技术
- 持续更新 GitHub 项目内容

---

日志由 init_profile.py 自动生成
"""

# 写入 weekXX.md
with open(log_file, "w", encoding="utf-8") as f:

    f.write(log_content.strip())

# ==========================================
# 输出结果
# ==========================================

print("\n====================================")
print("AI 学习日志自动生成成功")
print("====================================")

print(f"生成日志文件：{log_file}")

print("README.md 已自动更新")

print("\n已自动检查并创建目录：")

for folder in folders:

    print(f"- {folder}/")

print("\n当前 JSON 配置内容：")

print(f"姓名：{default_name}")

print(f"研究兴趣：{default_interest}")

print(f"12周目标：{goal_12week}")



print("====================================")