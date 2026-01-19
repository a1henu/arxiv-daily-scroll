---
layout: default
title: PhysRVG: Physics-Aware Unified Reinforcement Learning for Video Generative Models
---

# PhysRVG: Physics-Aware Unified Reinforcement Learning for Video Generative Models
**arXiv**：[2601.11087v1](https://arxiv.org/abs/2601.11087) · [PDF](https://arxiv.org/pdf/2601.11087.pdf)  
**作者**：Qiyuan Zhang, Biao Gong, Shuai Tan, Zheng Zhang, Yujun Shen, Xing Zhu, Yuyuan Li, Kelu Yao, Chunhua Shen, Changqing Zou  

**一句话要点**：提出物理感知强化学习范式PhysRVG，以解决视频生成中物理碰撞规则缺失的问题。

**关键词**：视频生成, 物理感知, 强化学习, 刚体运动, Transformer模型, 基准测试

## 3 点简述
- 核心问题：基于Transformer的视频生成忽略物理原理，导致刚体运动渲染不真实。
- 方法要点：引入物理感知强化学习，直接在像素空间强制执行碰撞规则，并扩展为Mimicry-Discovery Cycle统一框架。
- 实验或效果：构建PhysRVGBench基准，通过定性和定量实验验证方法的有效性。

## 摘要（原文）

> Physical principles are fundamental to realistic visual simulation, but remain a significant oversight in transformer-based video generation. This gap highlights a critical limitation in rendering rigid body motion, a core tenet of classical mechanics. While computer graphics and physics-based simulators can easily model such collisions using Newton formulas, modern pretrain-finetune paradigms discard the concept of object rigidity during pixel-level global denoising. Even perfectly correct mathematical constraints are treated as suboptimal solutions (i.e., conditions) during model optimization in post-training, fundamentally limiting the physical realism of generated videos. Motivated by these considerations, we introduce, for the first time, a physics-aware reinforcement learning paradigm for video generation models that enforces physical collision rules directly in high-dimensional spaces, ensuring the physics knowledge is strictly applied rather than treated as conditions. Subsequently, we extend this paradigm to a unified framework, termed Mimicry-Discovery Cycle (MDcycle), which allows substantial fine-tuning while fully preserving the model's ability to leverage physics-grounded feedback. To validate our approach, we construct new benchmark PhysRVGBench and perform extensive qualitative and quantitative experiments to thoroughly assess its effectiveness.

