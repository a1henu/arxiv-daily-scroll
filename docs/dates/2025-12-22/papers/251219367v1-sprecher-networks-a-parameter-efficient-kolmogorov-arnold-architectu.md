---
layout: default
title: Sprecher Networks: A Parameter-Efficient Kolmogorov-Arnold Architecture
---

# Sprecher Networks: A Parameter-Efficient Kolmogorov-Arnold Architecture
**arXiv**：[2512.19367v1](https://arxiv.org/abs/2512.19367) · [PDF](https://arxiv.org/pdf/2512.19367.pdf)  
**作者**：Christian Hägg, Kathlén Kohn, Giovanni Luca Marchetti, Boris Shapiro  

**一句话要点**：提出Sprecher网络，一种基于Kolmogorov-Arnold-Sprecher构造的参数高效神经网络架构。

**关键词**：参数高效神经网络, Kolmogorov-Arnold构造, 可学习样条, 内存优化, 深度学习架构

## 3 点简述
- 核心问题：传统多层感知机参数效率低，内存占用高，限制模型规模扩展。
- 方法要点：采用共享可学习样条和结构化块，实现参数和内存的线性缩放，支持深层组合。
- 实验或效果：相比MLPs，SNs在参数和内存上更高效，验证了其可行性和性能。

## 摘要（原文）

> We present Sprecher Networks (SNs), a family of trainable neural architectures inspired by the classical Kolmogorov-Arnold-Sprecher (KAS) construction for approximating multivariate continuous functions. Distinct from Multi-Layer Perceptrons (MLPs) with fixed node activations and Kolmogorov-Arnold Networks (KANs) featuring learnable edge activations, SNs utilize shared, learnable splines (monotonic and general) within structured blocks incorporating explicit shift parameters and mixing weights. Our approach directly realizes Sprecher's specific 1965 sum of shifted splines formula in its single-layer variant and extends it to deeper, multi-layer compositions. We further enhance the architecture with optional lateral mixing connections that enable intra-block communication between output dimensions, providing a parameter-efficient alternative to full attention mechanisms. Beyond parameter efficiency with $O(LN + LG)$ scaling (where $G$ is the knot count of the shared splines) versus MLPs' $O(LN^2)$, SNs admit a sequential evaluation strategy that reduces peak forward-intermediate memory from $O(N^2)$ to $O(N)$ (treating batch size as constant), making much wider architectures feasible under memory constraints. We demonstrate empirically that composing these blocks into deep networks leads to highly parameter and memory-efficient models, discuss theoretical motivations, and compare SNs with related architectures (MLPs, KANs, and networks with learnable node activations).

