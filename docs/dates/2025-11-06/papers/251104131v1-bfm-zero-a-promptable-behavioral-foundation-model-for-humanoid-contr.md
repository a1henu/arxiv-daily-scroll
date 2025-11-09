---
layout: default
title: BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning
---

# BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning
**arXiv**：[2511.04131v1](https://arxiv.org/abs/2511.04131) · [PDF](https://arxiv.org/pdf/2511.04131.pdf)  
**作者**：Yitang Li, Zhengyi Luo, Tonghe Zhang, Cunxi Dai, Anssi Kanervisto, Andrea Tirinzoni, Haoyang Weng, Kris Kitani, Mateusz Guzek, Ahmed Touati, Alessandro Lazaric, Matteo Pirotta, Guanya Shi  

**一句话要点**：提出BFM-Zero框架，通过无监督强化学习实现人形机器人可提示行为基础模型

**关键词**：行为基础模型, 无监督强化学习, 人形机器人控制, 潜在表示学习, 零样本推理, 模拟到真实迁移

## 3 点简述
- 核心问题：现有方法局限于模拟环境或特定任务，难以统一人形机器人控制
- 方法要点：学习共享潜在表示，嵌入动作、目标和奖励，支持零样本和少样本推理
- 实验或效果：在真实Unitree G1机器人上实现多任务控制，并通过消融实验验证设计

## 摘要（原文）

> Building Behavioral Foundation Models (BFMs) for humanoid robots has the
> potential to unify diverse control tasks under a single, promptable generalist
> policy. However, existing approaches are either exclusively deployed on
> simulated humanoid characters, or specialized to specific tasks such as
> tracking. We propose BFM-Zero, a framework that learns an effective shared
> latent representation that embeds motions, goals, and rewards into a common
> space, enabling a single policy to be prompted for multiple downstream tasks
> without retraining. This well-structured latent space in BFM-Zero enables
> versatile and robust whole-body skills on a Unitree G1 humanoid in the real
> world, via diverse inference methods, including zero-shot motion tracking, goal
> reaching, and reward optimization, and few-shot optimization-based adaptation.
> Unlike prior on-policy reinforcement learning (RL) frameworks, BFM-Zero builds
> upon recent advancements in unsupervised RL and Forward-Backward (FB) models,
> which offer an objective-centric, explainable, and smooth latent representation
> of whole-body motions. We further extend BFM-Zero with critical reward shaping,
> domain randomization, and history-dependent asymmetric learning to bridge the
> sim-to-real gap. Those key design choices are quantitatively ablated in
> simulation. A first-of-its-kind model, BFM-Zero establishes a step toward
> scalable, promptable behavioral foundation models for whole-body humanoid
> control.

