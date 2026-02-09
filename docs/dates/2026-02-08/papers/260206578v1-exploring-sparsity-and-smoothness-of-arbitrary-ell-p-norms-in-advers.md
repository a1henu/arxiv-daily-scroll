---
layout: default
title: Exploring Sparsity and Smoothness of Arbitrary $\ell_p$ Norms in Adversarial Attacks
---

# Exploring Sparsity and Smoothness of Arbitrary $\ell_p$ Norms in Adversarial Attacks
**arXiv**：[2602.06578v1](https://arxiv.org/abs/2602.06578) · [PDF](https://arxiv.org/pdf/2602.06578.pdf)  
**作者**：Christof Duhme, Florian Eilers, Xiaoyi Jiang  

**一句话要点**：探索任意ℓp范数在对抗攻击中的稀疏性与平滑性，以优化范数选择

**关键词**：对抗攻击, ℓp范数, 稀疏性, 平滑性, 深度学习, 图像数据集

## 3 点简述
- 研究ℓp范数参数p如何影响对抗扰动的稀疏性与平滑性，针对p∈[1,2]范围
- 采用文献稀疏度度量并引入三种平滑度度量，包括基于平滑操作和泰勒近似的框架
- 实验表明ℓ1或ℓ2范数通常非最优，p∈[1.3,1.5]在稀疏与平滑攻击间提供最佳平衡

## 摘要（原文）

> Adversarial attacks against deep neural networks are commonly constructed under $\ell_p$ norm constraints, most often using $p=1$, $p=2$ or $p=\infty$, and potentially regularized for specific demands such as sparsity or smoothness. These choices are typically made without a systematic investigation of how the norm parameter \( p \) influences the structural and perceptual properties of adversarial perturbations. In this work, we study how the choice of \( p \) affects sparsity and smoothness of adversarial attacks generated under \( \ell_p \) norm constraints for values of $p \in [1,2]$. To enable a quantitative analysis, we adopt two established sparsity measures from the literature and introduce three smoothness measures. In particular, we propose a general framework for deriving smoothness measures based on smoothing operations and additionally introduce a smoothness measure based on first-order Taylor approximations. Using these measures, we conduct a comprehensive empirical evaluation across multiple real-world image datasets and a diverse set of model architectures, including both convolutional and transformer-based networks. We show that the choice of $\ell_1$ or $\ell_2$ is suboptimal in most cases and the optimal $p$ value is dependent on the specific task. In our experiments, using $\ell_p$ norms with $p\in [1.3, 1.5]$ yields the best trade-off between sparse and smooth attacks. These findings highlight the importance of principled norm selection when designing and evaluating adversarial attacks.

