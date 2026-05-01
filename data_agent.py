from .base_agent import BaseAgent

class DataAgent(BaseAgent):
    def __init__(self):
        super().__init__(role_name="Data Reconnaissance Agent")

    def fetch_news(self, company_name):
        # 实际项目中，这里会调用爬虫模块、Twitter API、Google News API 等
        # 此处使用硬编码数据模拟全天候的信息监控
        simulated_news =[
            f"1. 彭博社：{company_name} 宣布推出下一代 AI 芯片架构，性能提升30倍。",
            f"2. 华尔街日报：多名华尔街分析师上调了 {company_name} 的目标股价。",
            f"3. 社交媒体舆情：开发者社区对 {company_name} 的 CUDA 新生态反响热烈。"
        ]
        return "\n".join(simulated_news)
