---
layout: default
title: Intrinsic Lorentz Neural Network
---

# Intrinsic Lorentz Neural Network
**arXiv**：[2602.23981v1](https://arxiv.org/abs/2602.23981) · [PDF](https://arxiv.org/pdf/2602.23981.pdf)  
**作者**：Xianglong Shi, Ziheng Chen, Yunhan Jiang, Nicu Sebe  

**一句话要点**：提出完全内蕴的洛伦兹神经网络，在双曲几何中处理层次结构数据。

**关键词**：双曲神经网络, 洛伦兹模型, 内蕴计算, 层次结构数据, 点对超平面层, GyroLBN

## 3 点简述
- 核心问题：现有双曲神经网络常混合欧几里得与双曲操作，非完全内蕴。
- 方法要点：引入点对超平面全连接层，基于洛伦兹模型设计内蕴模块如GyroLBN。
- 实验或效果：在CIFAR-10/100和基因组基准测试中达到SOTA，超越欧几里得基线。

## 摘要（原文）

> Real-world data frequently exhibit latent hierarchical structures, which can be naturally represented by hyperbolic geometry. Although recent hyperbolic neural networks have demonstrated promising results, many existing architectures remain partially intrinsic, mixing Euclidean operations with hyperbolic ones or relying on extrinsic parameterizations. To address it, we propose the \emph{Intrinsic Lorentz Neural Network} (ILNN), a fully intrinsic hyperbolic architecture that conducts all computations within the Lorentz model. At its core, the network introduces a novel \emph{point-to-hyperplane} fully connected layer (FC), replacing traditional Euclidean affine logits with closed-form hyperbolic distances from features to learned Lorentz hyperplanes, thereby ensuring that the resulting geometric decision functions respect the inherent curvature. Around this fundamental layer, we design intrinsic modules: GyroLBN, a Lorentz batch normalization that couples gyro-centering with gyro-scaling, consistently outperforming both LBN and GyroBN while reducing training time. We additionally proposed a gyro-additive bias for the FC output, a Lorentz patch-concatenation operator that aligns the expected log-radius across feature blocks via a digamma-based scale, and a Lorentz dropout layer. Extensive experiments conducted on CIFAR-10/100 and two genomic benchmarks (TEB and GUE) illustrate that ILNN achieves state-of-the-art performance and computational cost among hyperbolic models and consistently surpasses strong Euclidean baselines. The code is available at \href{https://github.com/Longchentong/ILNN}{\textcolor{magenta}{this url}}.

