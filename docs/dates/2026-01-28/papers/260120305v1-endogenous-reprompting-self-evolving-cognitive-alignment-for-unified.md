---
layout: default
title: Endogenous Reprompting: Self-Evolving Cognitive Alignment for Unified Multimodal Models
---

# Endogenous Reprompting: Self-Evolving Cognitive Alignment for Unified Multimodal Models
**arXiv**：[2601.20305v1](https://arxiv.org/abs/2601.20305) · [PDF](https://arxiv.org/pdf/2601.20305.pdf)  
**作者**：Zhenchen Tang, Songlin Yang, Zichuan Wang, Bo Peng, Yang Li, Beibei Dong, Jing Dong  

**一句话要点**：提出内源性重提示机制以解决统一多模态模型中的认知差距问题

**关键词**：统一多模态模型, 认知对齐, 内源性重提示, 强化学习, 视觉指令细化

## 3 点简述
- 核心问题：统一多模态模型存在认知差距，理解能力无法有效指导生成过程
- 方法要点：通过SEER框架建立两阶段内源性循环，利用强化学习优化生成推理策略
- 实验或效果：SEER在评估准确性、重提示效率和生成质量上优于基线，不牺牲通用能力

## 摘要（原文）

> Unified Multimodal Models (UMMs) exhibit strong understanding, yet this capability often fails to effectively guide generation. We identify this as a Cognitive Gap: the model lacks the understanding of how to enhance its own generation process. To bridge this gap, we propose Endogenous Reprompting, a mechanism that transforms the model's understanding from a passive encoding process into an explicit generative reasoning step by generating self-aligned descriptors during generation. To achieve this, we introduce SEER (Self-Evolving Evaluator and Reprompter), a training framework that establishes a two-stage endogenous loop using only 300 samples from a compact proxy task, Visual Instruction Elaboration. First, Reinforcement Learning with Verifiable Rewards (RLVR) activates the model's latent evaluation ability via curriculum learning, producing a high-fidelity endogenous reward signal. Second, Reinforcement Learning with Model-rewarded Thinking (RLMT) leverages this signal to optimize the generative reasoning policy. Experiments show that SEER consistently outperforms state-of-the-art baselines in evaluation accuracy, reprompting efficiency, and generation quality, without sacrificing general multimodal capabilities.

