---
layout: default
title: On the Feasibility and Opportunity of Autoregressive 3D Object Detection
---

# On the Feasibility and Opportunity of Autoregressive 3D Object Detection
**arXiv**：[2603.07985v1](https://arxiv.org/abs/2603.07985) · [PDF](https://arxiv.org/pdf/2603.07985.pdf)  
**作者**：Zanming Huang, Jinsu Yoo, Sooyoung Jeon, Zhenzhen Liu, Mark Campbell, Kilian Q Weinberger, Bharath Hariharan, Wei-Lun Chao, Katie Z Luo  

**一句话要点**：提出AutoReg3D，一种基于自回归序列生成的LiDAR 3D检测方法，以替代传统锚框和非极大值抑制。

**关键词**：自回归检测, 3D物体检测, LiDAR感知, 序列生成, 无锚框检测, 强化学习应用

## 3 点简述
- 核心问题：传统LiDAR检测器依赖锚框分配和非极大值抑制，训练复杂且扩展性受限。
- 方法要点：将检测建模为序列生成，按距离因果顺序输出对象，编码为离散令牌序列。
- 实验或效果：在nuScenes数据集上实现竞争性性能，无需锚框或NMS，并兼容多种点云骨干网络。

## 摘要（原文）

> LiDAR-based 3D object detectors typically rely on proposal heads with hand-crafted components like anchor assignment and non-maximum suppression (NMS), complicating training and limiting extensibility. We present AutoReg3D, an autoregressive 3D detector that casts detection as sequence generation. Given point-cloud features, AutoReg3D emits objects in a range-causal (near-to-far) order and encodes each object as a short, discrete-token sequence consisting of its center, size, orientation, velocity, and class. This near-to-far ordering mirrors LiDAR geometry--near objects occlude far ones but not vice versa--enabling straightforward teacher forcing during training and autoregressive decoding at test time. AutoReg3D is compatible across diverse point-cloud or backbones and attains competitive nuScenes performance without anchors or NMS. Beyond parity, the sequential formulation unlocks language-model advances for 3D perception, including GRPO-style reinforcement learning for task-aligned objectives. These results position autoregressive decoding as a viable, flexible alternative for LiDAR-based detection and open a path to importing modern sequence-modeling tools into 3D perception.

