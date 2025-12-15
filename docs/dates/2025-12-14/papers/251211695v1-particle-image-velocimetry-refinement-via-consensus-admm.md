---
layout: default
title: Particle Image Velocimetry Refinement via Consensus ADMM
---

# Particle Image Velocimetry Refinement via Consensus ADMM
**arXiv**：[2512.11695v1](https://arxiv.org/abs/2512.11695) · [PDF](https://arxiv.org/pdf/2512.11695.pdf)  
**作者**：Alan Bonomi, Francesco Banelli, Antonio Terpin  

**一句话要点**：提出基于共识ADMM的粒子图像测速优化方法，提升流体场量化精度与鲁棒性。

**关键词**：粒子图像测速, 交替方向乘子法, 流体场量化, 共识优化, 硬件加速, 主动流体控制

## 3 点简述
- 传统PIV方法依赖调参，性能易受成像条件影响，机器学习方法泛化性差。
- 采用多算法并行量化流场，结合ADMM共识框架融入平滑性和不可压缩性先验。
- 实验显示端点误差降低达20%，推理速率60Hz，集成于Flow Gym支持可复现比较。

## 摘要（原文）

> Particle Image Velocimetry (PIV) is an imaging technique in experimental fluid dynamics that quantifies flow fields around bluff bodies by analyzing the displacement of neutrally buoyant tracer particles immersed in the fluid. Traditional PIV approaches typically depend on tuning parameters specific to the imaging setup, making the performance sensitive to variations in illumination, flow conditions, and seeding density. On the other hand, even state-of-the-art machine learning methods for flow quantification are fragile outside their training set. In our experiments, we observed that flow quantification would improve if different tunings (or algorithms) were applied to different regions of the same image pair. In this work, we parallelize the instantaneous flow quantification with multiple algorithms and adopt a consensus framework based on the alternating direction method of multipliers, seamlessly incorporating priors such as smoothness and incompressibility. We perform several numerical experiments to demonstrate the benefits of this approach. For instance, we achieve a decrease in end-point-error of up to 20% of a dense-inverse-search estimator at an inference rate of 60Hz, and we show how this performance boost can be increased further with outlier rejection. Our method is implemented in JAX, effectively exploiting hardware acceleration, and integrated in Flow Gym, enabling (i) reproducible comparisons with the state-of-the-art, (ii) testing different base algorithms, (iii) straightforward deployment for active fluids control applications.

