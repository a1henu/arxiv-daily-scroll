---
layout: default
title: Sample-efficient evidence estimation of score based priors for model selection
---

# Sample-efficient evidence estimation of score based priors for model selection
**arXiv**：[2602.20549v1](https://arxiv.org/abs/2602.20549) · [PDF](https://arxiv.org/pdf/2602.20549.pdf)  
**作者**：Frederic Wang, Katherine L. Bouman  

**一句话要点**：提出一种基于扩散先验的模型证据估计方法，用于解决逆问题中的先验选择问题。

**关键词**：扩散模型, 模型证据估计, 逆问题, 先验选择, 后验采样, 黑洞成像

## 3 点简述
- 核心问题：扩散先验的模型证据计算困难，现有方法需大量先验密度评估或准确先验分数。
- 方法要点：利用后验采样过程中的时间边际积分，通过少量样本（如20个）高效估计模型证据。
- 实验或效果：在非线性逆问题中验证准确性，包括黑洞成像，能选择正确先验并诊断先验失配。

## 摘要（原文）

> The choice of prior is central to solving ill-posed imaging inverse problems, making it essential to select one consistent with the measurements $y$ to avoid severe bias. In Bayesian inverse problems, this could be achieved by evaluating the model evidence $p(y \mid M)$ under different models $M$ that specify the prior and then selecting the one with the highest value. Diffusion models are the state-of-the-art approach to solving inverse problems with a data-driven prior; however, directly computing the model evidence with respect to a diffusion prior is intractable. Furthermore, most existing model evidence estimators require either many pointwise evaluations of the unnormalized prior density or an accurate clean prior score. We propose \method, an estimator of the model evidence of a diffusion prior by integrating over the time-marginals of posterior sampling methods. Our method leverages the large amount of intermediate samples naturally obtained during the reverse diffusion sampling process to obtain an accurate estimation of the model evidence using only a handful of posterior samples (e.g., 20). We also demonstrate how to implement our estimator in tandem with recent diffusion posterior sampling methods. Empirically, our estimator matches the model evidence when it can be computed analytically, and it is able to both select the correct diffusion model prior and diagnose prior misfit under different highly ill-conditioned, non-linear inverse problems, including a real-world black hole imaging problem.

