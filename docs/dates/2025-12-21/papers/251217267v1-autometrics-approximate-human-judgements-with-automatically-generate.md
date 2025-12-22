---
layout: default
title: AutoMetrics: Approximate Human Judgements with Automatically Generated Evaluators
---

# AutoMetrics: Approximate Human Judgements with Automatically Generated Evaluators
**arXiv**：[2512.17267v1](https://arxiv.org/abs/2512.17267) · [PDF](https://arxiv.org/pdf/2512.17267.pdf)  
**作者**：Michael J. Ryan, Yanzhe Zhang, Amol Salunkhe, Yi Chu, Di Xu, Diyi Yang  

**一句话要点**：提出AutoMetrics框架，在低数据约束下合成评估指标以近似人类判断。

**关键词**：自动评估指标, 低数据学习, LLM-as-a-Judge, 回归合成, 开放域应用, MetricBank

## 3 点简述
- 核心问题：用户反馈稀缺或缓慢，难以评估开放域AI应用。
- 方法要点：结合检索MetricBank和LLM生成标准，通过回归最大化与人类信号相关性。
- 实验或效果：在5个任务中，相比LLM-as-a-Judge，Kendall相关性提升达33.4%，需少于100个反馈点。

## 摘要（原文）

> Evaluating user-facing AI applications remains a central challenge, especially in open-ended domains such as travel planning, clinical note generation, or dialogue. The gold standard is user feedback (e.g., thumbs up/down) or behavioral signals (e.g., retention), but these are often scarce in prototypes and research projects, or too-slow to use for system optimization. We present AutoMetrics, a framework for synthesizing evaluation metrics under low-data constraints. AutoMetrics combines retrieval from MetricBank, a collection of 48 metrics we curate, with automatically generated LLM-as-a-Judge criteria informed by lightweight human feedback. These metrics are composed via regression to maximize correlation with human signal. AutoMetrics takes you from expensive measures to interpretable automatic metrics. Across 5 diverse tasks, AutoMetrics improves Kendall correlation with human ratings by up to 33.4% over LLM-as-a-Judge while requiring fewer than 100 feedback points. We show that AutoMetrics can be used as a proxy reward to equal effect as a verifiable reward. We release the full AutoMetrics toolkit and MetricBank to accelerate adaptive evaluation of LLM applications.

