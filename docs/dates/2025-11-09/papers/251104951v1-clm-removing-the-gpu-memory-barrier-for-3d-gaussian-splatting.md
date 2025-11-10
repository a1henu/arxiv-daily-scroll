---
layout: default
title: CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting
---

# CLM: Removing the GPU Memory Barrier for 3D Gaussian Splatting
**arXiv**：[2511.04951v1](https://arxiv.org/abs/2511.04951) · [PDF](https://arxiv.org/pdf/2511.04951.pdf)  
**作者**：Hexu Zhao, Xiwen Min, Xiaoteng Liu, Moonjun Gong, Yiming Li, Ang Li, Saining Xie, Jinyang Li, Aurojit Panda  

**一句话要点**：提出CLM系统以解决3D高斯泼溅在单GPU上渲染大场景的内存限制问题

**关键词**：3D高斯泼溅, GPU内存优化, 卸载策略, 渲染系统, 大场景渲染

## 3 点简述
- 核心问题：3D高斯泼溅在大场景中GPU内存需求高，超出消费级GPU容量。
- 方法要点：通过将高斯数据卸载到CPU内存，仅在需要时加载到GPU，并优化访问模式以减少开销。
- 实验或效果：在RTX4090上成功渲染1亿高斯的大场景，保持高质量重建。

## 摘要（原文）

> 3D Gaussian Splatting (3DGS) is an increasingly popular novel view synthesis
> approach due to its fast rendering time, and high-quality output. However,
> scaling 3DGS to large (or intricate) scenes is challenging due to its large
> memory requirement, which exceed most GPU's memory capacity. In this paper, we
> describe CLM, a system that allows 3DGS to render large scenes using a single
> consumer-grade GPU, e.g., RTX4090. It does so by offloading Gaussians to CPU
> memory, and loading them into GPU memory only when necessary. To reduce
> performance and communication overheads, CLM uses a novel offloading strategy
> that exploits observations about 3DGS's memory access pattern for pipelining,
> and thus overlap GPU-to-CPU communication, GPU computation and CPU computation.
> Furthermore, we also exploit observation about the access pattern to reduce
> communication volume. Our evaluation shows that the resulting implementation
> can render a large scene that requires 100 million Gaussians on a single
> RTX4090 and achieve state-of-the-art reconstruction quality.

