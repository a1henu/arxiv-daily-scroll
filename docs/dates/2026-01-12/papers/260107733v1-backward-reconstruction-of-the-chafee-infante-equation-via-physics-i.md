---
layout: default
title: Backward Reconstruction of the Chafee--Infante Equation via Physics-Informed WGAN-GP
---

# Backward Reconstruction of the Chafee--Infante Equation via Physics-Informed WGAN-GP
**arXiv**：[2601.07733v1](https://arxiv.org/abs/2601.07733) · [PDF](https://arxiv.org/pdf/2601.07733.pdf)  
**作者**：Joseph L. Shomberg  

**一句话要点**：提出物理信息WGAN-GP以解决二维Chafee–Infante方程逆问题，从近平衡态重建未知初始条件。

**关键词**：逆问题求解, 物理信息生成对抗网络, Chafee–Infante方程, 初始条件重建, Wasserstein损失, 梯度惩罚

## 3 点简述
- 核心问题：从反应扩散方程100次前向迭代后的近平衡态，重建未知初始条件，逆问题严重不适定且对噪声敏感。
- 方法要点：结合U-Net生成器、PatchGAN判别器、Wasserstein损失与梯度惩罚，并引入物理信息项如Lyapunov能量匹配和前向模拟惩罚。
- 实验或效果：在128×128网格数据集上，最佳模型测试集平均绝对误差约0.2399，标准差约0.0027，实现稳定反演和界面结构准确恢复。

## 摘要（原文）

> We present a physics-informed Wasserstein GAN with gradient penalty (WGAN-GP) for solving the inverse Chafee--Infante problem on two-dimensional domains with Dirichlet boundary conditions. The objective is to reconstruct an unknown initial condition from a near-equilibrium state obtained after 100 explicit forward Euler iterations of the reaction-diffusion equation \[ u_t - γΔu + κ\left(u^3 - u\right)=0. \] Because this mapping strongly damps high-frequency content, the inverse problem is severely ill-posed and sensitive to noise.
>   Our approach integrates a U-Net generator, a PatchGAN critic with spectral normalization, Wasserstein loss with gradient penalty, and several physics-informed auxiliary terms, including Lyapunov energy matching, distributional statistics, and a crucial forward-simulation penalty. This penalty enforces consistency between the predicted initial condition and its forward evolution under the \emph{same} forward Euler discretization used for dataset generation. Earlier experiments employing an Eyre-type semi-implicit solver were not compatible with this residual mechanism due to the cost and instability of Newton iterations within batched GPU training.
>   On a dataset of 50k training and 10k testing pairs on $128\times128$ grids (with natural $[-1,1]$ amplitude scaling), the best trained model attains a mean absolute error (MAE) of approximately \textbf{0.23988159} on the full test set, with a sample-wise standard deviation of about \textbf{0.00266345}. The results demonstrate stable inversion, accurate recovery of interfacial structure, and robustness to high-frequency noise in the initial data.

