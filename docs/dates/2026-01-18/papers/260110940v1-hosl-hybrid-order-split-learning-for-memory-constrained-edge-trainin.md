---
layout: default
title: HOSL: Hybrid-Order Split Learning for Memory-Constrained Edge Training
---

# HOSL: Hybrid-Order Split Learning for Memory-Constrained Edge Training
**arXiv**：[2601.10940v1](https://arxiv.org/abs/2601.10940) · [PDF](https://arxiv.org/pdf/2601.10940.pdf)  
**作者**：Aakriti, Zhe Li, Dandan Liang, Chao Huang, Rui Li, Haibo Yang  

**一句话要点**：提出混合阶分割学习框架HOSL，以解决边缘设备内存受限下大语言模型训练的效率与性能权衡问题。

**关键词**：分割学习, 边缘训练, 混合阶优化, 内存效率, 大语言模型, 零阶梯度估计

## 3 点简述
- 现有分割学习依赖一阶优化，导致客户端内存开销大，抵消模型分割优势。
- HOSL在客户端采用零阶优化减少内存，服务器端用一阶优化确保收敛与性能。
- 实验显示HOSL在OPT模型上降低客户端GPU内存达3.7倍，精度接近一阶基线。

## 摘要（原文）

> Split learning (SL) enables collaborative training of large language models (LLMs) between resource-constrained edge devices and compute-rich servers by partitioning model computation across the network boundary. However, existing SL systems predominantly rely on first-order (FO) optimization, which requires clients to store intermediate quantities such as activations for backpropagation. This results in substantial memory overhead, largely negating benefits of model partitioning. In contrast, zeroth-order (ZO) optimization eliminates backpropagation and significantly reduces memory usage, but often suffers from slow convergence and degraded performance. In this work, we propose HOSL, a novel Hybrid-Order Split Learning framework that addresses this fundamental trade-off between memory efficiency and optimization effectiveness by strategically integrating ZO optimization on the client side with FO optimization on the server side. By employing memory-efficient ZO gradient estimation at the client, HOSL eliminates backpropagation and activation storage, reducing client memory consumption. Meanwhile, server-side FO optimization ensures fast convergence and competitive performance. Theoretically, we show that HOSL achieves a $\mathcal{O}(\sqrt{d_c/TQ})$ rate, which depends on client-side model dimension $d_c$ rather than the full model dimension $d$, demonstrating that convergence improves as more computation is offloaded to the server. Extensive experiments on OPT models (125M and 1.3B parameters) across 6 tasks demonstrate that HOSL reduces client GPU memory by up to 3.7$\times$ compared to the FO method while achieving accuracy within 0.20%-4.23% of this baseline. Furthermore, HOSL outperforms the ZO baseline by up to 15.55%, validating the effectiveness of our hybrid strategy for memory-efficient training on edge devices.

