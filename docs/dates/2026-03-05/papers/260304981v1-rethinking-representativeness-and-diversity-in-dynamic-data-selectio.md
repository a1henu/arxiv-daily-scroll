---
layout: default
title: Rethinking Representativeness and Diversity in Dynamic Data Selection
---

# Rethinking Representativeness and Diversity in Dynamic Data Selection
**arXiv**：[2603.04981v1](https://arxiv.org/abs/2603.04981) · [PDF](https://arxiv.org/pdf/2603.04981.pdf)  
**作者**：Yuzhe Zhou, Zhenglin Hua, Haiyun Guo, Yuheng Jia  

**一句话要点**：提出动态数据选择框架，通过重新定义代表性和多样性以加速训练并保持准确性。

**关键词**：动态数据选择, 样本代表性, 过程级多样性, 训练加速, 稀疏自编码器, 梯度偏差减少

## 3 点简述
- 核心问题：动态数据选择中样本评估的代表性和多样性定义不足，影响训练效率与准确性。
- 方法要点：基于数据集级特征因子覆盖定义代表性，结合过程级多样性与使用频率惩罚实现样本轮换。
- 实验或效果：在视觉和文本任务上实现超过2倍训练加速，匹配或超越全数据准确性。

## 摘要（原文）

> Dynamic data selection accelerates training by sampling a changing subset of the dataset while preserving accuracy. We rethink two core notions underlying sample evaluation: representativeness and diversity. Instead of local geometric centrality, we define representativeness as coverage of dataset-level common or high-frequency feature factors. Instead of within-subset dispersion, we define diversity at the process level, requiring the selection trajectory to gradually include complementary rare factors over training. Based on this view, we propose a dynamic selection framework with three components. First, we score representativeness in a plug-in feature space to prioritize samples covering frequent factors. We instantiate this with a sparse autoencoder trained on the target dataset, using sparse unit activations to summarize both individual samples and dataset-wide factor statistics. Second, we realize process-level diversity by combining rare-factor sampling with a Usage-Frequency Penalty that promotes sample rotation, provably discourages monopoly, and reduces gradient bias. Third, we couple the two-dimensional scoring with a smooth scheduler that transitions selection from core-pattern consolidation to rare-factor exploration, without extra gradients, influence estimates, or second-order computations on the training model. Extensive experiments on five benchmarks across vision and text tasks demonstrate improved accuracy-efficiency trade-offs across models. Our method matches or exceeds full-data accuracy with over 2x training acceleration. Code will be released.

