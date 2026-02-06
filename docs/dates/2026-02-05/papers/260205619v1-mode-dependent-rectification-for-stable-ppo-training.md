---
layout: default
title: Mode-Dependent Rectification for Stable PPO Training
---

# Mode-Dependent Rectification for Stable PPO Training
**arXiv**：[2602.05619v1](https://arxiv.org/abs/2602.05619) · [PDF](https://arxiv.org/pdf/2602.05619.pdf)  
**作者**：Mohamad Mohamad, Francesco Ponzio, Xavier Descombes  

**一句话要点**：提出模式依赖校正以稳定PPO训练，解决批归一化等层导致的策略失配问题。

**关键词**：强化学习, PPO训练, 模式依赖层, 批归一化, 稳定性优化, 策略失配

## 3 点简述
- 核心问题：批归一化等模式依赖层在训练与评估时行为差异，导致PPO策略失配、分布漂移和奖励崩溃。
- 方法要点：提出轻量级双阶段训练过程MDR，无需架构修改，稳定PPO在模式依赖层下的优化。
- 实验或效果：在程序生成游戏和真实世界补丁定位任务中，MDR一致提升稳定性和性能，并扩展至其他模式依赖层。

## 摘要（原文）

> Mode-dependent architectural components (layers that behave differently during training and evaluation, such as Batch Normalization or dropout) are commonly used in visual reinforcement learning but can destabilize on-policy optimization. We show that in Proximal Policy Optimization (PPO), discrepancies between training and evaluation behavior induced by Batch Normalization lead to policy mismatch, distributional drift, and reward collapse. We propose Mode-Dependent Rectification (MDR), a lightweight dual-phase training procedure that stabilizes PPO under mode-dependent layers without architectural changes. Experiments across procedurally generated games and real-world patch-localization tasks demonstrate that MDR consistently improves stability and performance, and extends naturally to other mode-dependent layers.

