---
layout: default
title: Certifiable Alignment of GNSS and Local Frames via Lagrangian Duality
---

# Certifiable Alignment of GNSS and Local Frames via Lagrangian Duality
**arXiv**：[2512.20931v1](https://arxiv.org/abs/2512.20931) · [PDF](https://arxiv.org/pdf/2512.20931.pdf)  
**作者**：Baoshan Song, Matthew Giamou, Penggao Yan, Chunxi Xia, Li-Ta Hsu  

**一句话要点**：提出基于拉格朗日对偶的全局最优GNSS与局部帧对齐方法，解决卫星受限环境下的可认证对齐问题。

**关键词**：GNSS对齐, 全局优化, 拉格朗日对偶, 可认证性, 卫星导航, 机器人定位

## 3 点简述
- 核心问题：GNSS与局部帧对齐易陷局部最优，依赖卫星可用性，现有方法在卫星受限时不可靠。
- 方法要点：将原始非凸QCQP问题松弛为凹拉格朗日对偶问题，提供全局最优解并支持可认证性验证。
- 实验效果：在仅2颗卫星和2D运动下仍能提供可认证最优解，优于传统方法，代码开源。

## 摘要（原文）

> Estimating the absolute orientation of a local system relative to a global navigation satellite system (GNSS) reference often suffers from local minima and high dependency on satellite availability. Existing methods for this alignment task rely on abundant satellites unavailable in GNSS-degraded environments, or use local optimization methods which cannot guarantee the optimality of a solution. This work introduces a globally optimal solver that transforms raw pseudo-range or Doppler measurements into a convexly relaxed problem. The proposed method is certifiable, meaning it can numerically verify the correctness of the result, filling a gap where existing local optimizers fail. We first formulate the original frame alignment problem as a nonconvex quadratically constrained quadratic program (QCQP) problem and relax the QCQP problem to a concave Lagrangian dual problem that provides a lower cost bound for the original problem. Then we perform relaxation tightness and observability analysis to derive criteria for certifiable optimality of the solution. Finally, simulation and real world experiments are conducted to evaluate the proposed method. The experiments show that our method provides certifiably optimal solutions even with only 2 satellites with Doppler measurements and 2D vehicle motion, while the traditional velocity-based VOBA method and the advanced GVINS alignment technique may fail or converge to local optima without notice. To support the development of GNSS-based navigation techniques in robotics, all code and data are open-sourced at https://github.com/Baoshan-Song/Certifiable-Doppler-alignment.

