#!/usr/bin/env python3
"""个人科研成长档案生成器 —— init_profile.py

基础任务：读取 learning_plan.json，自动生成 README.md 和 week01.md
提高任务：根据 JSON 自动创建 docs/src/data/outputs 四个目录
挑战任务：支持命令行参数 --name --interest --week-goal 自定义信息

用法:
  python init_profile.py                          # 基础模式
  python init_profile.py --name 李茹 --interest NLP --week-goal "学习Transformer"  # 挑战模式
"""

import os
import sys
import json
import argparse
from datetime import datetime


# =========================
# 配置
# =========================

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(PROJECT_DIR, "learning_plan.json")

# 默认四个核心目录及其用途说明
DEFAULT_FOLDERS = {
    "docs": "学习文档、笔记和日志（week01.md ~ week12.md）",
    "src": "项目源代码（Python脚本、实验代码）",
    "data": "数据集存放（原始数据、清洗后数据）",
    "outputs": "输出结果（模型预测结果、图表、报告）",
}


# =========================
# 核心功能
# =========================

def load_plan(json_path=JSON_PATH):
    """读取 learning_plan.json"""
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_directories(folders=None):
    """创建项目目录结构（提高任务）"""
    if folders is None:
        folders = DEFAULT_FOLDERS
    created = []
    for folder, purpose in folders.items():
        path = os.path.join(PROJECT_DIR, folder)
        os.makedirs(path, exist_ok=True)
        created.append((folder, purpose))
        print(f"  [OK] {folder}/ — {purpose}")
    return created


def generate_readme(plan, folders=None):
    """根据学习计划生成 README.md（基础任务）"""
    if folders is None:
        folders = DEFAULT_FOLDERS

    name = plan.get("name", "未命名")
    direction = plan.get("direction", "未指定")
    goal = plan.get("goal", "未设定")
    weeks = plan.get("weeks", [])

    # 目录表格
    folder_rows = ""
    for folder, purpose in folders.items():
        folder_rows += f"| `{folder}/` | {purpose} |\n"

    # 每周计划表格
    week_rows = ""
    for w in weeks:
        week_rows += f"| Week {w['week']} | {w['topic']} | {w['task']} |\n"

    content = f"""# {name} 的 AI 学习仓库

## 研究方向
> {direction}

## 12周学习目标
> {goal}

---

## 项目目录结构

| 目录 | 用途 |
|---|---|
{folder_rows}

---

## 学习计划总览

| 周次 | 主题 | 任务 |
|---|---|---|
{week_rows}

---

## 快速开始

```bash
# 初始化项目
python init_profile.py

# 挑战模式：自定义信息
python init_profile.py --name 你的名字 --interest 研究方向 --week-goal "本周目标"
```

---

*此 README 由 `init_profile.py` 自动生成于 {datetime.now().strftime("%Y-%m-%d %H:%M")}*
"""

    path = os.path.join(PROJECT_DIR, "README.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] README.md 已生成")


def generate_week01(plan):
    """生成第1周学习日志 week01.md（基础任务）"""
    weeks = plan.get("weeks", [])
    week1 = weeks[0] if weeks else {"topic": "科研记录与代码管理", "task": "学习 Git、Markdown、JSON、Python 文件读写"}

    name = plan.get("name", "未命名")
    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""# Week01 学习日志

> {name} | {today}

## 本周主题：{week1['topic']}

## 学习任务
{week1['task']}

---

## 本周完成情况

- [x] 安装 VSCode、Git 和基础 Python
- [x] 注册 GitHub / Gitee 账号
- [x] 创建个人 AI 学习仓库
- [x] 编写 `learning_plan.json` 学习计划
- [x] 编写 `init_profile.py` 自动化脚本
- [x] 自动生成 `README.md` 和 `week01.md`
- [x] 完成第一次代码提交

---

## 学习心得

本周初步掌握了科研项目的代码管理方式，学会了：

1. **Git 基础操作**：`git init`、`git add`、`git commit`、`git push`
2. **Markdown 写作**：标题、列表、表格、代码块
3. **JSON 数据格式**：结构化存储学习计划
4. **Python 文件读写**：用脚本自动生成文档
5. **项目目录规范**：docs / src / data / outputs 分工明确

