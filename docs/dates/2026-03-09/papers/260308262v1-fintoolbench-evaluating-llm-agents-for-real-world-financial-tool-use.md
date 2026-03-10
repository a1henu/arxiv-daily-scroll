---
layout: default
title: FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use
---

# FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use
**arXiv**：[2603.08262v1](https://arxiv.org/abs/2603.08262) · [PDF](https://arxiv.org/pdf/2603.08262.pdf)  
**作者**：Jiaxuan Lu, Kong Wang, Yemin Wang, Qingmei Tang, Hongwei Zeng, Xiang Chen, Jiahao Pi, Shujian Deng, Lingzhi Chen, Yi Fu, Kehua Yang, Xiao Sun  

**一句话要点**：提出FinToolBench基准以评估金融领域大语言模型代理的工具使用能力

**关键词**：金融工具学习, 大语言模型代理, 可执行基准, 工具检索, 监管合规, 评估框架

## 3 点简述
- 现有金融评估缺乏动态工具执行，忽略高风险、合规和快速数据变化需求
- FinToolBench集成760个可执行金融工具和295个查询，提供真实可运行测试环境
- 引入多维度评估框架和FATR基线，强调及时性、意图类型和监管对齐

## 摘要（原文）

> The integration of Large Language Models (LLMs) into the financial domain is driving a paradigm shift from passive information retrieval to dynamic, agentic interaction. While general-purpose tool learning has witnessed a surge in benchmarks, the financial sector, characterized by high stakes, strict compliance, and rapid data volatility, remains critically underserved. Existing financial evaluations predominantly focus on static textual analysis or document-based QA, ignoring the complex reality of tool execution. Conversely, general tool benchmarks lack the domain-specific rigor required for finance, often relying on toy environments or a negligible number of financial APIs. To bridge this gap, we introduce FinToolBench, the first real-world, runnable benchmark dedicated to evaluating financial tool learning agents. Unlike prior works limited to a handful of mock tools, FinToolBench establishes a realistic ecosystem coupling 760 executable financial tools with 295 rigorous, tool-required queries. We propose a novel evaluation framework that goes beyond binary execution success, assessing agents on finance-critical dimensions: timeliness, intent type, and regulatory domain alignment. Furthermore, we present FATR, a finance-aware tool retrieval and reasoning baseline that enhances stability and compliance. By providing the first testbed for auditable, agentic financial execution, FinToolBench sets a new standard for trustworthy AI in finance. The tool manifest, execution environment, and evaluation code will be open-sourced to facilitate future research.

