---
layout: default
title: Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow
---

# Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow
**arXiv**：[2603.05448v1](https://arxiv.org/abs/2603.05448) · [PDF](https://arxiv.org/pdf/2603.05448.pdf)  
**作者**：Yanda Yang, Sambeeta Das  

**一句话要点**：提出结合MPC与SAC学习残差策略的混合控制器，以增强时变流下微机器人细胞推送的鲁棒性。

**关键词**：微机器人控制, 模型预测控制, 强化学习, 细胞推送, 时变流, 鲁棒性增强

## 3 点简述
- 核心问题：微流体流中接触式微操作易受扰动，导致推送接触中断和横向漂移。
- 方法要点：在名义MPC基础上，通过SAC训练有界速度校正的残差策略，仅在接触时应用以稳定学习。
- 实验或效果：在非平稳流下，相比纯MPC和PID，提高了鲁棒性和跟踪精度，并能泛化到未见轨迹。

## 摘要（原文）

> Contact-rich micromanipulation in microfluidic flow is challenging because small disturbances can break pushing contact and induce large lateral drift. We study planar cell pushing with a magnetic rolling microrobot that tracks a waypoint-sampled reference curve under time-varying Poiseuille flow. We propose a hybrid controller that augments a nominal MPC with a learned residual policy trained by SAC. The policy outputs a bounded 2D velocity correction that is contact-gated, so residual actions are applied only during robot--cell contact, preserving reliable approach behavior and stabilizing learning. All methods share the same actuation interface and speed envelope for fair comparisons. Experiments show improved robustness and tracking accuracy over pure MPC and PID under nonstationary flow, with generalization from a clover training curve to unseen circle and square trajectories. A residual-bound sweep identifies an intermediate correction limit as the best trade-off, which we use in all benchmarks.

