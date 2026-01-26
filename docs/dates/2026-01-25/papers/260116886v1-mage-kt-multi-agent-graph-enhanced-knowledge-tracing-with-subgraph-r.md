---
layout: default
title: MAGE-KT: Multi-Agent Graph-Enhanced Knowledge Tracing with Subgraph Retrieval and Asymmetric Fusion
---

# MAGE-KT: Multi-Agent Graph-Enhanced Knowledge Tracing with Subgraph Retrieval and Asymmetric Fusion
**arXiv**：[2601.16886v1](https://arxiv.org/abs/2601.16886) · [PDF](https://arxiv.org/pdf/2601.16886.pdf)  
**作者**：Chi Yu, Hongyu Yuan, Zhiyi Duan  

**一句话要点**：提出多智能体图增强知识追踪框架，通过子图检索与不对称融合解决图注意力扩散和计算噪声问题。

**关键词**：知识追踪, 异构图, 子图检索, 注意力机制, 多智能体学习

## 3 点简述
- 核心问题：现有图知识追踪方法未充分探索概念间关系，且全图编码计算成本高、易引入噪声。
- 方法要点：构建多视图异构图，基于学生历史检索高价值子图，采用不对称交叉注意力融合模块增强预测。
- 实验或效果：在三个数据集上验证，概念关系准确性和下一问题预测性能优于现有方法。

## 摘要（原文）

> Knowledge Tracing (KT) aims to model a student's learning trajectory and predict performance on the next question. A key challenge is how to better represent the relationships among students, questions, and knowledge concepts (KCs). Recently, graph-based KT paradigms have shown promise for this problem. However, existing methods have not sufficiently explored inter-concept relations, often inferred solely from interaction sequences. In addition, the scale and heterogeneity of KT graphs make full-graph encoding both computationally both costly and noise-prone, causing attention to bleed into student-irrelevant regions and degrading the fidelity of inter-KC relations. To address these issues, we propose a novel framework: Multi-Agent Graph-Enhanced Knowledge Tracing (MAGE-KT). It constructs a multi-view heterogeneous graph by combining a multi-agent KC relation extractor and a student-question interaction graph, capturing complementary semantic and behavioral signals. Conditioned on the target student's history, it retrieves compact, high-value subgraphs and integrates them using an Asymmetric Cross-attention Fusion Module to enhance prediction while avoiding attention diffusion and irrelevant computation. Experiments on three widely used KT datasets show substantial improvements in KC-relation accuracy and clear gains in next-question prediction over existing methods.

