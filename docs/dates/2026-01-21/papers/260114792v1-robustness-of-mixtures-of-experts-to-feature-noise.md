---
layout: default
title: Robustness of Mixtures of Experts to Feature Noise
---

# Robustness of Mixtures of Experts to Feature Noise
**arXiv**：[2601.14792v1](https://arxiv.org/abs/2601.14792) · [PDF](https://arxiv.org/pdf/2601.14792.pdf)  
**作者**：Dong Sun, Rahul Nittala, Rebekka Burkholz  

**一句话要点**：证明混合专家模型通过稀疏激活过滤特征噪声，提升鲁棒性与收敛速度

**关键词**：混合专家模型, 特征噪声, 鲁棒性分析, 稀疏激活, 泛化误差, 收敛速度

## 3 点简述
- 核心问题：混合专家模型为何在参数规模外优于密集网络，尤其在特征噪声下
- 方法要点：在等参数设定下，分析稀疏专家激活作为噪声滤波器的理论机制
- 实验或效果：合成数据和真实语言任务验证了鲁棒性、泛化误差降低和收敛加速

## 摘要（原文）

> Despite their practical success, it remains unclear why Mixture of Experts (MoE) models can outperform dense networks beyond sheer parameter scaling. We study an iso-parameter regime where inputs exhibit latent modular structure but are corrupted by feature noise, a proxy for noisy internal activations. We show that sparse expert activation acts as a noise filter: compared to a dense estimator, MoEs achieve lower generalization error under feature noise, improved robustness to perturbations, and faster convergence speed. Empirical results on synthetic data and real-world language tasks corroborate the theoretical insights, demonstrating consistent robustness and efficiency gains from sparse modular computation.

