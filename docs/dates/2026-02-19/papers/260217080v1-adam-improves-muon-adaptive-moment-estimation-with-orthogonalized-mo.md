---
layout: default
title: Adam Improves Muon: Adaptive Moment Estimation with Orthogonalized Momentum
---

# Adam Improves Muon: Adaptive Moment Estimation with Orthogonalized Momentum
**arXiv**：[2602.17080v1](https://arxiv.org/abs/2602.17080) · [PDF](https://arxiv.org/pdf/2602.17080.pdf)  
**作者**：Minxin Zhang, Yuxuan Liu, Hayden Scheaffer  

**一句话要点**：提出NAMO和NAMO-D优化器，将正交动量与Adam型噪声适应结合，提升大语言模型训练性能。

**关键词**：优化算法, 正交动量, 自适应噪声适应, 大语言模型训练, 随机优化

## 3 点简述
- 核心问题：如何有效结合正交动量与自适应噪声适应以改进随机优化器性能。
- 方法要点：NAMO使用单一自适应步长缩放正交动量，NAMO-D引入对角矩阵进行神经元级噪声适应。
- 实验或效果：在GPT-2预训练中优于AdamW和Muon，NAMO-D通过额外超参数实现进一步增益。

## 摘要（原文）

> Efficient stochastic optimization typically integrates an update direction that performs well in the deterministic regime with a mechanism adapting to stochastic perturbations. While Adam uses adaptive moment estimates to promote stability, Muon utilizes the weight layers' matrix structure via orthogonalized momentum, showing superior performance in large language model training. We propose a new optimizer and a diagonal extension, NAMO and NAMO-D, providing the first principled integration of orthogonalized momentum with norm-based Adam-type noise adaptation. NAMO scales orthogonalized momentum using a single adaptive stepsize, preserving orthogonality while improving upon Muon at negligible additional cost. NAMO-D instead right-multiplies orthogonalized momentum by a diagonal matrix with clamped entries. This design enables neuron-wise noise adaptation and aligns with the common near block-diagonal Hessian structure. Under standard assumptions, we establish optimal convergence rates for both algorithms in the deterministic setting and show that, in the stochastic setting, their convergence guarantees adapt to the noise level of stochastic gradients. Experiments on pretraining GPT-2 models demonstrate improved performance of both NAMO and NAMO-D compared to the AdamW and Muon baselines, with NAMO-D achieving further gains over NAMO via an additional clamping hyperparameter that balances the competing goals of maintaining a well-conditioned update direction and leveraging fine-grained noise adaptation.

