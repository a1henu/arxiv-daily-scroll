---
layout: default
title: Sci-CoE: Co-evolving Scientific Reasoning LLMs via Geometric Consensus with Sparse Supervision
---

# Sci-CoE: Co-evolving Scientific Reasoning LLMs via Geometric Consensus with Sparse Supervision
**arXiv**：[2602.12164v1](https://arxiv.org/abs/2602.12164) · [PDF](https://arxiv.org/pdf/2602.12164.pdf)  
**作者**：Xiaohan He, Shiyang Feng, Songtao Huang, Lei Bai, Bin Wang, Bo Zhang  

**一句话要点**：提出Sci-CoE框架，通过几何共识与稀疏监督提升科学推理LLMs的鲁棒性。

**关键词**：科学推理, 协同进化, 几何共识, 稀疏监督, 无监督学习, 大语言模型

## 3 点简述
- 核心问题：科学推理任务中LLMs因评估不可靠和验证策略单一而脆弱。
- 方法要点：两阶段协同进化框架，从稀疏监督过渡到无监督学习，引入几何奖励机制。
- 实验或效果：在多个科学基准测试中增强复杂推理能力，展现强可扩展性。

## 摘要（原文）

> Large language models (LLMs) have demonstrated exceptional reasoning capabilities, and co-evolving paradigms have shown promising results in domains such as code and math. However, in scientific reasoning tasks, these models remain fragile due to unreliable solution evaluation and limited diversity in verification strategies. In this work, we propose Sci-CoE, a two-stage scientific co-evolving framework that enables models to self-evolve as both solver and verifier through a transition from sparse supervision to unsupervised learning. In the first stage, the model uses a small set of annotated data to establish fundamental correctness judgment anchors for the Verifier. In the second stage, we introduce a geometric reward mechanism that jointly considers consensus, reliability, and diversity, driving large-scale self-iteration on unlabeled data. Experiments on several general scientific benchmarks demonstrate that Sci-CoE enhances complex reasoning capabilities and exhibits strong scalability, facilitating the construction of more robust and diverse evaluation systems. Codes are available at https://github.com/InternScience/Sci-CoE.

