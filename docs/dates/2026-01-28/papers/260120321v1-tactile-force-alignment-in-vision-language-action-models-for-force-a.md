---
layout: default
title: Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation
---

# Tactile-Force Alignment in Vision-Language-Action Models for Force-aware Manipulation
**arXiv**：[2601.20321v1](https://arxiv.org/abs/2601.20321) · [PDF](https://arxiv.org/pdf/2601.20321.pdf)  
**作者**：Yuzhe Huang, Pei Lin, Wanlin Li, Daohan Li, Jiajun Li, Jiaming Jiang, Chenxi Xiao, Ziyuan Jiao  

**一句话要点**：提出TaF-VLA框架，通过触觉-力对齐实现接触密集任务的力感知操作

**关键词**：触觉-力对齐, 视觉-语言-动作模型, 力感知操作, 触觉传感器编码, 物理推理, 机器人操作

## 3 点简述
- 核心问题：现有视觉-语言-动作模型依赖视觉模态，缺乏接触密集任务所需的力调节和物理直觉
- 方法要点：开发触觉-力适配器，将触觉观测与物理力对齐，并构建TaF-Dataset支持训练
- 实验或效果：在真实世界实验中，TaF-VLA策略显著优于触觉-视觉对齐和仅视觉基线

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently emerged as powerful generalists for robotic manipulation. However, due to their predominant reliance on visual modalities, they fundamentally lack the physical intuition required for contact-rich tasks that require precise force regulation and physical reasoning. Existing attempts to incorporate vision-based tactile sensing into VLA models typically treat tactile inputs as auxiliary visual textures, thereby overlooking the underlying correlation between surface deformation and interaction dynamics. To bridge this gap, we propose a paradigm shift from tactile-vision alignment to tactile-force alignment. Here, we introduce TaF-VLA, a framework that explicitly grounds high-dimensional tactile observations in physical interaction forces. To facilitate this, we develop an automated tactile-force data acquisition device and curate the TaF-Dataset, comprising over 10 million synchronized tactile observations, 6-axis force/torque, and matrix force map. To align sequential tactile observations with interaction forces, the central component of our approach is the Tactile-Force Adapter (TaF-Adapter), a tactile sensor encoder that extracts discretized latent information for encoding tactile observations. This mechanism ensures that the learned representations capture history-dependent, noise-insensitive physical dynamics rather than static visual textures. Finally, we integrate this force-aligned encoder into a VLA backbone. Extensive real-world experiments demonstrate that TaF-VLA policy significantly outperforms state-of-the-art tactile-vision-aligned and vision-only baselines on contact-rich tasks, verifying its ability to achieve robust, force-aware manipulation through cross-modal physical reasoning.

