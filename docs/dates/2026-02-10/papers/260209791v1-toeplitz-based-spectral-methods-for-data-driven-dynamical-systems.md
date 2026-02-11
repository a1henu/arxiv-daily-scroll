---
layout: default
title: Toeplitz Based Spectral Methods for Data-driven Dynamical Systems
---

# Toeplitz Based Spectral Methods for Data-driven Dynamical Systems
**arXiv**：[2602.09791v1](https://arxiv.org/abs/2602.09791) · [PDF](https://arxiv.org/pdf/2602.09791.pdf)  
**作者**：Vladimir R. Kostic, Karim Lounici, Massimiliano Pontil  

**一句话要点**：提出基于Toeplitz的谱方法，用于数据驱动的线性演化算子谱估计。

**关键词**：Toeplitz滤波器, 谱估计, 数据驱动动力学, Koopman算子, 无穷小生成元, 统计学习算法

## 3 点简述
- 核心问题：从平衡轨迹数据估计线性演化算子（如转移和Koopman算子）的谱性质，未知运动方程。
- 方法要点：应用Toeplitz滤波器到无穷小生成元，提取特征值、特征函数和谱测度，可融入自伴或斜对称等结构先验。
- 实验或效果：在确定性和混沌系统中数值实验，显示能恢复标准数据驱动方法无法达到的谱性质，统计一致且计算高效。

## 摘要（原文）

> We introduce a Toeplitz-based framework for data-driven spectral estimation of linear evolution operators in dynamical systems. Focusing on transfer and Koopman operators from equilibrium trajectories without access to the underlying equations of motion, our method applies Toeplitz filters to the infinitesimal generator to extract eigenvalues, eigenfunctions, and spectral measures. Structural prior knowledge, such as self-adjointness or skew-symmetry, can be incorporated by design. The approach is statistically consistent and computationally efficient, leveraging both primal and dual algorithms commonly used in statistical learning. Numerical experiments on deterministic and chaotic systems demonstrate that the framework can recover spectral properties beyond the reach of standard data-driven methods.

