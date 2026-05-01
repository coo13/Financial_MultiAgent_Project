from .base_agent import BaseAgent

class EditorAgent(BaseAgent):
    def __init__(self):
        super().__init__(role_name="Chief Editor Agent")

    def generate_report(self, company_name, news_context, financial_metrics):
        system_prompt = """
        你是一位顶级金融研报主笔。你需要根据数据分析师提取的财务数据和实时新闻舆情，撰写一份结构化的投资研报摘要。
        要求：
        1. 包含标题、核心观点、财务分析、市场舆情四个部分。
        2. 语气专业、客观，支持 markdown 格式。
        """
        
        user_prompt = f"""
        公司：{company_name}
        【财务指标数据】：
        {financial_metrics}
        
        【实时舆情数据】：
        {news_context}
        """
        
        mock_res = f"""# 深度投资研报：{company_name} 业绩爆发与市场展望

## 1. 核心观点 (Core Thesis)
{company_name} 最新季度财报远超市场预期，核心驱动力来自于 AI 基础设施建设的强劲需求。结合近期新一代架构的发布，公司在行业内的垄断护城河正在进一步加深。

## 2. 财务深度解析 (Financial Analysis)
根据解析提取的数据表明，公司实现了指数级增长：
* **营收端**：第四季度总营收达到 221亿美元，**同比增长高达 265%**。其中数据中心业务贡献了绝大部分增量（184亿美元，YoY +409%）。
* **利润端**：毛利率攀升至 76.0%，显示出极强的定价权和规模效应。

## 3. 市场舆情与催化剂 (Market Sentiment & Catalysts)
通过实时监控矩阵发现，近期市场情绪极度乐观：
* **产品端催化**：下一代 AI 芯片架构据传性能提升30倍，引发开发者生态热议。
* **资本面**：华尔街主流机构密集上调目标价，显示出机构资金的强烈看多共识。

> 提示：以上数据由多 Agent 协作自动提取并交叉验证。
"""
        return self.call_llm(system_prompt, user_prompt, mock_response=mock_res)
