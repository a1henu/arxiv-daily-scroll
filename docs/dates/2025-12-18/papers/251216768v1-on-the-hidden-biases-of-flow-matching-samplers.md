---
layout: default
title: On The Hidden Biases of Flow Matching Samplers
---

# On The Hidden Biases of Flow Matching Samplers
**arXiv**：[2512.16768v1](https://arxiv.org/abs/2512.16768) · [PDF](https://arxiv.org/pdf/2512.16768.pdf)  
**作者**：Soon Hoe Lim  

**一句话要点**：揭示流匹配采样器的隐式偏差，分析其结构性和能量性偏差。

**关键词**：流匹配采样器, 隐式偏差, 经验流匹配, 动能分析, 源分布影响, 能量次优

## 3 点简述
- 核心问题：经验流匹配最小化器几乎从不形成梯度场，导致内在能量次优。
- 方法要点：通过经验流匹配视角研究隐式偏差，分析生成样本的动能行为。
- 实验或效果：高斯源导致动能指数集中，重尾源导致多项式尾部，偏差主要由源分布决定。

## 摘要（原文）

> We study the implicit bias of flow matching (FM) samplers via the lens of empirical flow matching. Although population FM may produce gradient-field velocities resembling optimal transport (OT), we show that the empirical FM minimizer is almost never a gradient field, even when each conditional flow is. Consequently, empirical FM is intrinsically energetically suboptimal. In view of this, we analyze the kinetic energy of generated samples. With Gaussian sources, both instantaneous and integrated kinetic energies exhibit exponential concentration, while heavy-tailed sources lead to polynomial tails. These behaviors are governed primarily by the choice of source distribution rather than the data. Overall, these notes provide a concise mathematical account of the structural and energetic biases arising in empirical FM.

