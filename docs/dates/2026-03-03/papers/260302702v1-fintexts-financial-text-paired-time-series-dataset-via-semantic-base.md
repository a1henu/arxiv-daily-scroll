---
layout: default
title: FinTexTS: Financial Text-Paired Time-Series Dataset via Semantic-Based and Multi-Level Pairing
---

# FinTexTS: Financial Text-Paired Time-Series Dataset via Semantic-Based and Multi-Level Pairing
**arXiv**：[2603.02702v1](https://arxiv.org/abs/2603.02702) · [PDF](https://arxiv.org/pdf/2603.02702.pdf)  
**作者**：Jaehoon Lee, Suhwan Park, Tae Yoon Lim, Seunghan Lee, Jun Seo, Dongwan Kang, Hwanil Choi, Minjae Kim, Sungdong Yoo, SoonYoung Lee, Yongjae Lee, Wonbin Ahn  

**一句话要点**：提出语义和多层次配对框架以解决金融时间序列与文本配对中的复杂关系捕获问题。

**关键词**：金融时间序列分析, 文本配对数据集, 语义匹配, 多层次分类, 股价预测, LLM应用

## 3 点简述
- 核心问题：现有基于关键词匹配的金融文本-时间序列配对方法难以捕捉公司间和宏观层面的复杂依赖关系。
- 方法要点：通过SEC文件提取公司上下文，使用嵌入匹配和LLM分类实现语义和多层次新闻配对。
- 实验或效果：构建FinTexTS数据集，实验证明该策略提升股价预测性能，尤其在专有新闻源上效果更佳。

## 摘要（原文）

> The financial domain involves a variety of important time-series problems. Recently, time-series analysis methods that jointly leverage textual and numerical information have gained increasing attention. Accordingly, numerous efforts have been made to construct text-paired time-series datasets in the financial domain. However, financial markets are characterized by complex interdependencies, in which a company's stock price is influenced not only by company-specific events but also by events in other companies and broader macroeconomic factors. Existing approaches that pair text with financial time-series data based on simple keyword matching often fail to capture such complex relationships. To address this limitation, we propose a semantic-based and multi-level pairing framework. Specifically, we extract company-specific context for the target company from SEC filings and apply an embedding-based matching mechanism to retrieve semantically relevant news articles based on this context. Furthermore, we classify news articles into four levels (macro-level, sector-level, related company-level, and target-company level) using large language models (LLMs), enabling multi-level pairing of news articles with the target company. Applying this framework to publicly-available news datasets, we construct \textbf{FinTexTS}, a new large-scale text-paired stock price dataset. Experimental results on \textbf{FinTexTS} demonstrate the effectiveness of our semantic-based and multi-level pairing strategy in stock price forecasting. In addition to publicly-available news underlying \textbf{FinTexTS}, we show that applying our method to proprietary yet carefully curated news sources leads to higher-quality paired data and improved stock price forecasting performance.

