---
layout: default
title: From Pairs to Sequences: Track-Aware Policy Gradients for Keypoint Detection
---

# From Pairs to Sequences: Track-Aware Policy Gradients for Keypoint Detection
**arXiv**：[2602.20630v1](https://arxiv.org/abs/2602.20630) · [PDF](https://arxiv.org/pdf/2602.20630.pdf)  
**作者**：Yepeng Liu, Hao Li, Liwen Yang, Fangzhen Li, Xudi Ge, Yuliang Gu, kuang Gao, Bing Wang, Guang Chen, Hangjun Ye, Yongchao Xu  

**一句话要点**：提出TraqPoint强化学习框架，通过序列决策优化关键点跟踪质量，提升3D视觉系统性能。

**关键词**：关键点检测, 强化学习, 序列决策, 轨迹感知奖励, 3D视觉系统, 稀疏匹配

## 3 点简述
- 核心问题：现有基于图像对的关键点检测方法未显式优化序列中的长期可跟踪性，难以应对视角和光照变化。
- 方法要点：引入轨迹感知奖励机制，结合策略梯度方法，联合优化关键点跨多视图的一致性和独特性。
- 实验或效果：在稀疏匹配基准测试中，包括相对姿态估计和3D重建，TraqPoint显著优于一些最先进方法。

## 摘要（原文）

> Keypoint-based matching is a fundamental component of modern 3D vision systems, such as Structure-from-Motion (SfM) and SLAM. Most existing learning-based methods are trained on image pairs, a paradigm that fails to explicitly optimize for the long-term trackability of keypoints across sequences under challenging viewpoint and illumination changes. In this paper, we reframe keypoint detection as a sequential decision-making problem. We introduce TraqPoint, a novel, end-to-end Reinforcement Learning (RL) framework designed to optimize the \textbf{Tra}ck-\textbf{q}uality (Traq) of keypoints directly on image sequences. Our core innovation is a track-aware reward mechanism that jointly encourages the consistency and distinctiveness of keypoints across multiple views, guided by a policy gradient method. Extensive evaluations on sparse matching benchmarks, including relative pose estimation and 3D reconstruction, demonstrate that TraqPoint significantly outperforms some state-of-the-art (SOTA) keypoint detection and description methods.

