---
layout: default
title: Learning with Locally Private Examples by Inverse Weierstrass Private Stochastic Gradient Descent
---

# Learning with Locally Private Examples by Inverse Weierstrass Private Stochastic Gradient Descent
**arXiv**：[2602.16436v1](https://arxiv.org/abs/2602.16436) · [PDF](https://arxiv.org/pdf/2602.16436.pdf)  
**作者**：Jean Dufraiche, Paul Mangold, Michaël Perrot, Marc Tommasi  

**一句话要点**：提出逆魏尔斯特拉斯私有随机梯度下降以解决非交互式本地差分隐私下数据发布导致的偏差问题

**关键词**：本地差分隐私, 偏差校正, 随机梯度下降, 二进制分类, 魏尔斯特拉斯变换, 无偏估计

## 3 点简述
- 核心问题：非交互式本地差分隐私数据发布在后续分析中可能引入偏差，影响模型准确性
- 方法要点：利用魏尔斯特拉斯变换分析偏差，通过逆变换实现无偏估计，构建IWP-SGD算法
- 实验或效果：在合成和真实数据集上验证IWP-SGD，收敛到真实风险最小化器，速率为O(1/n)

## 摘要（原文）

> Releasing data once and for all under noninteractive Local Differential Privacy (LDP) enables complete data reusability, but the resulting noise may create bias in subsequent analyses. In this work, we leverage the Weierstrass transform to characterize this bias in binary classification. We prove that inverting this transform leads to a bias-correction method to compute unbiased estimates of nonlinear functions on examples released under LDP. We then build a novel stochastic gradient descent algorithm called Inverse Weierstrass Private SGD (IWP-SGD). It converges to the true population risk minimizer at a rate of $\mathcal{O}(1/n)$, with $n$ the number of examples. We empirically validate IWP-SGD on binary classification tasks using synthetic and real-world datasets.

