---
layout: default
title: The power of small initialization in noisy low-tubal-rank tensor recovery
---

# The power of small initialization in noisy low-tubal-rank tensor recovery
**arXiv**：[2603.02729v1](https://arxiv.org/abs/2603.02729) · [PDF](https://arxiv.org/pdf/2603.02729.pdf)  
**作者**：ZHiyu Liu, Haobo Geng, Xudong Wang, Yandong Tang, Zhi Han, Yao Wang  

**一句话要点**：提出小初始化方法以解决噪声低管秩张量恢复中过参数化导致的误差增长问题

**关键词**：低管秩张量恢复, 因子化梯度下降, 过参数化, 噪声鲁棒性, 早期停止策略, t-乘积框架

## 3 点简述
- 研究噪声线性测量下低管秩张量恢复问题，聚焦过参数化场景
- 采用小初始化结合因子化梯度下降，实现与过估计管秩无关的恢复误差
- 通过四阶段分析框架和早期停止策略，理论验证与实验支持效果

## 摘要（原文）

> We study the problem of recovering a low-tubal-rank tensor $\mathcal{X}\_\star\in \mathbb{R}^{n \times n \times k}$ from noisy linear measurements under the t-product framework. A widely adopted strategy involves factorizing the optimization variable as $\mathcal{U} * \mathcal{U}^\top$, where $\mathcal{U} \in \mathbb{R}^{n \times R \times k}$, followed by applying factorized gradient descent (FGD) to solve the resulting optimization problem. Since the tubal-rank $r$ of the underlying tensor $\mathcal{X}_\star$ is typically unknown, this method often assumes $r < R \le n$, a regime known as over-parameterization. However, when the measurements are corrupted by some dense noise (e.g., Gaussian noise), FGD with the commonly used spectral initialization yields a recovery error that grows linearly with the over-estimated tubal-rank $R$. To address this issue, we show that using a small initialization enables FGD to achieve a nearly minimax optimal recovery error, even when the tubal-rank $R$ is significantly overestimated. Using a four-stage analytic framework, we analyze this phenomenon and establish the sharpest known error bound to date, which is independent of the overestimated tubal-rank $R$. Furthermore, we provide a theoretical guarantee showing that an easy-to-use early stopping strategy can achieve the best known result in practice. All these theoretical findings are validated through a series of simulations and real-data experiments.

