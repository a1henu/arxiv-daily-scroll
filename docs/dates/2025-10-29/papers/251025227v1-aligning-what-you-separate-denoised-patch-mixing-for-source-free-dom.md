---
layout: default
title: Aligning What You Separate: Denoised Patch Mixing for Source-Free Domain Adaptation in Medical Image Segmentation
---

# Aligning What You Separate: Denoised Patch Mixing for Source-Free Domain Adaptation in Medical Image Segmentation
**arXiv**：[2510.25227v1](https://arxiv.org/abs/2510.25227) · [PDF](https://arxiv.org/pdf/2510.25227.pdf)  
**作者**：Quang-Khai Bui-Tran, Thanh-Huy Nguyen, Hoang-Thien Nguyen, Ba-Thinh Lam, Nguyen Lan Vi Vu, Phat K. Huynh, Ulas Bagci, Min Xu  

**一句话要点**：提出基于硬样本选择和去噪补丁混合的源自由域适应方法，用于医学图像分割。

**关键词**：源自由域适应, 医学图像分割, 硬样本选择, 去噪补丁混合, 渐进对齐, 伪标签优化

## 3 点简述
- 源自由域适应中忽略样本难度和噪声监督，导致分割性能下降。
- 通过熵相似性分析划分样本，结合去噪掩码和补丁混合实现渐进对齐。
- 在基准数据集上实现Dice和ASSD指标提升，优于现有方法。

## 摘要（原文）

> Source-Free Domain Adaptation (SFDA) is emerging as a compelling solution for
> medical image segmentation under privacy constraints, yet current approaches
> often ignore sample difficulty and struggle with noisy supervision under domain
> shift. We present a new SFDA framework that leverages Hard Sample Selection and
> Denoised Patch Mixing to progressively align target distributions. First,
> unlabeled images are partitioned into reliable and unreliable subsets through
> entropy-similarity analysis, allowing adaptation to start from easy samples and
> gradually incorporate harder ones. Next, pseudo-labels are refined via Monte
> Carlo-based denoising masks, which suppress unreliable pixels and stabilize
> training. Finally, intra- and inter-domain objectives mix patches between
> subsets, transferring reliable semantics while mitigating noise. Experiments on
> benchmark datasets show consistent gains over prior SFDA and UDA methods,
> delivering more accurate boundary delineation and achieving state-of-the-art
> Dice and ASSD scores. Our study highlights the importance of progressive
> adaptation and denoised supervision for robust segmentation under domain shift.

