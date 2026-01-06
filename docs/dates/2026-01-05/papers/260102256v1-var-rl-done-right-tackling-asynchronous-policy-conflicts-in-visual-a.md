---
layout: default
title: VAR RL Done Right: Tackling Asynchronous Policy Conflicts in Visual Autoregressive Generation
---

# VAR RL Done Right: Tackling Asynchronous Policy Conflicts in Visual Autoregressive Generation
**arXiv**：[2601.02256v1](https://arxiv.org/abs/2601.02256) · [PDF](https://arxiv.org/pdf/2601.02256.pdf)  
**作者**：Shikun Sun, Liao Qu, Huichao Zhang, Yiheng Liu, Yangyang Song, Xian Li, Xu Wang, Yi Jiang, Daniel K. Du, Xinglong Wu, Jia Jia  

**一句话要点**：提出增强GRPO的框架以解决视觉自回归生成中的异步策略冲突问题

**关键词**：视觉自回归生成, 异步策略冲突, 强化学习优化, GRPO增强, 掩码传播算法, 样本质量提升

## 3 点简述
- 核心问题：VAR模型在生成步骤中因输入结构异质导致异步策略冲突，尤其在强化学习场景下引发训练不稳定和对齐不佳
- 方法要点：集成稳定中间奖励、动态时间步重加权方案和基于ReFL的掩码传播算法，以管理冲突并优化策略
- 实验或效果：相比基础GRPO基线，在样本质量和目标对齐方面取得显著改进，实现VAR模型的稳健优化

## 摘要（原文）

> Visual generation is dominated by three paradigms: AutoRegressive (AR), diffusion, and Visual AutoRegressive (VAR) models. Unlike AR and diffusion, VARs operate on heterogeneous input structures across their generation steps, which creates severe asynchronous policy conflicts. This issue becomes particularly acute in reinforcement learning (RL) scenarios, leading to unstable training and suboptimal alignment. To resolve this, we propose a novel framework to enhance Group Relative Policy Optimization (GRPO) by explicitly managing these conflicts. Our method integrates three synergistic components: 1) a stabilizing intermediate reward to guide early-stage generation; 2) a dynamic time-step reweighting scheme for precise credit assignment; and 3) a novel mask propagation algorithm, derived from principles of Reward Feedback Learning (ReFL), designed to isolate optimization effects both spatially and temporally. Our approach demonstrates significant improvements in sample quality and objective alignment over the vanilla GRPO baseline, enabling robust and effective optimization for VAR models.

