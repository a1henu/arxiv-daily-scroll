---
layout: default
title: LDLT $\mathcal{L}$-Lipschitz Network: Generalized Deep End-To-End Lipschitz Network Construction
---

# LDLT $\mathcal{L}$-Lipschitz Network: Generalized Deep End-To-End Lipschitz Network Construction
**arXiv**：[2512.05915v1](https://arxiv.org/abs/2512.05915) · [PDF](https://arxiv.org/pdf/2512.05915.pdf)  
**作者**：Marius F. R. Juston, Ramavarapu S. Sreenivas, Dustin Nottage, Ahmet Soylemezoglu  

**一句话要点**：提出基于LDLT分解的广义Lipschitz网络构建方法，以增强对抗鲁棒性和网络可验证性。

**关键词**：Lipschitz网络, 对抗鲁棒性, 线性矩阵不等式, 深度残差网络, 网络可验证性, 参数化方法

## 3 点简述
- 核心问题：控制神经网络Lipschitz常数以提升对抗鲁棒性和可验证性，但现有方法局限于特定架构。
- 方法要点：利用LDLT分解扩展LMI框架，实现任意非线性架构的Lipschitz网络参数化构建。
- 实验或效果：在121个UCI数据集上，相比SLL Layers，准确率提升3%-13%，保持网络表达力。

## 摘要（原文）

> Deep residual networks (ResNets) have demonstrated outstanding success in computer vision tasks, attributed to their ability to maintain gradient flow through deep architectures. Simultaneously, controlling the Lipschitz constant in neural networks has emerged as an essential area of research to enhance adversarial robustness and network certifiability. This paper presents a rigorous approach to the general design of $\mathcal{L}$-Lipschitz deep residual networks using a Linear Matrix Inequality (LMI) framework. Initially, the ResNet architecture was reformulated as a cyclic tridiagonal LMI, and closed-form constraints on network parameters were derived to ensure $\mathcal{L}$-Lipschitz continuity; however, using a new $LDL^\top$ decomposition approach for certifying LMI feasibility, we extend the construction of $\mathcal{L}$-Lipchitz networks to any other nonlinear architecture. Our contributions include a provable parameterization methodology for constructing Lipschitz-constrained residual networks and other hierarchical architectures. Cholesky decomposition is also used for efficient parameterization. These findings enable robust network designs applicable to adversarial robustness, certified training, and control systems. The $LDL^\top$ formulation is shown to be a tight relaxation of the SDP-based network, maintaining full expressiveness and achieving 3\%-13\% accuracy gains over SLL Layers on 121 UCI data sets.

