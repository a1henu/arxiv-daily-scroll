---
layout: default
title: MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction
---

# MeshMimic: Geometry-Aware Humanoid Motion Learning through 3D Scene Reconstruction
**arXiv**：[2602.15733v1](https://arxiv.org/abs/2602.15733) · [PDF](https://arxiv.org/pdf/2602.15733.pdf)  
**作者**：Qiang Zhang, Jiahao Ma, Peiran Liu, Shuai Shi, Zeran Su, Zifan Wang, Jingkai Sun, Wei Cui, Jialin Yu, Gang Han, Wen Zhao, Pihai Sun, Kangning Yin, Jiaxu Wang, Jiahang Cao, Lingfeng Zhang, Hao Cheng, Xiaoshuai Hao, Yiding Ji, Junwei Liang, Jian Tang, Renjing Xu, Yijie Guo  

**一句话要点**：提出MeshMimic框架，通过3D场景重建实现人形机器人从视频学习运动-地形交互

**关键词**：人形机器人运动控制, 3D场景重建, 强化学习, 运动-地形交互, 视觉感知, 物理仿真

## 3 点简述
- 核心问题：现有运动合成框架依赖昂贵动捕数据，缺乏场景几何信息，导致运动与地形解耦，产生物理不一致性。
- 方法要点：利用先进3D视觉模型重建场景几何和人体轨迹，通过优化算法提取高质量运动数据，并引入接触不变重定向方法。
- 实验或效果：在多样挑战性地形上实现鲁棒、高动态性能，证明低成本单目传感器可训练复杂物理交互。

## 摘要（原文）

> Humanoid motion control has witnessed significant breakthroughs in recent years, with deep reinforcement learning (RL) emerging as a primary catalyst for achieving complex, human-like behaviors. However, the high dimensionality and intricate dynamics of humanoid robots make manual motion design impractical, leading to a heavy reliance on expensive motion capture (MoCap) data. These datasets are not only costly to acquire but also frequently lack the necessary geometric context of the surrounding physical environment. Consequently, existing motion synthesis frameworks often suffer from a decoupling of motion and scene, resulting in physical inconsistencies such as contact slippage or mesh penetration during terrain-aware tasks. In this work, we present MeshMimic, an innovative framework that bridges 3D scene reconstruction and embodied intelligence to enable humanoid robots to learn coupled "motion-terrain" interactions directly from video. By leveraging state-of-the-art 3D vision models, our framework precisely segments and reconstructs both human trajectories and the underlying 3D geometry of terrains and objects. We introduce an optimization algorithm based on kinematic consistency to extract high-quality motion data from noisy visual reconstructions, alongside a contact-invariant retargeting method that transfers human-environment interaction features to the humanoid agent. Experimental results demonstrate that MeshMimic achieves robust, highly dynamic performance across diverse and challenging terrains. Our approach proves that a low-cost pipeline utilizing only consumer-grade monocular sensors can facilitate the training of complex physical interactions, offering a scalable path toward the autonomous evolution of humanoid robots in unstructured environments.

