---
layout: default
title: $π$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs
---

# $π$-StepNFT: Wider Space Needs Finer Steps in Online RL for Flow-based VLAs
**arXiv**：[2603.02083v1](https://arxiv.org/abs/2603.02083) · [PDF](https://arxiv.org/pdf/2603.02083.pdf)  
**作者**：Siting Wang, Xiaofeng Wang, Zheng Zhu, Minnan Pei, Xinyu Cui, Cheng Deng, Jian Zhao, Guan Huang, Haifeng Zhang, Jun Wang  

**一句话要点**：提出π-StepNFT框架，以解决基于流的VLA模型在线强化学习中多步采样的似然计算难题。

**关键词**：在线强化学习, 基于流的VLA模型, 多步采样, 似然计算, 泛化性能, 少样本学习

## 3 点简述
- 核心问题：基于流的VLA模型在在线强化学习中面临多步采样时似然计算不可行的问题。
- 方法要点：π-StepNFT是无评论家和似然的框架，每优化步仅需单次前向传播，无需辅助价值网络。
- 实验或效果：在LIBERO上展现少样本鲁棒性，在ManiSkill上优于基于价值的方法，防止对多模态特征的过拟合。

## 摘要（原文）

> Flow-based vision-language-action (VLA) models excel in embodied control but suffer from intractable likelihoods during multi-step sampling, hindering online reinforcement learning. We propose \textbf{\textit{$\boldsymbolπ$-StepNFT}} (Step-wise Negative-aware Fine-Tuning), a critic-and-likelihood-free framework that requires only a single forward pass per optimization step and eliminates auxiliary value networks. We identify that wider exploration spaces necessitate finer-grained, step-wise guidance for alignment. Empirically, $π$-StepNFT unlocks latent potential on LIBERO with competitive few-shot robustness. Moreover, it achieves superior generalization on ManiSkill, outperforming value-based baselines in OOD scenarios by preventing overfitting to multimodal features. This property offers a scalable solution promising for complex real-world applications.

