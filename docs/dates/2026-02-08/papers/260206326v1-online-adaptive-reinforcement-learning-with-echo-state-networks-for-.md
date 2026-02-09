---
layout: default
title: Online Adaptive Reinforcement Learning with Echo State Networks for Non-Stationary Dynamics
---

# Online Adaptive Reinforcement Learning with Echo State Networks for Non-Stationary Dynamics
**arXiv**：[2602.06326v1](https://arxiv.org/abs/2602.06326) · [PDF](https://arxiv.org/pdf/2602.06326.pdf)  
**作者**：Aoi Yoshimura, Gouhei Tanaka  

**一句话要点**：提出基于回声状态网络的在线自适应强化学习框架以应对非平稳动态环境

**关键词**：在线自适应强化学习, 回声状态网络, 非平稳动态环境, 递归最小二乘法, 轻量级适应框架

## 3 点简述
- 核心问题：强化学习在非平稳动态环境中部署时性能下降，现有方法依赖预训练或高计算成本
- 方法要点：集成回声状态网络作为适应模块，使用递归最小二乘法在线更新权重，无需反向传播或特权信息
- 实验或效果：在CartPole和HalfCheetah任务中显著优于域随机化和自适应基线，实现快速稳定适应

## 摘要（原文）

> Reinforcement learning (RL) policies trained in simulation often suffer from severe performance degradation when deployed in real-world environments due to non-stationary dynamics. While Domain Randomization (DR) and meta-RL have been proposed to address this issue, they typically rely on extensive pretraining, privileged information, or high computational cost, limiting their applicability to real-time and edge systems. In this paper, we propose a lightweight online adaptation framework for RL based on Reservoir Computing. Specifically, we integrate an Echo State Networks (ESNs) as an adaptation module that encodes recent observation histories into a latent context representation, and update its readout weights online using Recursive Least Squares (RLS). This design enables rapid adaptation without backpropagation, pretraining, or access to privileged information. We evaluate the proposed method on CartPole and HalfCheetah tasks with severe and abrupt environment changes, including periodic external disturbances and extreme friction variations. Experimental results demonstrate that the proposed approach significantly outperforms DR and representative adaptive baselines under out-of-distribution dynamics, achieving stable adaptation within a few control steps. Notably, the method successfully handles intra-episode environment changes without resetting the policy. Due to its computational efficiency and stability, the proposed framework provides a practical solution for online adaptation in non-stationary environments and is well suited for real-world robotic control and edge deployment.

