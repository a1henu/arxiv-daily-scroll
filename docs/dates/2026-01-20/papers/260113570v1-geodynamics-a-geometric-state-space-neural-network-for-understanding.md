---
layout: default
title: GeoDynamics: A Geometric State-Space Neural Network for Understanding Brain Dynamics on Riemannian Manifolds
---

# GeoDynamics: A Geometric State-Space Neural Network for Understanding Brain Dynamics on Riemannian Manifolds
**arXiv**：[2601.13570v1](https://arxiv.org/abs/2601.13570) · [PDF](https://arxiv.org/pdf/2601.13570.pdf)  
**作者**：Tingting Dan, Jiaqi Ding, Guorong Wu  

**一句话要点**：提出GeoDynamics几何状态空间神经网络，在黎曼流形上建模大脑动态以理解认知与疾病。

**关键词**：黎曼流形建模, 状态空间神经网络, 大脑动态分析, 对称正定矩阵, 动作识别, 神经疾病标记

## 3 点简述
- 核心问题：现有方法将大脑视为松散区域或简化网络，未基于黎曼流形捕捉功能连接矩阵的动态轨迹。
- 方法要点：在对称正定流形上嵌入状态空间模型，学习几何感知的递归过渡，跟踪潜在脑状态轨迹。
- 实验或效果：验证于神经科学任务和动作识别基准，揭示任务驱动状态变化及阿尔茨海默病等早期标记。

## 摘要（原文）

> State-space models (SSMs) have become a cornerstone for unraveling brain dynamics, revealing how latent neural states evolve over time and give rise to observed signals. By combining the flexibility of deep learning with the principled dynamical structure of SSMs, recent studies have achieved powerful fits to functional neuroimaging data. However, most existing approaches still view the brain as a set of loosely connected regions or impose oversimplified network priors, falling short of a truly holistic and self-organized dynamical system perspective. Brain functional connectivity (FC) at each time point naturally forms a symmetric positive definite (SPD) matrix, which resides on a curved Riemannian manifold rather than in Euclidean space. Capturing the trajectories of these SPD matrices is key to understanding how coordinated networks support cognition and behavior. To this end, we introduce GeoDynamics, a geometric state-space neural network that tracks latent brain-state trajectories directly on the high-dimensional SPD manifold. GeoDynamics embeds each connectivity matrix into a manifold-aware recurrent framework, learning smooth and geometry-respecting transitions that reveal task-driven state changes and early markers of Alzheimer's disease, Parkinson's disease, and autism. Beyond neuroscience, we validate GeoDynamics on human action recognition benchmarks (UTKinect, Florence, HDM05), demonstrating its scalability and robustness in modeling complex spatiotemporal dynamics across diverse domains.

