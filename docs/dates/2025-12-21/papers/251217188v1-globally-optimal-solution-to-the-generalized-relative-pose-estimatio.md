---
layout: default
title: Globally Optimal Solution to the Generalized Relative Pose Estimation Problem using Affine Correspondences
---

# Globally Optimal Solution to the Generalized Relative Pose Estimation Problem using Affine Correspondences
**arXiv**：[2512.17188v1](https://arxiv.org/abs/2512.17188) · [PDF](https://arxiv.org/pdf/2512.17188.pdf)  
**作者**：Zhenbao Yu, Banglei Guan, Shunkun Liang, Zibin Liu, Yang Shang, Qifeng Yu  

**一句话要点**：提出基于仿射对应的全局最优解算器，用于已知垂直方向的广义相对位姿估计

**关键词**：广义相对位姿估计, 仿射对应, 全局优化, 多项式求解, 多相机系统, 惯性测量单元

## 3 点简述
- 针对多相机系统相对位姿估计精度问题，利用仿射对应建立几何约束
- 通过解耦旋转矩阵和平移向量，将全局优化转化为多项式求解问题
- 在合成和真实数据集上验证，方法在准确性上优于现有先进方法

## 摘要（原文）

> Mobile devices equipped with a multi-camera system and an inertial measurement unit (IMU) are widely used nowadays, such as self-driving cars. The task of relative pose estimation using visual and inertial information has important applications in various fields. To improve the accuracy of relative pose estimation of multi-camera systems, we propose a globally optimal solver using affine correspondences to estimate the generalized relative pose with a known vertical direction. First, a cost function about the relative rotation angle is established after decoupling the rotation matrix and translation vector, which minimizes the algebraic error of geometric constraints from affine correspondences. Then, the global optimization problem is converted into two polynomials with two unknowns based on the characteristic equation and its first derivative is zero. Finally, the relative rotation angle can be solved using the polynomial eigenvalue solver, and the translation vector can be obtained from the eigenvector. Besides, a new linear solution is proposed when the relative rotation is small. The proposed solver is evaluated on synthetic data and real-world datasets. The experiment results demonstrate that our method outperforms comparable state-of-the-art methods in accuracy.

