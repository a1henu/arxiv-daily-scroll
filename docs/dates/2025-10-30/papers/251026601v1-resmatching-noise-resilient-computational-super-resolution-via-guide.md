---
layout: default
title: ResMatching: Noise-Resilient Computational Super-Resolution via Guided Conditional Flow Matching
---

# ResMatching: Noise-Resilient Computational Super-Resolution via Guided Conditional Flow Matching
**arXiv**：[2510.26601v1](https://arxiv.org/abs/2510.26601) · [PDF](https://arxiv.org/pdf/2510.26601.pdf)  
**作者**：Anirban Ray, Vera Galinova, Florian Jug  

**一句话要点**：提出ResMatching方法，利用引导条件流匹配实现噪声鲁棒的计算超分辨率

**关键词**：计算超分辨率, 引导条件流匹配, 噪声鲁棒性, 荧光显微镜, 数据不确定性

## 3 点简述
- 核心问题：荧光显微镜计算超分辨率是病态问题，需学习先验以推断未成像频率
- 方法要点：使用引导条件流匹配学习数据先验，提升噪声场景下的性能
- 实验或效果：在BioSR数据集上优于7个基线，平衡数据保真度与感知真实性

## 摘要（原文）

> Computational Super-Resolution (CSR) in fluorescence microscopy has, despite
> being an ill-posed problem, a long history. At its very core, CSR is about
> finding a prior that can be used to extrapolate frequencies in a micrograph
> that have never been imaged by the image-generating microscope. It stands to
> reason that, with the advent of better data-driven machine learning techniques,
> stronger prior can be learned and hence CSR can lead to better results. Here,
> we present ResMatching, a novel CSR method that uses guided conditional flow
> matching to learn such improved data-priors. We evaluate ResMatching on 4
> diverse biological structures from the BioSR dataset and compare its results
> against 7 baselines. ResMatching consistently achieves competitive results,
> demonstrating in all cases the best trade-off between data fidelity and
> perceptual realism. We observe that CSR using ResMatching is particularly
> effective in cases where a strong prior is hard to learn, e.g. when the given
> low-resolution images contain a lot of noise. Additionally, we show that
> ResMatching can be used to sample from an implicitly learned posterior
> distribution and that this distribution is calibrated for all tested use-cases,
> enabling our method to deliver a pixel-wise data-uncertainty term that can
> guide future users to reject uncertain predictions.

