---
layout: default
title: BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU
---

# BalanceGS: Algorithm-System Co-design for Efficient 3D Gaussian Splatting Training on GPU
**arXiv**：[2510.14564v1](https://arxiv.org/abs/2510.14564) · [PDF](https://arxiv.org/pdf/2510.14564.pdf)  
**作者**：Junyi Wu, Jiaming Xu, Jinhao Li, Yongkang Zhou, Jiayi Pan, Xingyang Li, Guohao Dai  

**一句话要点**：提出BalanceGS以解决3D高斯泼溅训练中的效率问题

**关键词**：3D高斯泼溅, 算法系统协同设计, GPU训练优化, 内存访问优化, 计算负载平衡

## 3 点简述
- 核心问题：传统3DGS训练存在密度分配不均、计算负载不平衡和内存访问碎片化
- 方法要点：算法层启发式密度控制，系统层相似性采样合并，映射层重排序内存访问
- 实验或效果：在A100 GPU上训练速度提升1.44倍，质量损失可忽略

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) has emerged as a promising 3D reconstruction
> technique. The traditional 3DGS training pipeline follows three sequential
> steps: Gaussian densification, Gaussian projection, and color splatting.
> Despite its promising reconstruction quality, this conventional approach
> suffers from three critical inefficiencies: (1) Skewed density allocation
> during Gaussian densification, (2) Imbalanced computation workload during
> Gaussian projection and (3) Fragmented memory access during color splatting.
>   To tackle the above challenges, we introduce BalanceGS, the algorithm-system
> co-design for efficient training in 3DGS. (1) At the algorithm level, we
> propose heuristic workload-sensitive Gaussian density control to automatically
> balance point distributions - removing 80% redundant Gaussians in dense regions
> while filling gaps in sparse areas. (2) At the system level, we propose
> Similarity-based Gaussian sampling and merging, which replaces the static
> one-to-one thread-pixel mapping with adaptive workload distribution - threads
> now dynamically process variable numbers of Gaussians based on local cluster
> density. (3) At the mapping level, we propose reordering-based memory access
> mapping strategy that restructures RGB storage and enables batch loading in
> shared memory.
>   Extensive experiments demonstrate that compared with 3DGS, our approach
> achieves a 1.44$\times$ training speedup on a NVIDIA A100 GPU with negligible
> quality degradation.

