---
layout: default
title: LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting
---

# LL-GaussianImage: Efficient Image Representation for Zero-shot Low-Light Enhancement with 2D Gaussian Splatting
**arXiv**：[2601.15772v1](https://arxiv.org/abs/2601.15772) · [PDF](https://arxiv.org/pdf/2601.15772.pdf)  
**作者**：Yuhan Chen, Wenxuan Yu, Guofa Li, Yijun Xu, Ying Fang, Yicui Shi, Long Cao, Wenbo Chu, Keqiang Li  

**一句话要点**：提出LL-GaussianImage，在2D高斯泼溅压缩域内实现零样本低光增强

**关键词**：2D高斯泼溅, 低光增强, 零样本学习, 压缩域处理, 专家混合框架, 多目标优化

## 3 点简述
- 现有低光增强算法需解压-增强-再压缩流程，效率低且易引入二次退化
- 设计语义引导的专家混合增强框架，直接在2DGS稀疏属性空间进行动态自适应变换
- 通过多目标协同损失和两阶段优化，在保持高压缩比的同时提升视觉质量

## 摘要（原文）

> 2D Gaussian Splatting (2DGS) is an emerging explicit scene representation method with significant potential for image compression due to high fidelity and high compression ratios. However, existing low-light enhancement algorithms operate predominantly within the pixel domain. Processing 2DGS-compressed images necessitates a cumbersome decompression-enhancement-recompression pipeline, which compromises efficiency and introduces secondary degradation. To address these limitations, we propose LL-GaussianImage, the first zero-shot unsupervised framework designed for low-light enhancement directly within the 2DGS compressed representation domain. Three primary advantages are offered by this framework. First, a semantic-guided Mixture-of-Experts enhancement framework is designed. Dynamic adaptive transformations are applied to the sparse attribute space of 2DGS using rendered images as guidance to enable compression-as-enhancement without full decompression to a pixel grid. Second, a multi-objective collaborative loss function system is established to strictly constrain smoothness and fidelity during enhancement, suppressing artifacts while improving visual quality. Third, a two-stage optimization process is utilized to achieve reconstruction-as-enhancement. The accuracy of the base representation is ensured through single-scale reconstruction and network robustness is enhanced. High-quality enhancement of low-light images is achieved while high compression ratios are maintained. The feasibility and superiority of the paradigm for direct processing within the compressed representation domain are validated through experimental results.

