---
layout: default
title: Standard Transformers Achieve the Minimax Rate in Nonparametric Regression with $C^{s,λ}$ Targets
---

# Standard Transformers Achieve the Minimax Rate in Nonparametric Regression with $C^{s,λ}$ Targets
**arXiv**：[2602.20555v1](https://arxiv.org/abs/2602.20555) · [PDF](https://arxiv.org/pdf/2602.20555.pdf)  
**作者**：Yanming Lai, Defeng Sun  

**一句话要点**：证明标准Transformer在非参数回归中达到Hölder目标函数的最小最大最优率

**关键词**：Transformer理论分析, 非参数回归, Hölder函数近似, 最小最大率, 结构刻画

## 3 点简述
- 核心问题：标准Transformer能否近似Hölder函数并实现非参数回归的最优收敛率
- 方法要点：引入尺寸元组和维度向量精细刻画Transformer结构，推导近似能力和Lipschitz常数上界
- 实验或效果：理论证明标准Transformer在L^t距离下任意精度近似Hölder函数，达到最小最大最优率

## 摘要（原文）

> The tremendous success of Transformer models in fields such as large language models and computer vision necessitates a rigorous theoretical investigation. To the best of our knowledge, this paper is the first work proving that standard Transformers can approximate Hölder functions $ C^{s,λ}\left([0,1]^{d\times n}\right) $$ (s\in\mathbb{N}_{\geq0},0<λ\leq1) $ under the $L^t$ distance ($t \in [1, \infty]$) with arbitrary precision. Building upon this approximation result, we demonstrate that standard Transformers achieve the minimax optimal rate in nonparametric regression for Hölder target functions. It is worth mentioning that, by introducing two metrics: the size tuple and the dimension vector, we provide a fine-grained characterization of Transformer structures, which facilitates future research on the generalization and optimization errors of Transformers with different structures. As intermediate results, we also derive the upper bounds for the Lipschitz constant of standard Transformers and their memorization capacity, which may be of independent interest. These findings provide theoretical justification for the powerful capabilities of Transformer models.

