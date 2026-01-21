---
layout: default
title: RL-BioAug: Label-Efficient Reinforcement Learning for Self-Supervised EEG Representation Learning
---

# RL-BioAug: Label-Efficient Reinforcement Learning for Self-Supervised EEG Representation Learning
**arXiv**：[2601.13964v1](https://arxiv.org/abs/2601.13964) · [PDF](https://arxiv.org/pdf/2601.13964.pdf)  
**作者**：Cheol-Hui Lee, Hwa-Yeon Lee, Dong-Joo Kim  

**一句话要点**：提出RL-BioAug框架，利用标签高效强化学习优化EEG自监督表示学习中的数据增强策略。

**关键词**：脑电图表示学习, 自监督学习, 强化学习, 数据增强, 非平稳信号处理

## 3 点简述
- 核心问题：EEG信号非平稳性导致静态或随机数据增强策略难以保留内在信息，影响对比学习性能。
- 方法要点：通过强化学习代理自主选择最优增强策略，仅需10%标签数据指导，实现严格自监督表示学习。
- 实验或效果：在Sleep-EDFX和CHB-MIT数据集上，Macro-F1分数分别提升9.69%和8.80%，优于随机策略。

## 摘要（原文）

> The quality of data augmentation serves as a critical determinant for the performance of contrastive learning in EEG tasks. Although this paradigm is promising for utilizing unlabeled data, static or random augmentation strategies often fail to preserve intrinsic information due to the non-stationarity of EEG signals where statistical properties change over time. To address this, we propose RL-BioAug, a framework that leverages a label-efficient reinforcement learning (RL) agent to autonomously determine optimal augmentation policies. While utilizing only a minimal fraction (10\%) of labeled data to guide the agent's policy, our method enables the encoder to learn robust representations in a strictly self-supervised manner. Experimental results demonstrate that RL-BioAug significantly outperforms the random selection strategy, achieving substantial improvements of 9.69\% and 8.80\% in Macro-F1 score on the Sleep-EDFX and CHB-MIT datasets, respectively. Notably, this agent mainly chose optimal strategies for each task -- for example, Time Masking with a 62\% probability for sleep stage classification and Crop \& Resize with a 77\% probability for seizure detection. Our framework suggests its potential to replace conventional heuristic-based augmentations and establish a new autonomous paradigm for data augmentation. The source code is available at \href{https://github.com/dlcjfgmlnasa/RL-BioAug}{https://github.com/dlcjfgmlnasa/RL-BioAug}.

