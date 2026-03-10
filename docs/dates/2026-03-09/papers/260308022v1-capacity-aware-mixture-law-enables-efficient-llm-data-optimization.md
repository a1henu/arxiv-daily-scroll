---
layout: default
title: Capacity-Aware Mixture Law Enables Efficient LLM Data Optimization
---

# Capacity-Aware Mixture Law Enables Efficient LLM Data Optimization
**arXiv**：[2603.08022v1](https://arxiv.org/abs/2603.08022) · [PDF](https://arxiv.org/pdf/2603.08022.pdf)  
**作者**：Jingwei Li, Xinran Gu, Jingzhao Zhang  

**一句话要点**：提出容量感知混合定律以高效优化大语言模型数据混合

**关键词**：数据混合优化, 缩放定律, 大语言模型训练, 混合专家模型, 计算效率

## 3 点简述
- 核心问题：现有数据混合方法成本高或缩放定律外推性差，影响下游性能优化。
- 方法要点：引入CAMEL定律建模模型大小与混合的非线性交互，结合损失到基准预测定律实现端到端性能预测。
- 实验或效果：在混合专家模型上验证，减少优化成本50%，提升下游基准性能达3%。

## 摘要（原文）

> A data mixture refers to how different data sources are combined to train large language models, and selecting an effective mixture is crucial for optimal downstream performance. Existing methods either conduct costly searches directly on the target model or rely on mixture scaling laws that fail to extrapolate well to large model sizes. We address these limitations by introducing a compute-efficient pipeline for data mixture scaling. First, we propose CAMEL, a capacity-aware mixture law that models validation loss with the nonlinear interplay between model size and mixture. We also introduce a loss-to-benchmark prediction law that estimates benchmark accuracy from validation loss, enabling end-to-end performance prediction for the target model. Next, we study how to allocate a fixed compute budget across model scales to fit the law and reduce prediction error. Finally, we apply our method to Mixture-of-Experts models with up to 7B-A150M parameters to fit the law, and verify the optimal mixture derived from the law by extrapolating to a 55B-A1.2B target model. Compared to prior methods, we reduces mixture optimization costs by 50\% and improves downstream benchmark performance by up to 3\%.

