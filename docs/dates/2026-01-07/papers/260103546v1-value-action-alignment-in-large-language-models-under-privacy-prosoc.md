---
layout: default
title: Value-Action Alignment in Large Language Models under Privacy-Prosocial Conflict
---

# Value-Action Alignment in Large Language Models under Privacy-Prosocial Conflict
**arXiv**：[2601.03546v1](https://arxiv.org/abs/2601.03546) · [PDF](https://arxiv.org/pdf/2601.03546.pdf)  
**作者**：Guanyu Chen, Chenxiao Yu, Xiyang Hu  

**一句话要点**：提出基于上下文的评估协议与价值-行动对齐率，以衡量大语言模型在隐私-亲社会冲突下的决策一致性。

**关键词**：大语言模型评估, 隐私-亲社会冲突, 价值-行动对齐, 结构方程建模, 数据共享决策

## 3 点简述
- 核心问题：现有评估孤立测量隐私态度或分享意图，难以确定模型表达的价值是否预测其数据共享行动。
- 方法要点：引入上下文评估协议，结合标准化问卷和多组结构方程建模分析价值与行动关系。
- 实验或效果：观察到模型特定的隐私-亲社会-数据接受度模式，价值-行动对齐存在显著异质性。

## 摘要（原文）

> Large language models (LLMs) are increasingly used to simulate decision-making tasks involving personal data sharing, where privacy concerns and prosocial motivations can push choices in opposite directions. Existing evaluations often measure privacy-related attitudes or sharing intentions in isolation, which makes it difficult to determine whether a model's expressed values jointly predict its downstream data-sharing actions as in real human behaviors. We introduce a context-based assessment protocol that sequentially administers standardized questionnaires for privacy attitudes, prosocialness, and acceptance of data sharing within a bounded, history-carrying session. To evaluate value-action alignments under competing attitudes, we use multi-group structural equation modeling (MGSEM) to identify relations from privacy concerns and prosocialness to data sharing. We propose Value-Action Alignment Rate (VAAR), a human-referenced directional agreement metric that aggregates path-level evidence for expected signs. Across multiple LLMs, we observe stable but model-specific Privacy-PSA-AoDS profiles, and substantial heterogeneity in value-action alignment.

