---
layout: default
title: STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models
---

# STARE-VLA: Progressive Stage-Aware Reinforcement for Fine-Tuning Vision-Language-Action Models
**arXiv**：[2512.05107v1](https://arxiv.org/abs/2512.05107) · [PDF](https://arxiv.org/pdf/2512.05107.pdf)  
**作者**：Feng Xu, Guangyao Zhai, Xin Kong, Tingzhong Fu, Daniel F. N. Gordon, Xueli An, Benjamin Busam  

**一句话要点**：提出STARE-VLA，通过阶段感知强化微调提升视觉-语言-动作模型的长时程动作准确性

**关键词**：视觉-语言-动作模型, 强化学习微调, 阶段感知优化, 长时程动作轨迹, 机器人操作, 离线与在线训练

## 3 点简述
- 现有VLA模型将长时程动作视为语言序列，导致信用分配粗糙和训练不稳定
- STARE模块将动作轨迹分解为语义阶段，提供密集、可解释的阶段对齐强化信号
- 在SimplerEnv和ManiSkill3实验中，达到98.0%和96.4%的成功率，实现SOTA性能

## 摘要（原文）

> Recent advances in Vision-Language-Action (VLA) models, powered by large language models and reinforcement learning-based fine-tuning, have shown remarkable progress in robotic manipulation. Existing methods often treat long-horizon actions as linguistic sequences and apply trajectory-level optimization methods such as Trajectory-wise Preference Optimization (TPO) or Proximal Policy Optimization (PPO), leading to coarse credit assignment and unstable training. However, unlike language, where a unified semantic meaning is preserved despite flexible sentence order, action trajectories progress through causally chained stages with different learning difficulties. This motivates progressive stage optimization. Thereby, we present Stage-Aware Reinforcement (STARE), a module that decomposes a long-horizon action trajectory into semantically meaningful stages and provides dense, interpretable, and stage-aligned reinforcement signals. Integrating STARE into TPO and PPO, we yield Stage-Aware TPO (STA-TPO) and Stage-Aware PPO (STA-PPO) for offline stage-wise preference and online intra-stage interaction, respectively. Further building on supervised fine-tuning as initialization, we propose the Imitation -> Preference -> Interaction (IPI), a serial fine-tuning pipeline for improving action accuracy in VLA models. Experiments on SimplerEnv and ManiSkill3 demonstrate substantial gains, achieving state-of-the-art success rates of 98.0 percent on SimplerEnv and 96.4 percent on ManiSkill3 tasks.

