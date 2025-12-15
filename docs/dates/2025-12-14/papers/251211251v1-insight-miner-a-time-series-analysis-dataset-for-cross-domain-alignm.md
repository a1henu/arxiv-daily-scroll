---
layout: default
title: Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Natural Language
---

# Insight Miner: A Time Series Analysis Dataset for Cross-Domain Alignment with Natural Language
**arXiv**：[2512.11251v1](https://arxiv.org/abs/2512.11251) · [PDF](https://arxiv.org/pdf/2512.11251.pdf)  
**作者**：Yunkai Zhang, Yawen Zhang, Ming Zheng, Kezhen Chen, Chongyang Gao, Ruian Ge, Siyuan Teng, Amine Jelloul, Jinmeng Rao, Xiaoyuan Guo, Chiang-Wei Fang, Zeyu Zheng, Jie Yang  

**一句话要点**：提出Insight Miner模型与TS-Insights数据集，以解决跨领域时间序列分析中依赖专家知识的问题。

**关键词**：时间序列分析, 多模态模型, 语言对齐, 数据集构建, 指令调优, 跨领域应用

## 3 点简述
- 核心问题：时间序列分析需深度领域知识，过程耗时费力。
- 方法要点：构建TS-Insights数据集，通过代理工作流合成时间序列与语言对齐数据。
- 实验或效果：Insight Miner在指令调优后，在生成描述和洞察方面优于LLaVA和GPT-4等模型。

## 摘要（原文）

> Time-series data is critical across many scientific and industrial domains, including environmental analysis, agriculture, transportation, and finance. However, mining insights from this data typically requires deep domain expertise, a process that is both time-consuming and labor-intensive. In this paper, we propose \textbf{Insight Miner}, a large-scale multimodal model (LMM) designed to generate high-quality, comprehensive time-series descriptions enriched with domain-specific knowledge. To facilitate this, we introduce \textbf{TS-Insights}\footnote{Available at \href{https://huggingface.co/datasets/zhykoties/time-series-language-alignment}{https://huggingface.co/datasets/zhykoties/time-series-language-alignment}.}, the first general-domain dataset for time series and language alignment. TS-Insights contains 100k time-series windows sampled from 20 forecasting datasets. We construct this dataset using a novel \textbf{agentic workflow}, where we use statistical tools to extract features from raw time series before synthesizing them into coherent trend descriptions with GPT-4. Following instruction tuning on TS-Insights, Insight Miner outperforms state-of-the-art multimodal models, such as LLaVA \citep{liu2023llava} and GPT-4, in generating time-series descriptions and insights. Our findings suggest a promising direction for leveraging LMMs in time series analysis, and serve as a foundational step toward enabling LLMs to interpret time series as a native input modality.

