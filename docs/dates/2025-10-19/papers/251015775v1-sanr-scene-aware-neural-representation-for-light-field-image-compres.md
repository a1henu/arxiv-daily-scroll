---
layout: default
title: SANR: Scene-Aware Neural Representation for Light Field Image Compression with Rate-Distortion Optimization
---

# SANR: Scene-Aware Neural Representation for Light Field Image Compression with Rate-Distortion Optimization
**arXiv**：[2510.15775v1](https://arxiv.org/abs/2510.15775) · [PDF](https://arxiv.org/pdf/2510.15775.pdf)  
**作者**：Gai Zhang, Xinfeng Zhang, Lv Tang, Hongyu An, Li Zhang, Qingming Huang  

**一句话要点**：提出SANR以解决光场图像压缩中的场景建模与率失真优化问题

**关键词**：光场图像压缩, 神经表示, 场景建模, 率失真优化, 量化感知训练

## 3 点简述
- 核心问题：光场图像高维数据导致压缩效率低，现有方法忽略场景结构建模。
- 方法要点：引入分层场景建模块，结合熵约束量化感知训练实现端到端优化。
- 实验效果：在率失真性能上显著优于现有技术，BD-rate节省达65.62%。

## 摘要（原文）

> Light field images capture multi-view scene information and play a crucial
> role in 3D scene reconstruction. However, their high-dimensional nature results
> in enormous data volumes, posing a significant challenge for efficient
> compression in practical storage and transmission scenarios. Although neural
> representation-based methods have shown promise in light field image
> compression, most approaches rely on direct coordinate-to-pixel mapping through
> implicit neural representation (INR), often neglecting the explicit modeling of
> scene structure. Moreover, they typically lack end-to-end rate-distortion
> optimization, limiting their compression efficiency. To address these
> limitations, we propose SANR, a Scene-Aware Neural Representation framework for
> light field image compression with end-to-end rate-distortion optimization. For
> scene awareness, SANR introduces a hierarchical scene modeling block that
> leverages multi-scale latent codes to capture intrinsic scene structures,
> thereby reducing the information gap between INR input coordinates and the
> target light field image. From a compression perspective, SANR is the first to
> incorporate entropy-constrained quantization-aware training (QAT) into neural
> representation-based light field image compression, enabling end-to-end
> rate-distortion optimization. Extensive experiment results demonstrate that
> SANR significantly outperforms state-of-the-art techniques regarding
> rate-distortion performance with a 65.62\% BD-rate saving against HEVC.

