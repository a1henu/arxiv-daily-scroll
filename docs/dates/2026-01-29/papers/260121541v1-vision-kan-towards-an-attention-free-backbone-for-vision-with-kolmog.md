---
layout: default
title: Vision KAN: Towards an Attention-Free Backbone for Vision with Kolmogorov-Arnold Networks
---

# Vision KAN: Towards an Attention-Free Backbone for Vision with Kolmogorov-Arnold Networks
**arXiv**：[2601.21541v1](https://arxiv.org/abs/2601.21541) · [PDF](https://arxiv.org/pdf/2601.21541.pdf)  
**作者**：Zhuoqin Yang, Jiansong Zhang, Xiaoling Luo, Xu Wu, Zheng Lu, Linlin Shen  

**一句话要点**：提出Vision KAN作为无注意力视觉骨干，基于Kolmogorov-Arnold网络实现线性复杂度竞争性能

**关键词**：无注意力骨干, Kolmogorov-Arnold网络, 令牌混合器, 线性复杂度, 径向基函数, 视觉骨干网络

## 3 点简述
- 核心问题：注意力机制在视觉骨干中存在二次复杂度高和可解释性差的问题，限制可扩展性和清晰度
- 方法要点：引入MultiPatch-RBFKAN作为统一令牌混合器，结合基于径向基函数的KAN、轴可分离混合和低秩全局映射，以补丁分组策略降低计算成本
- 实验或效果：在ImageNet-1K上实验显示，ViK以线性复杂度实现竞争性准确率，验证KAN基础令牌混合作为注意力高效替代的潜力

## 摘要（原文）

> Attention mechanisms have become a key module in modern vision backbones due to their ability to model long-range dependencies. However, their quadratic complexity in sequence length and the difficulty of interpreting attention weights limit both scalability and clarity. Recent attention-free architectures demonstrate that strong performance can be achieved without pairwise attention, motivating the search for alternatives. In this work, we introduce Vision KAN (ViK), an attention-free backbone inspired by the Kolmogorov-Arnold Networks. At its core lies MultiPatch-RBFKAN, a unified token mixer that combines (a) patch-wise nonlinear transform with Radial Basis Function-based KANs, (b) axis-wise separable mixing for efficient local propagation, and (c) low-rank global mapping for long-range interaction. Employing as a drop-in replacement for attention modules, this formulation tackles the prohibitive cost of full KANs on high-resolution features by adopting a patch-wise grouping strategy with lightweight operators to restore cross-patch dependencies. Experiments on ImageNet-1K show that ViK achieves competitive accuracy with linear complexity, demonstrating the potential of KAN-based token mixing as an efficient and theoretically grounded alternative to attention.

