---
layout: default
title: Computing Conditional Shapley Values Using Tabular Foundation Models
---

# Computing Conditional Shapley Values Using Tabular Foundation Models
**arXiv**：[2602.09489v1](https://arxiv.org/abs/2602.09489) · [PDF](https://arxiv.org/pdf/2602.09489.pdf)  
**作者**：Lars Henry Berge Olsen, Dennis Christensen  

**一句话要点**：利用表格基础模型高效计算条件Shapley值，提升可解释AI性能

**关键词**：条件Shapley值, 表格基础模型, 可解释AI, 上下文学习, 计算效率

## 3 点简述
- 核心问题：Shapley值计算成本高，尤其在特征依赖时需近似大量条件期望。
- 方法要点：使用TabPFN等表格基础模型，通过上下文学习避免重训练，快速近似条件期望。
- 实验或效果：在模拟和真实数据集上，TabPFN通常性能最佳，运行时间显著减少。

## 摘要（原文）

> Shapley values have become a cornerstone of explainable AI, but they are computationally expensive to use, especially when features are dependent. Evaluating them requires approximating a large number of conditional expectations, either via Monte Carlo integration or regression. Until recently it has not been possible to fully exploit deep learning for the regression approach, because retraining for each conditional expectation takes too long. Tabular foundation models such as TabPFN overcome this computational hurdle by leveraging in-context learning, so each conditional expectation can be approximated without any re-training. In this paper, we compute Shapley values with multiple variants of TabPFN and compare their performance with state-of-the-art methods on both simulated and real datasets. In most cases, TabPFN yields the best performance; where it does not, it is only marginally worse than the best method, at a fraction of the runtime. We discuss further improvements and how tabular foundation models can be better adapted specifically for conditional Shapley value estimation.

