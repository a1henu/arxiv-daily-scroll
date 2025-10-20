---
layout: default
title: Rethinking Efficient Hierarchical Mixing Architecture for Low-light RAW Image Enhancement
---

# Rethinking Efficient Hierarchical Mixing Architecture for Low-light RAW Image Enhancement
**arXiv**：[2510.15497v1](https://arxiv.org/abs/2510.15497) · [PDF](https://arxiv.org/pdf/2510.15497.pdf)  
**作者**：Xianmin Chen, Peiliang Huang, Longfei Han, Dingwen Zhang, Junwei Han  

**一句话要点**：提出HiMA架构以高效增强低光RAW图像

**关键词**：低光图像增强, RAW图像处理, 分层混合架构, Transformer模块, Mamba模块, 多先验融合

## 3 点简述
- 核心问题：低光RAW图像增强需平衡高质量与高效率，现有方法存在局限。
- 方法要点：结合Transformer和Mamba模块，引入LoDA和MPF提升局部适应与细节。
- 实验或效果：在多个数据集上优于SOTA，参数更少，性能更优。

## 摘要（原文）

> Low-light RAW image enhancement remains a challenging task. Although numerous
> deep learning based approaches have been proposed, they still suffer from
> inherent limitations. A key challenge is how to simultaneously achieve strong
> enhancement quality and high efficiency. In this paper, we rethink the
> architecture for efficient low-light image signal processing (ISP) and
> introduce a Hierarchical Mixing Architecture (HiMA). HiMA leverages the
> complementary strengths of Transformer and Mamba modules to handle features at
> large and small scales, respectively, thereby improving efficiency while
> avoiding the ambiguities observed in prior two-stage frameworks. To further
> address uneven illumination with strong local variations, we propose Local
> Distribution Adjustment (LoDA), which adaptively aligns feature distributions
> across different local regions. In addition, to fully exploit the denoised
> outputs from the first stage, we design a Multi-prior Fusion (MPF) module that
> integrates spatial and frequency-domain priors for detail enhancement.
> Extensive experiments on multiple public datasets demonstrate that our method
> outperforms state-of-the-art approaches, achieving superior performance with
> fewer parameters. Code will be released at https://github.com/Cynicarlos/HiMA.

