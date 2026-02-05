---
layout: default
title: Bayesian PINNs for uncertainty-aware inverse problems (BPINN-IP)
---

# Bayesian PINNs for uncertainty-aware inverse problems (BPINN-IP)
**arXiv**：[2602.04459v1](https://arxiv.org/abs/2602.04459) · [PDF](https://arxiv.org/pdf/2602.04459.pdf)  
**作者**：Ali Mohammad-Djafari  

**一句话要点**：提出贝叶斯PINNs以解决线性逆问题中的不确定性量化问题

**关键词**：贝叶斯神经网络, 物理信息神经网络, 不确定性量化, 线性逆问题, 变分推断

## 3 点简述
- 核心问题：线性逆问题中传统PINNs缺乏不确定性量化能力
- 方法要点：采用分层贝叶斯框架，结合变分推断和蒙特卡洛dropout
- 实验或效果：应用于去卷积和超分辨率，提供预测均值和方差

## 摘要（原文）

> The main contribution of this paper is to develop a hierarchical Bayesian formulation of PINNs for linear inverse problems, which is called BPINN-IP. The proposed methodology extends PINN to account for prior knowledge on the nature of the expected NN output, as well as its weights. Also, as we can have access to the posterior probability distributions, naturally uncertainties can be quantified. Also, variational inference and Monte Carlo dropout are employed to provide predictive means and variances for reconstructed images. Un example of applications to deconvolution and super-resolution is considered, details of the different steps of implementations are given, and some preliminary results are presented.

