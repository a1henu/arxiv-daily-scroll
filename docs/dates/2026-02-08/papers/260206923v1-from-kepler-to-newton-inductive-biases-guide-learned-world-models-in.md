---
layout: default
title: From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers
---

# From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers
**arXiv**：[2602.06923v1](https://arxiv.org/abs/2602.06923) · [PDF](https://arxiv.org/pdf/2602.06923.pdf)  
**作者**：Ziming Liu, Sophia Sanborn, Surya Ganguli, Andreas Tolias  

**一句话要点**：引入三种归纳偏置使通用Transformer从曲线拟合转向学习物理世界模型

**关键词**：世界模型, 归纳偏置, Transformer, 物理定律发现, 自动科学发现

## 3 点简述
- 核心问题：通用AI架构能否超越预测，发现物理定律？
- 方法要点：引入空间平滑性、稳定性和时间局部性三种归纳偏置。
- 实验效果：Transformer成功学习开普勒和牛顿世界模型，实现自动科学发现。

## 摘要（原文）

> Can general-purpose AI architectures go beyond prediction to discover the physical laws governing the universe? True intelligence relies on "world models" -- causal abstractions that allow an agent to not only predict future states but understand the underlying governing dynamics. While previous "AI Physicist" approaches have successfully recovered such laws, they typically rely on strong, domain-specific priors that effectively "bake in" the physics. Conversely, Vafa et al. recently showed that generic Transformers fail to acquire these world models, achieving high predictive accuracy without capturing the underlying physical laws. We bridge this gap by systematically introducing three minimal inductive biases. We show that ensuring spatial smoothness (by formulating prediction as continuous regression) and stability (by training with noisy contexts to mitigate error accumulation) enables generic Transformers to surpass prior failures and learn a coherent Keplerian world model, successfully fitting ellipses to planetary trajectories. However, true physical insight requires a third bias: temporal locality. By restricting the attention window to the immediate past -- imposing the simple assumption that future states depend only on the local state rather than a complex history -- we force the model to abandon curve-fitting and discover Newtonian force representations. Our results demonstrate that simple architectural choices determine whether an AI becomes a curve-fitter or a physicist, marking a critical step toward automated scientific discovery.

