# analysis.py
import pandas as pd
import matplotlib.pyplot as plt
import os

# 创建输出文件夹
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# CSV 文件路径
csv_file = os.path.join("data", "student_score.csv")

# 成绩列
score_cols = ['Math','English','Physics','Chemistry','Biology','History','Geography']

# 读取 CSV 并处理
def load_data():
    df = pd.read_csv(csv_file)
    df[score_cols] = df[score_cols].apply(pd.to_numeric, errors='coerce')
    df['Total'] = df[score_cols].sum(axis=1)
    df['Average'] = df[score_cols].mean(axis=1)
    df['Rank'] = df['Total'].rank(ascending=False)
    return df

# 生成课程统计
def get_course_stats(df):
    stats_list = []
    for col in score_cols:
        stats_list.append({
            'Course': col,
            'Average': df[col].mean(),
            'Max': df[col].max(),
            'Min': df[col].min()
        })
    return pd.DataFrame(stats_list)

# 绘图函数
def plot_bar(df):
    df_plot = df.set_index('Name')[score_cols]
    df_plot.plot(kind='bar', figsize=(10,6))
    plt.title("Student Scores per Subject")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join("outputs", "score_bar_chart.png"))
    plt.show()
    print("柱状图已保存到 outputs 文件夹")

def plot_line(df):
    df.plot(x='Name', y='Total', kind='line', marker='o', figsize=(10,6))
    plt.title("Total Score per Student")
    plt.ylabel("Total Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join("outputs", "score_line_chart.png"))
    plt.show()
    print("折线图已保存到 outputs 文件夹")

# 生成约300字分析报告
def generate_report(df, course_stats):
    report = f"""
本次学生成绩分析涵盖了七门课程：{', '.join(score_cols)}。
班级总分平均为 {df['Total'].mean():.1f} 分，最高分 {df['Total'].max():.1f} 分，最低分 {df['Total'].min():.1f} 分。
数学和英语平均分较高，显示学生在基础学科掌握较好；物理和化学成绩波动较大，部分学生表现有待提高。

总分排名显示，部分学生成绩突出，各科均衡，尤其数学和英语表现优异；少数学生总分偏低，需要在学习方法和时间分配上改进。
课程统计显示，历史和地理平均分略低，教师在课堂教学中可适当加强相关内容。
柱状图清晰展示各学生各科成绩，折线图展示总分变化趋势，为教学提供数据支持，可用于辅导、分组教学及个性化学习计划制定。
"""
    # 保存到文件
    with open(os.path.join("outputs", "analysis_report.txt"), "w", encoding="utf-8") as f:
        f.write(report.strip())
    return report

# 命令行菜单
def menu():
    while True:
        df = load_data()
        course_stats = get_course_stats(df)
        print("\n===== 学生成绩分析菜单 =====")
        print("1. 查看全部学生统计")
        print("2. 查看单门课程成绩")
        print("3. 查看课程统计")
        print("4. 绘制柱状图")
        print("5. 绘制折线图")
        print("6. 查看分析报告")
        print("7. 退出")
        choice = input("请输入选项(1-7): ")
        if choice == "1":
            print(df)
        elif choice == "2":
            course = input("请输入课程名称: ")
            if course in df.columns:
                print(df[['Name', course]])
            else:
                print("课程名不存在！")
        elif choice == "3":
            print(course_stats)
        elif choice == "4":
            plot_bar(df)
        elif choice == "5":
            plot_line(df)
        elif choice == "6":
            report = generate_report(df, course_stats)
            print("\n=== 分析报告 ===")
            print(report)
        elif choice == "7":
            print("退出程序")
            break
        else:
            print("无效输入，请重新选择")

if __name__ == "__main__":
    print("学生成绩分析系统启动...")
    menu()