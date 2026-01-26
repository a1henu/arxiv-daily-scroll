---
layout: default
title: E2Former-V2: On-the-Fly Equivariant Attention with Linear Activation Memory
---

# E2Former-V2: On-the-Fly Equivariant Attention with Linear Activation Memory
**arXiv**：[2601.16622v1](https://arxiv.org/abs/2601.16622) · [PDF](https://arxiv.org/pdf/2601.16622.pdf)  
**作者**：Lin Huang, Chengxiang Huang, Ziang Wang, Yiyue Du, Chu Wang, Haocheng Lu, Yunyang Li, Xiaoli Liu, Arthur Jiang, Jia Zhang  

**一句话要点**：提出E2Former-V2，通过代数稀疏化和硬件感知执行，解决等变图神经网络在3D原子系统建模中的可扩展性瓶颈。

**关键词**：等变图神经网络, 3D原子系统建模, 代数稀疏化, 硬件感知执行, 注意力机制, 可扩展性优化

## 3 点简述
- 主流等变图神经网络因显式构建几何特征或密集张量积导致可扩展性瓶颈。
- 引入EAAS和On-the-Fly Equivariant Attention，将密集张量收缩转换为稀疏奇偶重索引操作，并实现节点中心注意力机制。
- 在SPICE和OMol25数据集上，E2Former-V2保持预测性能，推理速度显著提升，TFLOPS提高20倍。

## 摘要（原文）

> Equivariant Graph Neural Networks (EGNNs) have become a widely used approach for modeling 3D atomistic systems. However, mainstream architectures face critical scalability bottlenecks due to the explicit construction of geometric features or dense tensor products on \textit{every} edge. To overcome this, we introduce \textbf{E2Former-V2}, a scalable architecture that integrates algebraic sparsity with hardware-aware execution. We first propose \textbf{E}quivariant \textbf{A}xis-\textbf{A}ligned \textbf{S}parsification (EAAS). EAAS builds on Wigner-$6j$ convolution by exploiting an $\mathrm{SO}(3) \rightarrow \mathrm{SO}(2)$ change of basis to transform computationally expensive dense tensor contractions into efficient, sparse parity re-indexing operations. Building on this representation, we introduce \textbf{On-the-Fly Equivariant Attention}, a fully node-centric mechanism implemented via a custom fused Triton kernel. By eliminating materialized edge tensors and maximizing SRAM utilization, our kernel achieves a \textbf{20$\times$ improvement in TFLOPS} compared to standard implementations. Extensive experiments on the SPICE and OMol25 datasets demonstrate that E2Former-V2 maintains comparable predictive performance while notably accelerating inference. This work demonstrates that large equivariant transformers can be trained efficiently using widely accessible GPU platforms. The code is avalible at https://github.com/IQuestLab/UBio-MolFM/tree/e2formerv2.

