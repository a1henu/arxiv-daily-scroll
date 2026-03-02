---
layout: default
title: Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives
---

# Prune Wisely, Reconstruct Sharply: Compact 3D Gaussian Splatting via Adaptive Pruning and Difference-of-Gaussian Primitives
**arXiv**：[2602.24136v1](https://arxiv.org/abs/2602.24136) · [PDF](https://arxiv.org/pdf/2602.24136.pdf)  
**作者**：Haoran Wang, Guoxi Huang, Fan Zhang, David Bull, Nantheera Anantrasirichai  

**一句话要点**：提出自适应剪枝与差分高斯基元以压缩3D高斯溅射模型，提升紧凑性与渲染质量。

**关键词**：3D高斯溅射, 模型剪枝, 自适应优化, 差分高斯基元, 紧凑表示, 实时渲染

## 3 点简述
- 核心问题：3D高斯溅射模型需大量基元实现高保真，导致冗余和资源消耗高，限制复杂场景扩展。
- 方法要点：集成重建感知的自适应剪枝策略，基于重建质量动态确定剪枝时机和细化间隔；引入3D差分高斯基元，在单个基元中联合建模正负密度，提升紧凑配置下的表达能力。
- 实验或效果：显著提升模型紧凑性，高斯数量减少高达90%，视觉质量与或优于先进方法。

## 摘要（原文）

> Recent significant advances in 3D scene representation have been driven by 3D Gaussian Splatting (3DGS), which has enabled real-time rendering with photorealistic quality. 3DGS often requires a large number of primitives to achieve high fidelity, leading to redundant representations and high resource consumption, thereby limiting its scalability for complex or large-scale scenes. Consequently, effective pruning strategies and more expressive primitives that can reduce redundancy while preserving visual quality are crucial for practical deployment. We propose an efficient, integrated reconstruction-aware pruning strategy that adaptively determines pruning timing and refining intervals based on reconstruction quality, thus reducing model size while enhancing rendering quality. Moreover, we introduce a 3D Difference-of-Gaussians primitive that jointly models both positive and negative densities in a single primitive, improving the expressiveness of Gaussians under compact configurations. Our method significantly improves model compactness, achieving up to 90\% reduction in Gaussian-count while delivering visual quality that is similar to, or in some cases better than, that produced by state-of-the-art methods. Code will be made publicly available.

