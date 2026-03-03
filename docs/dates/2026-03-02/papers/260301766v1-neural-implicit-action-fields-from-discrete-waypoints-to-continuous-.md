---
layout: default
title: Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models
---

# Neural Implicit Action Fields: From Discrete Waypoints to Continuous Functions for Vision-Language-Action Models
**arXiv**：[2603.01766v1](https://arxiv.org/abs/2603.01766) · [PDF](https://arxiv.org/pdf/2603.01766.pdf)  
**作者**：Haoyun Liu, Jianzhuang Zhao, Xinyuan Chang, Tianle Shi, Chuanzhang Meng, Jiayuan Tan, Feng Xiong, Tong Lin, Dongjie Huo, Mu Xu, SongLin Dong, Zhiheng Ma, Yihong Gong, Sheng Zhong  

**一句话要点**：提出神经隐式动作场以解决视觉-语言-动作模型中离散路径点预测与物理运动连续性不匹配的问题

**关键词**：神经隐式动作场, 连续动作函数回归, 视觉-语言-动作模型, 阻抗控制, 轨迹合成

## 3 点简述
- 核心问题：离散路径点预测导致采样率固定、缺乏高阶可微性，阻碍精确交互
- 方法要点：将动作预测重构为连续动作函数回归，利用MLLM作为分层谱调制器
- 实验或效果：在CALVIN和LIBERO基准上取得先进结果，支持稳定阻抗控制

## 摘要（原文）

> Despite the rapid progress of Vision-Language-Action (VLA) models, the prevailing paradigm of predicting discrete waypoints remains fundamentally misaligned with the intrinsic continuity of physical motion. This discretization imposes rigid sampling rates, lacks high-order differentiability, and introduces quantization artifacts that hinder precise, compliant interaction. We propose Neural Implicit Action Fields (NIAF), a paradigm shift that reformulates action prediction from discrete waypoints to continuous action function regression. By utilizing an MLLM as a hierarchical spectral modulator over a learnable motion prior, NIAF synthesizes infinite-resolution trajectories as continuous-time manifolds. This formulation enables analytical differentiability, allowing for explicit supervision of velocity, acceleration, and jerk to ensure mathematical consistency and physical plausibility. Our approach achieves state-of-the-art results on CALVIN and LIBERO benchmarks across diverse backbones. Furthermore, real-world experiments demonstrate that NIAF enables stable impedance control, bridging the gap between high-level semantic understanding and low-level dynamic execution.

