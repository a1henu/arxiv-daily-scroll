---
layout: default
title: EXaMCaP: Subset Selection with Entropy Gain Maximization for Probing Capability Gains of Large Chart Understanding Training Sets
---

# EXaMCaP: Subset Selection with Entropy Gain Maximization for Probing Capability Gains of Large Chart Understanding Training Sets
**arXiv**：[2602.04365v1](https://arxiv.org/abs/2602.04365) · [PDF](https://arxiv.org/pdf/2602.04365.pdf)  
**作者**：Jiapeng Liu, Liang Li, Bing Li, Peng Fu, Xiyan Gao, Chengyang Fang, Xiaoshuai Hao, Can Ma  

**一句话要点**：提出EXaMCaP，通过熵增益最大化选择子集以探测大型图表理解训练集的能力增益

**关键词**：图表理解, 子集选择, 熵增益最大化, 多模态大语言模型, 数据集评估

## 3 点简述
- 问题：全量微调MLLMs评估图表理解数据集能力增益耗时高，阻碍数据集迭代优化
- 方法：基于熵增益最大化选择高多样性子集，近似最大熵子集以探测能力增益
- 效果：EXaMCaP在探测能力增益上优于基线，适用于不同子集大小和MLLM架构

## 摘要（原文）

> Recent works focus on synthesizing Chart Understanding (ChartU) training sets to inject advanced chart knowledge into Multimodal Large Language Models (MLLMs), where the sufficiency of the knowledge is typically verified by quantifying capability gains via the fine-tune-then-evaluate paradigm. However, full-set fine-tuning MLLMs to assess such gains incurs significant time costs, hindering the iterative refinement cycles of the ChartU dataset. Reviewing the ChartU dataset synthesis and data selection domains, we find that subsets can potentially probe the MLLMs' capability gains from full-set fine-tuning. Given that data diversity is vital for boosting MLLMs' performance and entropy reflects this feature, we propose EXaMCaP, which uses entropy gain maximization to select a subset. To obtain a high-diversity subset, EXaMCaP chooses the maximum-entropy subset from the large ChartU dataset. As enumerating all possible subsets is impractical, EXaMCaP iteratively selects samples to maximize the gain in set entropy relative to the current set, approximating the maximum-entropy subset of the full dataset. Experiments show that EXaMCaP outperforms baselines in probing the capability gains of the ChartU training set, along with its strong effectiveness across diverse subset sizes and compatibility with various MLLM architectures.

