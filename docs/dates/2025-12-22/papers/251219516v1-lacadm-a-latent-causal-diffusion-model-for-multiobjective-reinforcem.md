---
layout: default
title: LacaDM: A Latent Causal Diffusion Model for Multiobjective Reinforcement Learning
---

# LacaDM: A Latent Causal Diffusion Model for Multiobjective Reinforcement Learning
**arXiv**：[2512.19516v1](https://arxiv.org/abs/2512.19516) · [PDF](https://arxiv.org/pdf/2512.19516.pdf)  
**作者**：Xueming Yan, Bo Yin, Yaochu Jin  

**一句话要点**：提出LacaDM以增强多目标强化学习在动态环境中的适应性和泛化能力。

**关键词**：多目标强化学习, 潜在因果模型, 扩散模型, 泛化能力, 动态环境适应

## 3 点简述
- 核心问题：多目标强化学习存在目标冲突和动态环境适应困难，传统方法泛化能力不足。
- 方法要点：学习环境状态与策略间的潜在时序因果关系，结合扩散模型框架平衡目标冲突。
- 实验或效果：在MOGymnasium任务中，LacaDM在超体积、稀疏性和期望效用最大化方面优于基线方法。

## 摘要（原文）

> Multiobjective reinforcement learning (MORL) poses significant challenges due to the inherent conflicts between objectives and the difficulty of adapting to dynamic environments. Traditional methods often struggle to generalize effectively, particularly in large and complex state-action spaces. To address these limitations, we introduce the Latent Causal Diffusion Model (LacaDM), a novel approach designed to enhance the adaptability of MORL in discrete and continuous environments. Unlike existing methods that primarily address conflicts between objectives, LacaDM learns latent temporal causal relationships between environmental states and policies, enabling efficient knowledge transfer across diverse MORL scenarios. By embedding these causal structures within a diffusion model-based framework, LacaDM achieves a balance between conflicting objectives while maintaining strong generalization capabilities in previously unseen environments. Empirical evaluations on various tasks from the MOGymnasium framework demonstrate that LacaDM consistently outperforms the state-of-art baselines in terms of hypervolume, sparsity, and expected utility maximization, showcasing its effectiveness in complex multiobjective tasks.

