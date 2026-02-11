---
layout: default
title: Quantum Multiple Rotation Averaging
---

# Quantum Multiple Rotation Averaging
**arXiv**：[2602.10115v1](https://arxiv.org/abs/2602.10115) · [PDF](https://arxiv.org/pdf/2602.10115.pdf)  
**作者**：Shuteng Wang, Natacha Kuete Meli, Michael Möller, Vladislav Golyanik  

**一句话要点**：提出IQARS算法，利用量子退火解决多旋转平均问题，提升高噪声场景精度。

**关键词**：多旋转平均, 量子退火, 旋转同步, 非凸优化, 3D视觉, 机器人学

## 3 点简述
- 多旋转平均是3D视觉与机器人中的基础优化问题，旨在从噪声相对测量恢复全局一致绝对旋转。
- IQARS将问题重构为局部二次非凸子问题，通过量子退火利用隧穿和并行性探索解空间，避免凸松弛依赖。
- 在合成与真实数据集上，IQARS在D-Wave退火器上比Shonan方法精度提升约12%，但当前硬件规模有限。

## 摘要（原文）

> Multiple rotation averaging (MRA) is a fundamental optimization problem in 3D vision and robotics that aims to recover globally consistent absolute rotations from noisy relative measurements. Established classical methods, such as L1-IRLS and Shonan, face limitations including local minima susceptibility and reliance on convex relaxations that fail to preserve the exact manifold geometry, leading to reduced accuracy in high-noise scenarios. We introduce IQARS (Iterative Quantum Annealing for Rotation Synchronization), the first algorithm that reformulates MRA as a sequence of local quadratic non-convex sub-problems executable on quantum annealers after binarization, to leverage inherent hardware advantages. IQARS removes convex relaxation dependence and better preserves non-Euclidean rotation manifold geometry while leveraging quantum tunneling and parallelism for efficient solution space exploration. We evaluate IQARS's performance on synthetic and real-world datasets. While current annealers remain in their nascent phase and only support solving problems of limited scale with constrained performance, we observed that IQARS on D-Wave annealers can already achieve ca. 12% higher accuracy than Shonan, i.e., the best-performing classical method evaluated empirically.

