---
layout: default
title: Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks
---

# Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks
**arXiv**：[2601.22751v1](https://arxiv.org/abs/2601.22751) · [PDF](https://arxiv.org/pdf/2601.22751.pdf)  
**作者**：Gnankan Landry Regis N'guessan, Bum Jun Kim  

**一句话要点**：提出物理信息Müntz-Szász网络以显式学习物理系统中的幂律标度指数

**关键词**：物理信息神经网络, 幂律标度, 奇点分析, 可训练指数, 渐近可解释性, 约束感知训练

## 3 点简述
- 物理系统在奇点、界面和临界点附近呈现幂律标度，但标准神经网络无法显式处理标度指数。
- 引入MSN-PINN，将标度指数作为可训练参数，结合神经网络表达性和渐近分析可解释性。
- 实验显示，在噪声和稀疏采样下，单指数恢复误差为1-5%，二维拉普拉斯方程奇点指数误差低至0.009%。

## 摘要（原文）

> Physical systems near singularities, interfaces, and critical points exhibit power-law scaling, yet standard neural networks leave the governing exponents implicit. We introduce physics-informed M"untz-Sz'asz Networks (MSN-PINN), a power-law basis network that treats scaling exponents as trainable parameters. The model outputs both the solution and its scaling structure. We prove identifiability, or unique recovery, and show that, under these conditions, the squared error between learned and true exponents scales as $O(\|μ- α\|^2)$. Across experiments, MSN-PINN achieves single-exponent recovery with 1--5% error under noise and sparse sampling. It recovers corner singularity exponents for the two-dimensional Laplace equation with 0.009% error, matches the classical result of Kondrat'ev (1967), and recovers forcing-induced exponents in singular Poisson problems with 0.03% and 0.05% errors. On a 40-configuration wedge benchmark, it reaches a 100% success rate with 0.022% mean error. Constraint-aware training encodes physical requirements such as boundary condition compatibility and improves accuracy by three orders of magnitude over naive training. By combining the expressiveness of neural networks with the interpretability of asymptotic analysis, MSN-PINN produces learned parameters with direct physical meaning.

