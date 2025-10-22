---
layout: default
title: SSD: Spatial-Semantic Head Decoupling for Efficient Autoregressive Image Generation
---

# SSD: Spatial-Semantic Head Decoupling for Efficient Autoregressive Image Generation
**arXiv**：[2510.18716v1](https://arxiv.org/abs/2510.18716) · [PDF](https://arxiv.org/pdf/2510.18716.pdf)  
**作者**：Siyong Jian, Huan Wang  

**一句话要点**：提出空间-语义头解耦KV缓存压缩框架，以高效自回归图像生成。

**关键词**：自回归图像生成, KV缓存压缩, 注意力头解耦, 空间局部性, 语义汇, 高效计算

## 3 点简述
- 自回归图像生成模型内存和计算成本高，KV缓存压缩在图像领域未充分探索。
- 方法基于空间局部性和语义汇现象，将注意力头解耦为空间和语义类型进行压缩。
- 实验显示内存使用减少5倍，吞吐量提升6.6倍，视觉质量损失极小。

## 摘要（原文）

> Autoregressive image generation models like Janus-Pro produce high-quality
> images, but at the significant cost of high memory and ever-growing
> computational demands due to the large number of visual tokens. While KV cache
> compression has been extensively studied in language modeling, it still remains
> largely unexplored for the image generation domain. In this work, we begin by
> identifying a distinct and prominent attention phenomenon, which we term
> spatial locality and emergent semantic sink. To leverage this key insight, we
> introduce a novel KV cache compression framework. Specifically, we compress the
> KV cache for all visual tokens by adaptively decoupling attention heads into
> two separate types: for spatial-locality heads, our method maintains a short
> recent token window; for semantic-sink heads, it strategically preserves a
> compact set of highly-attended tokens. Our extensive experiments demonstrate
> that the proposed method achieves a 5$\times$ reduction in memory usage and a
> notable 6.6$\times$ speedup in overall throughput with only minimal visual
> quality loss, thereby enabling highly efficient native autoregressive image
> generation on resource-constrained hardware.

