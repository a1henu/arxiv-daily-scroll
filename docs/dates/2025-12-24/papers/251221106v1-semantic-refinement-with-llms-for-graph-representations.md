---
layout: default
title: Semantic Refinement with LLMs for Graph Representations
---

# Semantic Refinement with LLMs for Graph Representations
**arXiv**：[2512.21106v1](https://arxiv.org/abs/2512.21106) · [PDF](https://arxiv.org/pdf/2512.21106.pdf)  
**作者**：Safal Thapaliya, Zehong Wang, Jiazheng Li, Ziming Li, Yanfang Ye, Chuxu Zhang  

**一句话要点**：提出数据自适应语义精炼框架DAS，通过耦合GNN与LLM解决图数据中结构与语义异质性问题。

**关键词**：图表示学习, 语义精炼, 大语言模型, 图神经网络, 数据自适应, 异质性

## 3 点简述
- 核心问题：图数据中结构与语义异质性导致固定归纳偏置模型难以泛化。
- 方法要点：采用数据中心视角，将节点语义作为任务自适应变量，通过GNN与LLM闭环反馈精炼语义。
- 实验或效果：在结构主导图上表现提升，语义丰富图上保持竞争力，验证数据自适应语义适应有效性。

## 摘要（原文）

> Graph-structured data exhibit substantial heterogeneity in where their predictive signals originate: in some domains, node-level semantics dominate, while in others, structural patterns play a central role. This structure-semantics heterogeneity implies that no graph learning model with a fixed inductive bias can generalize optimally across diverse graph domains. However, most existing methods address this challenge from the model side by incrementally injecting new inductive biases, which remains fundamentally limited given the open-ended diversity of real-world graphs. In this work, we take a data-centric perspective and treat node semantics as a task-adaptive variable. We propose a Data-Adaptive Semantic Refinement framework DAS for graph representation learning, which couples a fixed graph neural network (GNN) and a large language model (LLM) in a closed feedback loop. The GNN provides implicit supervisory signals to guide the semantic refinement of LLM, and the refined semantics are fed back to update the same graph learner. We evaluate our approach on both text-rich and text-free graphs. Results show consistent improvements on structure-dominated graphs while remaining competitive on semantics-rich graphs, demonstrating the effectiveness of data-centric semantic adaptation under structure-semantics heterogeneity.

