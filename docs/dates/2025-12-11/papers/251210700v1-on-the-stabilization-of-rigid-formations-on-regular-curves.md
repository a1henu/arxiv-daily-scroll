---
layout: default
title: On the Stabilization of Rigid Formations on Regular Curves
---

# On the Stabilization of Rigid Formations on Regular Curves
**arXiv**：[2512.10700v1](https://arxiv.org/abs/2512.10700) · [PDF](https://arxiv.org/pdf/2512.10700.pdf)  
**作者**：Mohamed Elobaid, Shinkyu Park, Eric Feron  

**一句话要点**：提出随机多启动牛顿类算法和连续反馈律，以稳定多智能体刚性编队在平面曲线上的形成

**关键词**：多智能体系统, 刚性编队控制, 曲线稳定, 牛顿类算法, 连续反馈律, 路径扫描

## 3 点简述
- 核心问题：稳定多智能体刚性编队在平面可微曲线上的形成，包括路径扫描和顶点收敛
- 方法要点：使用随机多启动牛顿类算法寻找内接正多边形，设计连续反馈律确保曲线扫描和智能体间避碰
- 实验或效果：通过数值模拟验证方法在不同曲线和刚性编队上的有效性，代码已开源

## 摘要（原文）

> This work deals with the problem of stabilizing a multi-agent rigid formation on a general class of planar curves. Namely, we seek to stabilize an equilateral polygonal formation on closed planar differentiable curves after a path sweep. The task of finding an inscribed regular polygon centered at the point of interest is solved via a randomized multi-start Newton-Like algorithm for which one is able to ascertain the existence of a minimizer. Then we design a continuous feedback law that guarantees convergence to, and sufficient sweeping of the curve, followed by convergence to the desired formation vertices while ensuring inter-agent avoidance. The proposed approach is validated through numerical simulations for different classes of curves and different rigid formations. Code: https://github.com/mebbaid/paper-elobaid-ifacwc-2026

