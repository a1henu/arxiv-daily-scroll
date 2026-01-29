---
layout: default
title: DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment
---

# DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment
**arXiv**：[2601.20218v1](https://arxiv.org/abs/2601.20218) · [PDF](https://arxiv.org/pdf/2601.20218.pdf)  
**作者**：Haoyou Deng, Keyu Yan, Chaojie Mao, Xiang Wang, Yu Liu, Changxin Gao, Nong Sang  

**一句话要点**：提出DenseGRPO框架，通过密集奖励解决流匹配模型对齐中的稀疏奖励问题

**关键词**：流匹配模型, 奖励模型, 文本到图像生成, 密集奖励, 模型对齐, 去噪过程

## 3 点简述
- 核心问题：现有GRPO方法在文本到图像生成中面临稀疏奖励问题，全局反馈与中间步骤贡献不匹配
- 方法要点：预测每个去噪步骤的密集奖励，并基于奖励自适应调整探索空间
- 实验或效果：在多个标准基准上验证了有效性，强调密集奖励在模型对齐中的关键作用

## 摘要（原文）

> Recent GRPO-based approaches built on flow matching models have shown remarkable improvements in human preference alignment for text-to-image generation. Nevertheless, they still suffer from the sparse reward problem: the terminal reward of the entire denoising trajectory is applied to all intermediate steps, resulting in a mismatch between the global feedback signals and the exact fine-grained contributions at intermediate denoising steps. To address this issue, we introduce \textbf{DenseGRPO}, a novel framework that aligns human preference with dense rewards, which evaluates the fine-grained contribution of each denoising step. Specifically, our approach includes two key components: (1) we propose to predict the step-wise reward gain as dense reward of each denoising step, which applies a reward model on the intermediate clean images via an ODE-based approach. This manner ensures an alignment between feedback signals and the contributions of individual steps, facilitating effective training; and (2) based on the estimated dense rewards, a mismatch drawback between the uniform exploration setting and the time-varying noise intensity in existing GRPO-based methods is revealed, leading to an inappropriate exploration space. Thus, we propose a reward-aware scheme to calibrate the exploration space by adaptively adjusting a timestep-specific stochasticity injection in the SDE sampler, ensuring a suitable exploration space at all timesteps. Extensive experiments on multiple standard benchmarks demonstrate the effectiveness of the proposed DenseGRPO and highlight the critical role of the valid dense rewards in flow matching model alignment.

