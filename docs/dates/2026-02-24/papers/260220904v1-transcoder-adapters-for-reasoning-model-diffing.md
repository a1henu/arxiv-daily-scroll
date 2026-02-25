---
layout: default
title: Transcoder Adapters for Reasoning-Model Diffing
---

# Transcoder Adapters for Reasoning-Model Diffing
**arXiv**：[2602.20904v1](https://arxiv.org/abs/2602.20904) · [PDF](https://arxiv.org/pdf/2602.20904.pdf)  
**作者**：Nathan Hu, Jake Ward, Thomas Icard, Christopher Potts  

**一句话要点**：提出transcoder adapters以解释推理模型微调前后的内部机制差异

**关键词**：推理模型, 模型差异分析, 可解释性, 微调研究, 稀疏激活特征

## 3 点简述
- 核心问题：推理训练对模型内部机制的影响尚不明确
- 方法要点：学习可解释的MLP计算差异近似，应用于Qwen2.5-Math-7B与蒸馏变体
- 实验或效果：适配器恢复50-90%精度增益，特征稀疏激活，可追溯犹豫标记行为

## 摘要（原文）

> While reasoning models are increasingly ubiquitous, the effects of reasoning training on a model's internal mechanisms remain poorly understood. In this work, we introduce transcoder adapters, a technique for learning an interpretable approximation of the difference in MLP computation before and after fine-tuning. We apply transcoder adapters to characterize the differences between Qwen2.5-Math-7B and its reasoning-distilled variant, DeepSeek-R1-Distill-Qwen-7B. Learned adapters are faithful to the target model's internal computation and next-token predictions. When evaluated on reasoning benchmarks, adapters match the reasoning model's response lengths and typically recover 50-90% of the accuracy gains from reasoning fine-tuning. Adapter features are sparsely activating and interpretable. When examining adapter features, we find that only ~8% have activating examples directly related to reasoning behaviors. We deeply study one such behavior -- the production of hesitation tokens (e.g., "wait"). Using attribution graphs, we trace hesitation to only ~2.4% of adapter features (5.6k total) performing one of two functions. These features are necessary and sufficient for producing hesitation tokens; removing them reduces response length, often without affecting accuracy. Overall, our results provide insight into reasoning training and suggest transcoder adapters may be useful for studying fine-tuning more broadly.

