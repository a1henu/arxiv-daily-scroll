---
layout: default
title: Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks
---

# Beyond Short-Horizon: VQ-Memory for Robust Long-Horizon Manipulation in Non-Markovian Simulation Benchmarks
**arXiv**：[2603.09513v1](https://arxiv.org/abs/2603.09513) · [PDF](https://arxiv.org/pdf/2603.09513.pdf)  
**作者**：Wang Honghui, Jing Zhi, Ao Jicong, Song Shiji, Li Xuelong, Huang Gao, Bai Chenjia  

**一句话要点**：提出VQ-Memory以解决非马尔可夫长时程操作中的鲁棒性问题

**关键词**：长时程操作, 非马尔可夫基准, 向量量化自编码器, 时序表示, 机器人仿真, 视觉语言动作模型

## 3 点简述
- 问题：现有基准集中于简单操作，缺乏非马尔可夫特性和复杂关节物体交互的建模。
- 方法：引入RuleSafe基准和VQ-Memory，使用VQ-VAE编码历史状态为离散令牌，提供结构化时序表示。
- 效果：VQ-Memory提升长时程规划、泛化能力和操作效率，在VLA模型和扩散策略中验证有效。

## 摘要（原文）

> The high cost of collecting real-robot data has made robotic simulation a scalable platform for both evaluation and data generation. Yet most existing benchmarks concentrate on simple manipulation tasks such as pick-and-place, failing to capture the non-Markovian characteristics of real-world tasks and the complexity of articulated object interactions. To address this limitation, we present RuleSafe, a new articulated manipulation benchmark built upon a scalable LLM-aided simulation framework. RuleSafe features safes with diverse unlocking mechanisms, such as key locks, password locks, and logic locks, which require different multi-stage reasoning and manipulation strategies. These LLM-generated rules produce non-Markovian and long-horizon tasks that require temporal modeling and memory-based reasoning. We further propose VQ-Memory, a compact and structured temporal representation that uses vector-quantized variational autoencoders (VQ-VAEs) to encode past proprioceptive states into discrete latent tokens. This representation filters low-level noise while preserving high-level task-phase context, providing lightweight yet robust temporal cues that are compatible with existing Vision-Language-Action models (VLA). Extensive experiments on state-of-the-art VLA models and diffusion policies show that VQ-Memory consistently improves long-horizon planning, enhances generalization to unseen configurations, and enables more efficient manipulation with reduced computational cost. Project page: vqmemory.github.io

