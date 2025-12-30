---
layout: default
title: The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction
---

# The Gaining Paths to Investment Success: Information-Driven LLM Graph Reasoning for Venture Capital Prediction
**arXiv**：[2512.23489v1](https://arxiv.org/abs/2512.23489) · [PDF](https://arxiv.org/pdf/2512.23489.pdf)  
**作者**：Haoyu Pei, Zhongyang Liu, Xiangyi Xiao, Xiaocong Du, Haipeng Zhang, Kunpeng Zhang, Suting Hong  

**一句话要点**：提出MIRAGE-VC框架，通过信息增益驱动路径检索和多智能体融合，解决风险投资预测中的图外推理挑战。

**关键词**：风险投资预测, 图外推理, 信息增益路径检索, 多智能体融合, LLM图推理, 异构证据融合

## 3 点简述
- 核心问题：风险投资预测需从复杂图数据中推理外部目标，传统方法缺乏显式推理能力，图-LLM方法面临路径爆炸和异构证据融合障碍。
- 方法要点：设计信息增益驱动的路径检索器迭代选择高价值邻居，结合多智能体架构通过可学习门控机制融合公司披露、投资者记录和网络结构证据。
- 实验或效果：在严格防泄漏控制下，MIRAGE-VC提升F1分数5.0%和PrecisionAt5 16.6%，并适用于推荐和风险评估等图外预测任务。

## 摘要（原文）

> Most venture capital (VC) investments fail, while a few deliver outsized returns. Accurately predicting startup success requires synthesizing complex relational evidence, including company disclosures, investor track records, and investment network structures, through explicit reasoning to form coherent, interpretable investment theses. Traditional machine learning and graph neural networks both lack this reasoning capability. Large language models (LLMs) offer strong reasoning but face a modality mismatch with graphs. Recent graph-LLM methods target in-graph tasks where answers lie within the graph, whereas VC prediction is off-graph: the target exists outside the network. The core challenge is selecting graph paths that maximize predictor performance on an external objective while enabling step-by-step reasoning. We present MIRAGE-VC, a multi-perspective retrieval-augmented generation framework that addresses two obstacles: path explosion (thousands of candidate paths overwhelm LLM context) and heterogeneous evidence fusion (different startups need different analytical emphasis). Our information-gain-driven path retriever iteratively selects high-value neighbors, distilling investment networks into compact chains for explicit reasoning. A multi-agent architecture integrates three evidence streams via a learnable gating mechanism based on company attributes. Under strict anti-leakage controls, MIRAGE-VC achieves +5.0% F1 and +16.6% PrecisionAt5, and sheds light on other off-graph prediction tasks such as recommendation and risk assessment. Code: https://anonymous.4open.science/r/MIRAGE-VC-323F.

