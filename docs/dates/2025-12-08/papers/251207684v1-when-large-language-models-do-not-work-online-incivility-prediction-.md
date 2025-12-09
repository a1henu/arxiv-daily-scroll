---
layout: default
title: When Large Language Models Do Not Work: Online Incivility Prediction through Graph Neural Networks
---

# When Large Language Models Do Not Work: Online Incivility Prediction through Graph Neural Networks
**arXiv**：[2512.07684v1](https://arxiv.org/abs/2512.07684) · [PDF](https://arxiv.org/pdf/2512.07684.pdf)  
**作者**：Zihan Chen, Lanyu Yu  

**一句话要点**：提出基于图神经网络的框架，以解决在线社区不文明行为检测中准确性和效率不足的问题。

**关键词**：在线不文明行为检测, 图神经网络, 文本相似性, 注意力机制, 行为预测, 英语维基百科

## 3 点简述
- 在线不文明行为在数字社区中普遍存在，现有方法在准确性和效率上受限。
- 模型将用户评论表示为节点，基于文本相似性构建边，结合语言内容和关系结构学习。
- 实验显示，该框架在多个指标上优于12个大型语言模型，且推理成本显著降低。

## 摘要（原文）

> Online incivility has emerged as a widespread and persistent problem in digital communities, imposing substantial social and psychological burdens on users. Although many platforms attempt to curb incivility through moderation and automated detection, the performance of existing approaches often remains limited in both accuracy and efficiency. To address this challenge, we propose a Graph Neural Network (GNN) framework for detecting three types of uncivil behavior (i.e., toxicity, aggression, and personal attacks) within the English Wikipedia community. Our model represents each user comment as a node, with textual similarity between comments defining the edges, allowing the network to jointly learn from both linguistic content and relational structures among comments. We also introduce a dynamically adjusted attention mechanism that adaptively balances nodal and topological features during information aggregation. Empirical evaluations demonstrate that our proposed architecture outperforms 12 state-of-the-art Large Language Models (LLMs) across multiple metrics while requiring significantly lower inference cost. These findings highlight the crucial role of structural context in detecting online incivility and address the limitations of text-only LLM paradigms in behavioral prediction. All datasets and comparative outputs will be publicly available in our repository to support further research and reproducibility.

