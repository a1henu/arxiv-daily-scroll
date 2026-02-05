---
layout: default
title: HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation
---

# HoRD: Robust Humanoid Control via History-Conditioned Reinforcement Learning and Online Distillation
**arXiv**：[2602.04412v1](https://arxiv.org/abs/2602.04412) · [PDF](https://arxiv.org/pdf/2602.04412.pdf)  
**作者**：Puyue Wang, Jiawei Hu, Yan Gao, Junyan Wang, Yu Zhang, Gillian Dobbie, Tao Gu, Wafa Johal, Ting Dang, Hong Jia  

**一句话要点**：提出HoRD框架，通过历史条件强化学习和在线蒸馏实现人形机器人在域转移下的鲁棒控制。

**关键词**：人形机器人控制, 强化学习, 在线蒸馏, 域适应, Transformer, 鲁棒性

## 3 点简述
- 核心问题：人形机器人在动态、任务或环境微小变化下性能显著下降。
- 方法要点：两阶段学习，先训练历史条件教师策略在线适应动态，再通过在线蒸馏将能力转移至基于Transformer的学生策略。
- 实验或效果：在未见域和外部扰动下，HoRD在鲁棒性和迁移性上优于基线方法。

## 摘要（原文）

> Humanoid robots can suffer significant performance drops under small changes in dynamics, task specifications, or environment setup. We propose HoRD, a two-stage learning framework for robust humanoid control under domain shift. First, we train a high-performance teacher policy via history-conditioned reinforcement learning, where the policy infers latent dynamics context from recent state--action trajectories to adapt online to diverse randomized dynamics. Second, we perform online distillation to transfer the teacher's robust control capabilities into a transformer-based student policy that operates on sparse root-relative 3D joint keypoint trajectories. By combining history-conditioned adaptation with online distillation, HoRD enables a single policy to adapt zero-shot to unseen domains without per-domain retraining. Extensive experiments show HoRD outperforms strong baselines in robustness and transfer, especially under unseen domains and external perturbations. Code and project page are available at \href{https://tonywang-0517.github.io/hord/}{https://tonywang-0517.github.io/hord/}.

