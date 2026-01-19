---
layout: default
title: FORESTLLM: Large Language Models Make Random Forest Great on Few-shot Tabular Learning
---

# FORESTLLM: Large Language Models Make Random Forest Great on Few-shot Tabular Learning
**arXiv**：[2601.11311v1](https://arxiv.org/abs/2601.11311) · [PDF](https://arxiv.org/pdf/2601.11311.pdf)  
**作者**：Zhihan Yang, Jiaqi Wei, Xiang Zhang, Haoyu Dong, Yiwen Wang, Xiaoke Guo, Pengkun Zhang, Yiwei Xu, Chenyu You  

**一句话要点**：提出FORESTLLM框架，结合决策森林与LLM，解决小样本表格学习问题。

**关键词**：小样本学习, 表格数据, 决策森林, 大语言模型, 语义分割, 模型蒸馏

## 3 点简述
- 核心问题：小样本表格学习中，传统树方法易过拟合，LLM直接应用忽略结构。
- 方法要点：利用LLM作为离线模型设计器，引入语义分割准则和一次性上下文推理机制。
- 实验或效果：在多样小样本分类和回归基准测试中，达到最先进性能。

## 摘要（原文）

> Tabular data high-stakes critical decision-making in domains such as finance, healthcare, and scientific discovery. Yet, learning effectively from tabular data in few-shot settings, where labeled examples are scarce, remains a fundamental challenge. Traditional tree-based methods often falter in these regimes due to their reliance on statistical purity metrics, which become unstable and prone to overfitting with limited supervision. At the same time, direct applications of large language models (LLMs) often overlook its inherent structure, leading to suboptimal performance. To overcome these limitations, we propose FORESTLLM, a novel framework that unifies the structural inductive biases of decision forests with the semantic reasoning capabilities of LLMs. Crucially, FORESTLLM leverages the LLM only during training, treating it as an offline model designer that encodes rich, contextual knowledge into a lightweight, interpretable forest model, eliminating the need for LLM inference at test time. Our method is two-fold. First, we introduce a semantic splitting criterion in which the LLM evaluates candidate partitions based on their coherence over both labeled and unlabeled data, enabling the induction of more robust and generalizable tree structures under few-shot supervision. Second, we propose a one-time in-context inference mechanism for leaf node stabilization, where the LLM distills the decision path and its supporting examples into a concise, deterministic prediction, replacing noisy empirical estimates with semantically informed outputs. Across a diverse suite of few-shot classification and regression benchmarks, FORESTLLM achieves state-of-the-art performance.

