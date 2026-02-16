---
layout: default
title: FlashSchNet: Fast and Accurate Coarse-Grained Neural Network Molecular Dynamics
---

# FlashSchNet: Fast and Accurate Coarse-Grained Neural Network Molecular Dynamics
**arXiv**：[2602.13140v1](https://arxiv.org/abs/2602.13140) · [PDF](https://arxiv.org/pdf/2602.13140.pdf)  
**作者**：Pingzhi Li, Hongxuan Li, Zirui Liu, Xingcheng Lin, Tianlong Chen  

**一句话要点**：提出FlashSchNet以解决图神经网络分子动力学模拟中GPU利用率低和速度慢的问题

**关键词**：图神经网络, 分子动力学模拟, GPU优化, IO感知计算, 粗粒度建模, 量化加速

## 3 点简述
- 核心问题：SchNet等GNN势能模型因内存访问瓶颈和碎片化计算导致GPU利用率不足，模拟速度慢于经典力场。
- 方法要点：采用IO感知设计，通过闪存径向基、闪存消息传递、闪存聚合和通道量化四项技术融合计算步骤，减少内存读写。
- 实验或效果：在单GPU上，对粗粒度蛋白质模拟实现1000 ns/天吞吐量，比基线快6.5倍，内存峰值降低80%，保持高精度。

## 摘要（原文）

> Graph neural network (GNN) potentials such as SchNet improve the accuracy and transferability of molecular dynamics (MD) simulation by learning many-body interactions, but remain slower than classical force fields due to fragmented kernels and memory-bound pipelines that underutilize GPUs. We show that a missing principle is making GNN-MD IO-aware, carefully accounting for reads and writes between GPU high-bandwidth memory (HBM) and on-chip SRAM. We present FlashSchNet, an efficient and accurate IO-aware SchNet-style GNN-MD framework built on four techniques: (1) flash radial basis, which fuses pairwise distance computation, Gaussian basis expansion, and cosine envelope into a single tiled pass, computing each distance once and reusing it across all basis functions; (2) flash message passing, which fuses cutoff, neighbor gather, filter multiplication, and reduction to avoid materializing edge tensors in HBM; (3) flash aggregation, which reformulates scatter-add via CSR segment reduce, reducing atomic writes by a factor of feature dimension and enabling contention-free accumulation in both forward and backward passes; (4) channel-wise 16-bit quantization that exploits the low per-channel dynamic range in SchNet MLP weights to further improve throughput with negligible accuracy loss. On a single NVIDIA RTX PRO 6000, FlashSchNet achieves 1000 ns/day aggregate simulation throughput over 64 parallel replicas on coarse-grained (CG) protein containing 269 beads (6.5x faster than CGSchNet baseline with 80% reduction of peak memory), surpassing classical force fields (e.g. MARTINI) while retaining SchNet-level accuracy and transferability.

