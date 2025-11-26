---
layout: default
title: BRIC: Bridging Kinematic Plans and Physical Control at Test Time
---

# BRIC: Bridging Kinematic Plans and Physical Control at Test Time
**arXiv**：[2511.20431v1](https://arxiv.org/abs/2511.20431) · [PDF](https://arxiv.org/pdf/2511.20431.pdf)  
**作者**：Dohun Lim, Minji Kim, Jaewoon Lim, Sungchan Kim  

**一句话要点**：提出BRIC框架以解决运动规划与物理控制间的执行差异

**关键词**：测试时适应, 运动生成, 物理控制, 扩散模型, 强化学习

## 3 点简述
- 核心问题：扩散模型生成的运动计划在物理模拟中常不真实，导致执行漂移
- 方法要点：动态适应物理控制器并引入轻量级测试时引导机制
- 实验或效果：在多种长期任务中实现最先进性能，验证一致性与物理合理性

## 摘要（原文）

> We propose BRIC, a novel test-time adaptation (TTA) framework that enables long-term human motion generation by resolving execution discrepancies between diffusion-based kinematic motion planners and reinforcement learning-based physics controllers. While diffusion models can generate diverse and expressive motions conditioned on text and scene context, they often produce physically implausible outputs, leading to execution drift during simulation. To address this, BRIC dynamically adapts the physics controller to noisy motion plans at test time, while preserving pre-trained skills via a loss function that mitigates catastrophic forgetting. In addition, BRIC introduces a lightweight test-time guidance mechanism that steers the diffusion model in the signal space without updating its parameters. By combining both adaptation strategies, BRIC ensures consistent and physically plausible long-term executions across diverse environments in an effective and efficient manner. We validate the effectiveness of BRIC on a variety of long-term tasks, including motion composition, obstacle avoidance, and human-scene interaction, achieving state-of-the-art performance across all tasks.

