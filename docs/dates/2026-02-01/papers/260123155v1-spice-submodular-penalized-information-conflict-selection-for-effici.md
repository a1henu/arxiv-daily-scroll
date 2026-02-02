---
layout: default
title: SPICE: Submodular Penalized Information-Conflict Selection for Efficient Large Language Model Training
---

# SPICE: Submodular Penalized Information-Conflict Selection for Efficient Large Language Model Training
**arXiv**：[2601.23155v1](https://arxiv.org/abs/2601.23155) · [PDF](https://arxiv.org/pdf/2601.23155.pdf)  
**作者**：Powei Chang, Jinpeng Zhang, Bowen Chen, Chenyu Wang, Chenlu Guo, Yixing Zhang, Yukang Gao, JianXiang Xiang, Yue Gao, Chaoqun Sun, Yiyi Chen, Dongying Kong  

**一句话要点**：提出SPICE方法以解决大语言模型训练中梯度冲突导致信息选择效率低的问题

**关键词**：大语言模型训练, 数据选择, 梯度冲突, 子模优化, 指令调优, 高效训练

## 3 点简述
- 核心问题：基于信息的数据选择中，梯度冲突减缓边际信息增益衰减，影响选择效率
- 方法要点：通过ε-分解量化冲突，设计冲突感知选择器最大化信息并惩罚错位
- 实验或效果：在8个基准测试中，使用10%数据匹配或超越全数据调优，显著降低训练成本

## 摘要（原文）

> Information-based data selection for instruction tuning is compelling: maximizing the log-determinant of the Fisher information yields a monotone submodular objective, enabling greedy algorithms to achieve a $(1-1/e)$ approximation under a cardinality budget. In practice, however, we identify alleviating gradient conflicts, misalignment between per-sample gradients, is a key factor that slows down the decay of marginal log-determinant information gains, thereby preventing significant loss of information. We formalize this via an $\varepsilon$-decomposition that quantifies the deviation from ideal submodularity as a function of conflict statistics, yielding data-dependent approximation factors that tighten as conflicts diminish. Guided by this analysis, we propose SPICE, a conflict-aware selector that maximizes information while penalizing misalignment, and that supports early stopping and proxy models for efficiency. Empirically, SPICE selects subsets with higher log-determinant information than original criteria, and these informational gains translate into performance improvements: across 8 benchmarks with LLaMA2-7B and Qwen2-7B, SPICE uses only 10% of the data, yet matches or exceeds 6 methods including full-data tuning. This achieves performance improvements with substantially lower training cost.

