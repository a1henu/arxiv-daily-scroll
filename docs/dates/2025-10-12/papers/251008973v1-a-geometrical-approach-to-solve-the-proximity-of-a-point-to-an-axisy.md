---
layout: default
title: A geometrical approach to solve the proximity of a point to an axisymmetric quadric in space
---

# A geometrical approach to solve the proximity of a point to an axisymmetric quadric in space
**arXiv**：[2510.08973v1](https://arxiv.org/abs/2510.08973) · [PDF](https://arxiv.org/pdf/2510.08973.pdf)  
**作者**：Bibekananda Patra, Aditya Mahesh Kolte, Sandipan Bandyopadhyay  

**一句话要点**：提出几何方法解决空间点与轴对称二次曲面邻近问题，并实现高效计算。

**关键词**：轴对称二次曲面, 点邻近问题, 几何方法, 降维求解, 圆锥曲线, 高效计算

## 3 点简述
- 核心问题：计算三维空间中给定点与轴对称二次曲面的最短距离。
- 方法要点：将问题降维至二维，利用圆锥曲线几何性质分类求解。
- 实验或效果：在C语言实现中，速度优于Bullet商业库。

## 摘要（原文）

> This paper presents the classification of a general quadric into an
> axisymmetric quadric (AQ) and the solution to the problem of the proximity of a
> given point to an AQ. The problem of proximity in $R^3$ is reduced to the same
> in $R^2$, which is not found in the literature. A new method to solve the
> problem in $R^2$ is used based on the geometrical properties of the conics,
> such as sub-normal, length of the semi-major axis, eccentricity, slope and
> radius. Furthermore, the problem in $R^2$ is categorised into two and three
> more sub-cases for parabola and ellipse/hyperbola, respectively, depending on
> the location of the point, which is a novel approach as per the authors'
> knowledge. The proposed method is suitable for implementation in a common
> programming language, such as C and proved to be faster than a commercial
> library, namely, Bullet.

