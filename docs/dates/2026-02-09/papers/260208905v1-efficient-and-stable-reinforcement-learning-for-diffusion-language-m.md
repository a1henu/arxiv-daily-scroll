---
layout: default
title: Efficient and Stable Reinforcement Learning for Diffusion Language Models
---

# Efficient and Stable Reinforcement Learning for Diffusion Language Models
**arXiv**：[2602.08905v1](https://arxiv.org/abs/2602.08905) · [PDF](https://arxiv.org/pdf/2602.08905.pdf)  
**作者**：Jiawei Liu, Xiting Wang, Yuanyuan Zhong, Defu Lian, Yu Yang  

**一句话要点**：提出时空剪枝框架以提升扩散语言模型强化学习的效率与稳定性

**关键词**：扩散语言模型, 强化学习, 时空剪枝, 效率优化, 稳定性提升

## 3 点简述
- 核心问题：扩散语言模型的强化学习面临效率低和稳定性差的挑战
- 方法要点：通过空间剪枝约束探索空间，时间剪枝跳过冗余步骤
- 实验或效果：理论分析证明降低方差，实验显示超越基线

## 摘要（原文）

> Reinforcement Learning (RL) is crucial for unlocking the complex reasoning capabilities of Diffusion-based Large Language Models (dLLMs). However, applying RL to dLLMs faces unique challenges in efficiency and stability. To address these challenges, we propose Spatio-Temporal Pruning (STP), a framework designed to simultaneously improve the efficiency and stability of RL for dLLMs. STP compresses the redundancy in the generative process through: (1) \textit{spatial pruning}, which constrains the exploration space using static priors; and (2) \textit{temporal pruning}, which bypasses redundant late-stage refinement steps. Our theoretical analysis demonstrates that STP strictly reduces the variance of the log-likelihood estimation, thereby ensuring more stable policy updates. Extensive experiments demonstrate that STP surpasses state-of-the-art baselines in both efficiency and accuracy. Our code is available at https://github.com/Lolo1222/STP.

