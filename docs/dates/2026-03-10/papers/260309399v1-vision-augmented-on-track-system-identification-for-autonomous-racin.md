---
layout: default
title: Vision-Augmented On-Track System Identification for Autonomous Racing via Attention-Based Priors and Iterative Neural Correction
---

# Vision-Augmented On-Track System Identification for Autonomous Racing via Attention-Based Priors and Iterative Neural Correction
**arXiv**：[2603.09399v1](https://arxiv.org/abs/2603.09399) · [PDF](https://arxiv.org/pdf/2603.09399.pdf)  
**作者**：Zhiping Wu, Cheng Hu, Yiqin Wang, Lei Xie, Hongye Su  

**一句话要点**：提出视觉增强的迭代系统识别框架，以解决自动驾驶赛车在极限操控下的非线性轮胎动力学建模问题。

**关键词**：自动驾驶赛车, 系统识别, 视觉先验, S4模型, 轮胎动力学, 迭代优化

## 3 点简述
- 核心问题：传统在线优化方法存在冷启动失败和高频瞬态动力学建模困难。
- 方法要点：结合视觉先验、S4模型和迭代优化，实现轻量级、高精度的轮胎参数提取。
- 实验或效果：在CarSim中，摩擦估计误差降低76.1%，收敛速度提升71.4%，侧向力RMSE减少超60%。

## 摘要（原文）

> Operating autonomous vehicles at the absolute limits of handling requires precise, real-time identification of highly non-linear tire dynamics. However, traditional online optimization methods suffer from "cold-start" initialization failures and struggle to model high-frequency transient dynamics. To address these bottlenecks, this paper proposes a novel vision-augmented, iterative system identification framework. First, a lightweight CNN (MobileNetV3) translates visual road textures into a continuous heuristic friction prior, providing a robust "warm-start" for parameter optimization. Next, a S4 model captures complex temporal dynamic residuals, circumventing the memory and latency limitations of traditional MLPs and RNNs. Finally, a derivative-free Nelder-Mead algorithm iteratively extracts physically interpretable Pacejka tire parameters via a hybrid virtual simulation. Co-simulation in CarSim demonstrates that the lightweight vision backbone reduces friction estimation error by 76.1 using 85 fewer FLOPs, accelerating cold-start convergence by 71.4. Furthermore, the S4-augmented framework improves parameter extraction accuracy and decreases lateral force RMSE by over 60 by effectively capturing complex vehicle dynamics, demonstrating superior performance compared to conventional neural architectures.

