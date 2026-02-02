---
layout: default
title: TSAQA: Time Series Analysis Question And Answering Benchmark
---

# TSAQA: Time Series Analysis Question And Answering Benchmark
**arXiv**：[2601.23204v1](https://arxiv.org/abs/2601.23204) · [PDF](https://arxiv.org/pdf/2601.23204.pdf)  
**作者**：Baoyu Jing, Sanhorn Chen, Lecheng Zheng, Boyu Liu, Zihao Li, Jiaru Zou, Tianxin Wei, Zhining Liu, Zhichen Zeng, Ruizhong Qiu, Xiao Lin, Yuchen Yan, Dongqi Fu, Jingchao Ni, Jingrui He, Hanghang Tong  

**一句话要点**：提出TSAQA基准以扩展时间序列问答任务覆盖并评估LLMs的时序分析能力。

**关键词**：时间序列问答, 多任务基准, 大语言模型评估, 时序分析, 数据集构建

## 3 点简述
- 当前基准局限于预测和异常检测，缺乏多样化时序分析任务。
- TSAQA整合六类任务，包括异常检测、分类、表征、比较、数据转换和时序关系分析。
- 零样本评估显示LLMs表现不佳，指令微调提升开源模型性能但仍有改进空间。

## 摘要（原文）

> Time series data are integral to critical applications across domains such as finance, healthcare, transportation, and environmental science. While recent work has begun to explore multi-task time series question answering (QA), current benchmarks remain limited to forecasting and anomaly detection tasks. We introduce TSAQA, a novel unified benchmark designed to broaden task coverage and evaluate diverse temporal analysis capabilities. TSAQA integrates six diverse tasks under a single framework ranging from conventional analysis, including anomaly detection and classification, to advanced analysis, such as characterization, comparison, data transformation, and temporal relationship analysis. Spanning 210k samples across 13 domains, the dataset employs diverse formats, including true-or-false (TF), multiple-choice (MC), and a novel puzzling (PZ), to comprehensively assess time series analysis. Zero-shot evaluation demonstrates that these tasks are challenging for current Large Language Models (LLMs): the best-performing commercial LLM, Gemini-2.5-Flash, achieves an average score of only 65.08. Although instruction tuning boosts open-source performance: the best-performing open-source model, LLaMA-3.1-8B, shows significant room for improvement, highlighting the complexity of temporal analysis for LLMs.

