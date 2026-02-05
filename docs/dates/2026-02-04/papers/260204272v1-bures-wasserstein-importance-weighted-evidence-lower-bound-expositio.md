---
layout: default
title: Bures-Wasserstein Importance-Weighted Evidence Lower Bound: Exposition and Applications
---

# Bures-Wasserstein Importance-Weighted Evidence Lower Bound: Exposition and Applications
**arXiv**：[2602.04272v1](https://arxiv.org/abs/2602.04272) · [PDF](https://arxiv.org/pdf/2602.04272.pdf)  
**作者**：Peiwen Jiang, Takuo Matsubara, Minh-Ngoc Tran  

**一句话要点**：提出Bures-Wasserstein空间中的重要性加权证据下界优化方法，以解决梯度估计器信噪比消失问题。

**关键词**：变分推断, 重要性加权证据下界, Bures-Wasserstein空间, 梯度估计稳定性, 高斯分布, Wasserstein度量

## 3 点简述
- 重要性加权证据下界在欧几里得空间优化时梯度估计器信噪比随样本数增加而消失，导致效率低下。
- 在Bures-Wasserstein空间中推导IW-ELBO的Wasserstein梯度，并投影到该空间，实现高斯变分推断的可行算法。
- 实验表明该方法在近似性能上优于基线，并证明梯度估计器信噪比随样本数增加而有利缩放。

## 摘要（原文）

> The Importance-Weighted Evidence Lower Bound (IW-ELBO) has emerged as an effective objective for variational inference (VI), tightening the standard ELBO and mitigating the mode-seeking behaviour.
>   However, optimizing the IW-ELBO in Euclidean space is often inefficient, as its gradient estimators suffer from a vanishing signal-to-noise ratio (SNR). This paper formulates the optimisation of the IW-ELBO in Bures-Wasserstein space, a manifold of Gaussian distributions equipped with the 2-Wasserstein metric. We derive the Wasserstein gradient of the IW-ELBO and project it onto the Bures-Wasserstein space to yield a tractable algorithm for Gaussian VI.
>   A pivotal contribution of our analysis concerns the stability of the gradient estimator. While the SNR of the standard Euclidean gradient estimator is known to vanish as the number of importance samples $K$ increases, we prove that the SNR of the Wasserstein gradient scales favourably as $Ω(\sqrt{K})$, ensuring optimisation efficiency even for large $K$. We further extend this geometric analysis to the Variational Rényi Importance-Weighted Autoencoder bound, establishing analogous stability guarantees. Experiments demonstrate that the proposed framework achieves superior approximation performance compared to other baselines.

