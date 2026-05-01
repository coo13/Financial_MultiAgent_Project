import os
from dotenv import load_dotenv
from agents.data_agent import DataAgent
from agents.analysis_agent import AnalysisAgent
from agents.editor_agent import EditorAgent

# 加载环境变量
load_dotenv()

def main():
    print("="*50)
    print("🚀 启动[金融/商业分析多 Agent 矩阵系统]")
    print("="*50)

    # 初始化多 Agent 矩阵
    data_agent = DataAgent()
    analysis_agent = AnalysisAgent()
    editor_agent = EditorAgent()

    target_company = "NVIDIA (NVDA)"
    
    # 模拟外部输入的长文本财报 (RAG 的前置步骤)
    mock_pdf_text = """
    NVIDIA 2024财年第四季度财务报告：
    第四季度营收创纪录，达到221亿美元，较上一季度增长22%，较去年同期增长265%。
    全年营收创纪录，达到609亿美元，较上年增长126%。
    数据中心第四季度营收创纪录，达到184亿美元，较上一季度增长27%，较去年同期增长409%。
    毛利率达到了76.0%，显著提升。
    """

    #[Agent 1] 数据 Agent：获取实时新闻和舆情
    print(f"\n[1/3] 📡 数据 Agent 正在全网检索 {target_company} 的最新舆情...")
    news_context = data_agent.fetch_news(target_company)
    print(f"  -> 获取到 {len(news_context)} 条核心舆情数据。")

    # [Agent 2] 分析 Agent：进行长链推理和财报关键指标提取
    print(f"\n[2/3] 🧠 分析 Agent 正在深度解析财报与异常值对比...")
    financial_metrics = analysis_agent.extract_metrics(target_company, mock_pdf_text)
    print("  -> 财务指标解析完成。")

    # [Agent 3] 主编 Agent：将数据整合，按照 SOP 生成最终研报
    print(f"\n[3/3] ✍️ 主编 Agent 正在撰写深度投资研报...")
    final_report = editor_agent.generate_report(target_company, news_context, financial_metrics)
    
    print("\n" + "="*50)
    print(" 📑 最终生成的研报输出：")
    print("="*50 + "\n")
    print(final_report)

if __name__ == "__main__":
    main()
