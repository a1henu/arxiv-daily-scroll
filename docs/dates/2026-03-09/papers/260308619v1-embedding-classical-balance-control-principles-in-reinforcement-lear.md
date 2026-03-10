---
layout: default
title: Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
---

# Embedding Classical Balance Control Principles in Reinforcement Learning for Humanoid Recovery
**arXiv**：[2603.08619v1](https://arxiv.org/abs/2603.08619) · [PDF](https://arxiv.org/pdf/2603.08619.pdf)  
**作者**：Nehar Poddar, Stephen McCrory, Luigi Penco, Geoffrey Clark, Hakki Erhan Svil, Robert Griffin  

**一句话要点**：提出嵌入经典平衡指标的强化学习策略，以提升人形机器人自主恢复能力

**关键词**：人形机器人平衡控制, 强化学习策略, 模拟到硬件迁移, 自主恢复, 经典平衡指标嵌入

## 3 点简述
- 核心问题：人形机器人在非结构化环境中易跌倒且恢复困难，现有强化学习方法缺乏对平衡状态的显式建模
- 方法要点：在强化学习中嵌入捕获点、质心状态和质心动量作为特权批评输入，并围绕这些指标设计奖励，实现从模拟到硬件的零样本迁移
- 实验或效果：在Unitree H1-2上训练，恢复率达93.4%，消融实验显示平衡结构对学习至关重要，并展示了跨环境泛化能力

## 摘要（原文）

> Humanoid robots remain vulnerable to falls and unrecoverable failure states, limiting their practical utility in unstructured environments. While reinforcement learning has demonstrated stand-up behaviors, existing approaches treat recovery as a pure task-reward problem without an explicit representation of the balance state. We present a unified RL policy that addresses this limitation by embedding classical balance metrics: capture point, center-of-mass state, and centroidal momentum, as privileged critic inputs and shaping rewards directly around these quantities during training, while the actor relies solely on proprioception for zero-shot hardware transfer. Without reference trajectories or scripted contacts, a single policy spans the full recovery spectrum: ankle and hip strategies for small disturbances, corrective stepping under large pushes, and compliant falling with multi-contact stand-up using the hands, elbows, and knees. Trained on the Unitree H1-2 in Isaac Lab, the policy achieves a 93.4% recovery rate across randomized initial poses and unscripted fall configurations. An ablation study shows that removing the balance-informed structure causes stand-up learning to fail entirely, confirming that these metrics provide a meaningful learning signal rather than incidental structure. Sim-to-sim transfer to MuJoCo and preliminary hardware experiments further demonstrate cross-environment generalization. These results show that embedding interpretable balance structure into the learning framework substantially reduces time spent in failure states and broadens the envelope of autonomous recovery.

