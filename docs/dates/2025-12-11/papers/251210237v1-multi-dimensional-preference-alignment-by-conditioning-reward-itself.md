---
layout: default
title: Multi-dimensional Preference Alignment by Conditioning Reward Itself
---

# Multi-dimensional Preference Alignment by Conditioning Reward Itself
**arXiv**：[2512.10237v1](https://arxiv.org/abs/2512.10237) · [PDF](https://arxiv.org/pdf/2512.10237.pdf)  
**作者**：Jiho Jang, Jinyoung Kim, Kyungjune Baek, Nojun Kwak  

**一句话要点**：提出多奖励条件DPO以解决扩散模型对齐中的奖励冲突问题

**关键词**：扩散模型对齐, 奖励冲突, 多维度偏好, 条件化训练, 强化学习

## 3 点简述
- 标准DPO因Bradley-Terry模型聚合多维度奖励导致冲突，迫使模型遗忘特定维度的有益特征
- MCDPO引入解耦Bradley-Terry目标，通过偏好结果向量条件化训练，独立优化各奖励维度
- 在Stable Diffusion 1.5和SDXL上实验显示，MCDPO性能优越，支持推理时动态多轴控制

## 摘要（原文）

> Reinforcement Learning from Human Feedback has emerged as a standard for aligning diffusion models. However, we identify a fundamental limitation in the standard DPO formulation because it relies on the Bradley-Terry model to aggregate diverse evaluation axes like aesthetic quality and semantic alignment into a single scalar reward. This aggregation creates a reward conflict where the model is forced to unlearn desirable features of a specific dimension if they appear in a globally non-preferred sample. To address this issue, we propose Multi Reward Conditional DPO (MCDPO). This method resolves reward conflicts by introducing a disentangled Bradley-Terry objective. MCDPO explicitly injects a preference outcome vector as a condition during training, which allows the model to learn the correct optimization direction for each reward axis independently within a single network. We further introduce dimensional reward dropout to ensure balanced optimization across dimensions. Extensive experiments on Stable Diffusion 1.5 and SDXL demonstrate that MCDPO achieves superior performance on benchmarks. Notably, our conditional framework enables dynamic and multiple-axis control at inference time using Classifier Free Guidance to amplify specific reward dimensions without additional training or external reward models.

