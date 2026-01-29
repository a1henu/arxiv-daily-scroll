---
layout: default
title: Positive-Unlabeled Reinforcement Learning Distillation for On-Premise Small Models
---

# Positive-Unlabeled Reinforcement Learning Distillation for On-Premise Small Models
**arXiv**：[2601.20687v1](https://arxiv.org/abs/2601.20687) · [PDF](https://arxiv.org/pdf/2601.20687.pdf)  
**作者**：Zhiqiang Kou, Junyang Chen, Xin-Qiang Cai, Xiaobo Xia, Ming-Kun Xie, Dong-Dong Wu, Biao Liu, Yuheng Jia, Xin Geng, Masashi Sugiyama, Tat-Seng Chua  

**一句话要点**：提出正未标记强化学习蒸馏方法，用于本地小模型部署，无需人工偏好或奖励模型。

**关键词**：强化学习蒸馏, 正未标记学习, 本地模型部署, 偏好优化, 小模型对齐

## 3 点简述
- 核心问题：本地小模型部署常因隐私、成本限制，无法进行强化学习对齐，缺乏偏好标注或奖励模型。
- 方法要点：通过查询教师模型获取锚点响应，本地采样学生候选，进行锚点条件自排序，诱导偏好信号以支持本地训练。
- 实验或效果：理论分析支持偏好信号稳定，实验显示在低成本设置下实现强性能。

## 摘要（原文）

> Due to constraints on privacy, cost, and latency, on-premise deployment of small models is increasingly common. However, most practical pipelines stop at supervised fine-tuning (SFT) and fail to reach the reinforcement learning (RL) alignment stage. The main reason is that RL alignment typically requires either expensive human preference annotation or heavy reliance on high-quality reward models with large-scale API usage and ongoing engineering maintenance, both of which are ill-suited to on-premise settings. To bridge this gap, we propose a positive-unlabeled (PU) RL distillation method for on-premise small-model deployment. Without human-labeled preferences or a reward model, our method distills the teacher's preference-optimization capability from black-box generations into a locally trainable student. For each prompt, we query the teacher once to obtain an anchor response, locally sample multiple student candidates, and perform anchor-conditioned self-ranking to induce pairwise or listwise preferences, enabling a fully local training loop via direct preference optimization or group relative policy optimization. Theoretical analysis justifies that the induced preference signal by our method is order-consistent and concentrates on near-optimal candidates, supporting its stability for preference optimization. Experiments demonstrate that our method achieves consistently strong performance under a low-cost setting.

