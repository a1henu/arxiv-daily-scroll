---
layout: default
title: Asymmetric regularization mechanism for GAN training with Variational Inequalities
---

# Asymmetric regularization mechanism for GAN training with Variational Inequalities
**arXiv**：[2601.13920v1](https://arxiv.org/abs/2601.13920) · [PDF](https://arxiv.org/pdf/2601.13920.pdf)  
**作者**：Spyridon C. Giagtzoglou, Mark H. M. Winands, Barbara Franci  

**一句话要点**：提出基于非对称正则化的GAN训练机制，以稳定训练并寻求纳什均衡。

**关键词**：生成对抗网络, 纳什均衡, 正则化机制, 训练稳定性, 线性收敛

## 3 点简述
- 将GAN训练建模为纳什均衡寻求问题，旨在解决训练不稳定问题。
- 引入非对称正则化机制，结合Tikhonov步和零中心梯度惩罚，确保算子性质。
- 在学术示例上实证，即使无强单调性，该机制也能收敛并稳定轨迹。

## 摘要（原文）

> We formulate the training of generative adversarial networks (GANs) as a Nash equilibrium seeking problem. To stabilize the training process and find a Nash equilibrium, we propose an asymmetric regularization mechanism based on the classic Tikhonov step and on a novel zero-centered gradient penalty. Under smoothness and a local identifiability condition induced by a Gauss-Newton Gramian, we obtain explicit Lipschitz and (strong)-monotonicity constants for the regularized operator. These constants ensure last-iterate linear convergence of a single-call Extrapolation-from-the-Past (EFTP) method. Empirical simulations on an academic example show that, even when strong monotonicity cannot be achieved, the asymmetric regularization is enough to converge to an equilibrium and stabilize the trajectory.

