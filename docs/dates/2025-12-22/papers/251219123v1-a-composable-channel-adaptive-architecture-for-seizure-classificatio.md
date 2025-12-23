---
layout: default
title: A Composable Channel-Adaptive Architecture for Seizure Classification
---

# A Composable Channel-Adaptive Architecture for Seizure Classification
**arXiv**：[2512.19123v1](https://arxiv.org/abs/2512.19123) · [PDF](https://arxiv.org/pdf/2512.19123.pdf)  
**作者**：Francesco Carzaniga, Michael Hersche, Kaspar Schindler, Abbas Rahimi  

**一句话要点**：提出可组合通道自适应架构，用于处理任意通道数的颅内脑电图以进行癫痫分类。

**关键词**：癫痫分类, 通道自适应架构, 颅内脑电图处理, 向量符号算法, 长时记忆模块, 个性化微调

## 3 点简述
- 核心问题：处理多通道颅内脑电图时，现有模型难以适应不同受试者的通道异质性，且时间上下文有限。
- 方法要点：先独立处理单通道信号，再通过向量符号算法融合特征，并引入长达2分钟的记忆模块进行分类。
- 实验或效果：在短期和长期数据集上，CA-EEGWaveNet和CA-EEGNet均超越基线模型，F1分数更高，且个性化微调更快。

## 摘要（原文）

> Objective: We develop a channel-adaptive (CA) architecture that seamlessly processes multi-variate time-series with an arbitrary number of channels, and in particular intracranial electroencephalography (iEEG) recordings. Methods: Our CA architecture first processes the iEEG signal using state-of-the-art models applied to each single channel independently. The resulting features are then fused using a vector-symbolic algorithm which reconstructs the spatial relationship using a trainable scalar per channel. Finally, the fused features are accumulated in a long-term memory of up to 2 minutes to perform the classification. Each CA-model can then be pre-trained on a large corpus of iEEG recordings from multiple heterogeneous subjects. The pre-trained model is personalized to each subject via a quick fine-tuning routine, which uses equal or lower amounts of data compared to existing state-of-the-art models, but requiring only 1/5 of the time. Results: We evaluate our CA-models on a seizure detection task both on a short-term (~20 hours) and a long-term (~2500 hours) dataset. In particular, our CA-EEGWaveNet is trained on a single seizure of the tested subject, while the baseline EEGWaveNet is trained on all but one. Even in this challenging scenario, our CA-EEGWaveNet surpasses the baseline in median F1-score (0.78 vs 0.76). Similarly, CA-EEGNet based on EEGNet, also surpasses its baseline in median F1-score (0.79 vs 0.74). Conclusion and significance: Our CA-model addresses two issues: first, it is channel-adaptive and can therefore be trained across heterogeneous subjects without loss of performance; second, it increases the effective temporal context size to a clinically-relevant length. Therefore, our model is a drop-in replacement for existing models, bringing better characteristics and performance across the board.

