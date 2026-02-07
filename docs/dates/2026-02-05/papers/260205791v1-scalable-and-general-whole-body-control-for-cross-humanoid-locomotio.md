---
layout: default
title: Scalable and General Whole-Body Control for Cross-Humanoid Locomotion
---

# Scalable and General Whole-Body Control for Cross-Humanoid Locomotion
**arXiv**：[2602.05791v1](https://arxiv.org/abs/2602.05791) · [PDF](https://arxiv.org/pdf/2602.05791.pdf)  
**作者**：Yufei Xue, YunFeng Lin, Wentao Dong, Yang Tang, Jingbo Wang, Jiangmiao Pang, Ming Zhou, Minghuan Liu, Weinan Zhang  

**一句话要点**：提出XHugWBC框架以解决跨人形机器人通用全身控制问题

**关键词**：跨人形机器人控制, 全身控制, 形态随机化, 零样本迁移, 通用策略学习

## 3 点简述
- 核心问题：现有基于学习的全身控制器需针对特定机器人训练，缺乏跨机器人泛化能力。
- 方法要点：通过物理一致形态随机化、语义对齐观测动作空间及有效策略架构，实现一次性训练通用控制。
- 实验或效果：在12个模拟和7个真实人形机器人上验证，展示零样本迁移的强泛化性和鲁棒性。

## 摘要（原文）

> Learning-based whole-body controllers have become a key driver for humanoid robots, yet most existing approaches require robot-specific training. In this paper, we study the problem of cross-embodiment humanoid control and show that a single policy can robustly generalize across a wide range of humanoid robot designs with one-time training. We introduce XHugWBC, a novel cross-embodiment training framework that enables generalist humanoid control through: (1) physics-consistent morphological randomization, (2) semantically aligned observation and action spaces across diverse humanoid robots, and (3) effective policy architectures modeling morphological and dynamical properties. XHugWBC is not tied to any specific robot. Instead, it internalizes a broad distribution of morphological and dynamical characteristics during training. By learning motion priors from diverse randomized embodiments, the policy acquires a strong structural bias that supports zero-shot transfer to previously unseen robots. Experiments on twelve simulated humanoids and seven real-world robots demonstrate the strong generalization and robustness of the resulting universal controller.