后续12周的代码、笔记和实验结果都将托管在这个仓库中。

---

## 环境配置记录

| 工具 | 版本 | 状态 |
|---|---|---|
| VSCode | latest | ✅ 已安装 |
| Git | latest | ✅ 已安装 |
| Python | 3.11 | ✅ 已安装 |

---

*此日志由 `init_profile.py` 自动生成*
"""

    path = os.path.join(PROJECT_DIR, "week01.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] week01.md 已生成")


def generate_gitignore():
    """生成 .gitignore"""
    content = """# Python
__pycache__/
*.py[cod]
*.pyo
*.egg-info/
dist/
build/
venv/
.venv/

# IDE
.idea/
.vscode/
*.swp
*.swo

# 环境
.env
.env.local

# 数据（按需取消注释）
# data/
# outputs/
"""
    path = os.path.join(PROJECT_DIR, ".gitignore")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] .gitignore 已生成")


def run_basic(plan):
    """基础任务：生成 README.md 和 week01.md"""
    print("\n[基础任务] 生成 README.md 和 week01.md ...")
    generate_readme(plan)
    generate_week01(plan)


def run_advanced(plan):
    """提高任务：自动创建 docs/src/data/outputs 四个目录"""
    print("\n[提高任务] 创建项目目录结构 ...")
    return create_directories()


def run_challenge(args):
    """挑战任务：命令行小工具，支持输入姓名、研究兴趣和本周目标"""
    print("\n[挑战任务] 命令行模式 ...")
    plan = load_plan()

    if args.name:
        plan["name"] = args.name
        print(f"  姓名已更新: {args.name}")
    if args.interest:
        plan["direction"] = args.interest
        print(f"  研究方向已更新: {args.interest}")
    if args.week_goal:
        if plan.get("weeks") and len(plan["weeks"]) > 0:
            plan["weeks"][0]["task"] = args.week_goal
        print(f"  本周目标已更新: {args.week_goal}")

    # 保存更新后的 JSON
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=4)
    print(f"  [OK] learning_plan.json 已更新")

    return plan


# =========================
# 主入口
# =========================

def main():
    parser = argparse.ArgumentParser(
        description="个人科研成长档案生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python init_profile.py
  python init_profile.py --name 李四 --interest NLP
  python init_profile.py --name 王五 --interest "强化学习" --week-goal "学习Q-Learning算法"
        """,
    )
    parser.add_argument("--name", type=str, help="你的姓名")
    parser.add_argument("--interest", type=str, help="研究方向")
    parser.add_argument("--week-goal", type=str, help="本周学习目标")

    args = parser.parse_args()

    print("=" * 50)
    print("  个人科研成长档案生成器")
    print("=" * 50)

    # 加载学习计划
    plan = load_plan()
    print(f"\n当前用户: {plan.get('name', '未设置')}")
    print(f"研究方向: {plan.get('direction', '未设置')}")

    # 挑战模式：命令行参数更新
    if args.name or args.interest or args.week_goal:
        plan = run_challenge(args)

    # 提高任务：创建目录
    run_advanced(plan)

    # 基础任务：生成文档
    run_basic(plan)

    # 生成 .gitignore
    generate_gitignore()

    print("\n" + "=" * 50)
    print("  项目初始化全部完成！")
    print("=" * 50)
    print(f"""
生成的文件:
  ├── README.md          — 仓库主页文档
  ├── week01.md          — 第1周学习日志
  ├── learning_plan.json — 12周学习计划
  ├── init_profile.py    — 本脚本
  ├── .gitignore         — Git 忽略规则
  ├── docs/              — 学习文档目录
  ├── src/               — 源代码目录
  ├── data/              — 数据集目录
  └── outputs/           — 输出结果目录

下一步:
  git init
  git add .
  git commit -m "feat: 初始化个人AI学习仓库"
  git remote add origin <你的仓库地址>
  git push -u origin main
""")


if __name__ == "__main__":
    main()
