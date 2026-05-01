from .base_agent import BaseAgent

class AnalysisAgent(BaseAgent):
    def __init__(self):
        super().__init__(role_name="Financial Analysis Agent")

    def extract_metrics(self, company_name, report_text):
        system_prompt = """
        你是一个资深的华尔街数据分析师。你需要从提供的长文本财报中提取核心财务指标。
        请严格按照 JSON 格式输出，包含以下字段：Revenue, YoY_Growth, Gross_Margin, Key_Highlights。
        """
        
        user_prompt = f"请分析以下 {company_name} 的财报截取内容：\n{report_text}"
        
        mock_res = """
        - 总营收: 221亿美元 (YoY +265%)
        - 数据中心营收: 184亿美元 (YoY +409%)
        - 毛利率: 76.0%
        - 核心亮点: 数据中心业务呈现指数级爆发，整体利润率显著提升。
        """
        
        return self.call_llm(system_prompt, user_prompt, mock_response=mock_res)
