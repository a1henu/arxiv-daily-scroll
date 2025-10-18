---
layout: default
title: Terra: Explorable Native 3D World Model with Point Latents
---

# Terra: Explorable Native 3D World Model with Point Latents
**arXiv**：[2510.14977v1](https://arxiv.org/abs/2510.14977) · [PDF](https://arxiv.org/pdf/2510.14977.pdf)  
**作者**：Yuanhui Huang, Weiliang Chen, Wenzhao Zheng, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  

**一句话要点**：提出Terra原生3D世界模型，以点潜在表示解决3D一致性与建模效率问题

**关键词**：3D世界模型, 点潜在表示, 高斯基元, 变分自编码器, 流匹配网络, 多视角一致性

## 3 点简述
- 现有世界模型依赖像素对齐表示，忽略物理世界3D本质，影响一致性与效率
- 引入P2G-VAE编码3D输入为点潜在，解码为高斯基元；SPFlow网络生成点潜在
- 在ScanNet v2上实验，实现多视角一致、任意视角渲染，重建与生成性能领先

## 摘要（原文）

> World models have garnered increasing attention for comprehensive modeling of
> the real world. However, most existing methods still rely on pixel-aligned
> representations as the basis for world evolution, neglecting the inherent 3D
> nature of the physical world. This could undermine the 3D consistency and
> diminish the modeling efficiency of world models. In this paper, we present
> Terra, a native 3D world model that represents and generates explorable
> environments in an intrinsic 3D latent space. Specifically, we propose a novel
> point-to-Gaussian variational autoencoder (P2G-VAE) that encodes 3D inputs into
> a latent point representation, which is subsequently decoded as 3D Gaussian
> primitives to jointly model geometry and appearance. We then introduce a sparse
> point flow matching network (SPFlow) for generating the latent point
> representation, which simultaneously denoises the positions and features of the
> point latents. Our Terra enables exact multi-view consistency with native 3D
> representation and architecture, and supports flexible rendering from any
> viewpoint with only a single generation process. Furthermore, Terra achieves
> explorable world modeling through progressive generation in the point latent
> space. We conduct extensive experiments on the challenging indoor scenes from
> ScanNet v2. Terra achieves state-of-the-art performance in both reconstruction
> and generation with high 3D consistency.

