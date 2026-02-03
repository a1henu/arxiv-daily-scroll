---
layout: default
title: The Effect of Mini-Batch Noise on the Implicit Bias of Adam
---

# The Effect of Mini-Batch Noise on the Implicit Bias of Adam
**arXiv**：[2602.01642v1](https://arxiv.org/abs/2602.01642) · [PDF](https://arxiv.org/pdf/2602.01642.pdf)  
**作者**：Matias D. Cattaneo, Boris Shigida  

**一句话要点**：提出理论框架分析小批量噪声对Adam隐式偏差的影响，指导多轮训练超参数选择

**关键词**：Adam优化器, 隐式偏差, 小批量噪声, 多轮训练, 泛化性能, 超参数调优

## 3 点简述
- 研究小批量噪声如何影响Adam优化器的隐式偏差，关联损失景观锐度与泛化差距
- 理论推导显示批量大小与动量超参数(β1, β2)交互作用，导致正则化效应反转
- 实验验证在过拟合边缘的小规模数据中，超参数调整可提升验证精度

## 摘要（原文）

> With limited high-quality data and growing compute, multi-epoch training is gaining back its importance across sub-areas of deep learning. Adam(W), versions of which are go-to optimizers for many tasks such as next token prediction, has two momentum hyperparameters $(β_1, β_2)$ controlling memory and one very important hyperparameter, batch size, controlling (in particular) the amount mini-batch noise. We introduce a theoretical framework to understand how mini-batch noise influences the implicit bias of memory in Adam (depending on $β_1$, $β_2$) towards sharper or flatter regions of the loss landscape, which is commonly observed to correlate with the generalization gap in multi-epoch training. We find that in the case of large batch sizes, higher $β_2$ increases the magnitude of anti-regularization by memory (hurting generalization), but as the batch size becomes smaller, the dependence of (anti-)regulariation on $β_2$ is reversed. A similar monotonicity shift (in the opposite direction) happens in $β_1$. In particular, the commonly "default" pair $(β_1, β_2) = (0.9, 0.999)$ is a good choice if batches are small; for larger batches, in many settings moving $β_1$ closer to $β_2$ is much better in terms of validation accuracy in multi-epoch training. Moreover, our theoretical derivations connect the scale of the batch size at which the shift happens to the scale of the critical batch size. We illustrate this effect in experiments with small-scale data in the about-to-overfit regime.

