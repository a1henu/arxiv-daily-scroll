---
layout: default
title: Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay
---

# Optimal Learning-Rate Schedules under Functional Scaling Laws: Power Decay and Warmup-Stable-Decay
**arXiv**：[2602.06797v1](https://arxiv.org/abs/2602.06797) · [PDF](https://arxiv.org/pdf/2602.06797.pdf)  
**作者**：Binghui Li, Zilin Wang, Fengling Chen, Shiyang Zhao, Ruiheng Zheng, Lei Wu  

**一句话要点**：提出基于功能缩放定律的最优学习率调度策略，揭示幂衰减与预热-稳定-衰减的相变现象。

**关键词**：学习率调度, 功能缩放定律, 优化理论, 随机梯度下降, 核回归, 相变分析

## 3 点简述
- 在功能缩放定律框架下，研究固定训练周期内的最优学习率调度问题。
- 根据任务难度（s与β关系），推导出幂衰减或预热-稳定-衰减的最优调度结构。
- 理论分析应用于核回归SGD，实现最小最大最优率，实验验证预测。

## 摘要（原文）

> We study optimal learning-rate schedules (LRSs) under the functional scaling law (FSL) framework introduced in Li et al. (2025), which accurately models the loss dynamics of both linear regression and large language model (LLM) pre-training. Within FSL, loss dynamics are governed by two exponents: a source exponent $s>0$ controlling the rate of signal learning, and a capacity exponent $β>1$ determining the rate of noise forgetting. Focusing on a fixed training horizon $N$, we derive the optimal LRSs and reveal a sharp phase transition. In the easy-task regime $s \ge 1 - 1/β$, the optimal schedule follows a power decay to zero, $η^*(z) = η_{\mathrm{peak}}(1 - z/N)^{2β- 1}$, where the peak learning rate scales as $η_{\mathrm{peak}} \eqsim N^{-ν}$ for an explicit exponent $ν= ν(s,β)$. In contrast, in the hard-task regime $s < 1 - 1/β$, the optimal LRS exhibits a warmup-stable-decay (WSD) (Hu et al. (2024)) structure: it maintains the largest admissible learning rate for most of training and decays only near the end, with the decay phase occupying a vanishing fraction of the horizon.
>   We further analyze optimal shape-fixed schedules, where only the peak learning rate is tuned -- a strategy widely adopted in practiceand characterize their strengths and intrinsic limitations. This yields a principled evaluation of commonly used schedules such as cosine and linear decay. Finally, we apply the power-decay LRS to one-pass stochastic gradient descent (SGD) for kernel regression and show the last iterate attains the exact minimax-optimal rate, eliminating the logarithmic suboptimality present in prior analyses. Numerical experiments corroborate our theoretical predictions.

