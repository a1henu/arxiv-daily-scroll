---
layout: default
title: Neural Posterior Estimation for Cataloging Astronomical Images from the Legacy Survey of Space and Time
---

# Neural Posterior Estimation for Cataloging Astronomical Images from the Legacy Survey of Space and Time
**arXiv**：[2510.15315v1](https://arxiv.org/abs/2510.15315) · [PDF](https://arxiv.org/pdf/2510.15315.pdf)  
**作者**：Yicun Duan, Xinyue Li, Camille Avestruz, Jeffrey Regier  

**一句话要点**：提出神经后验估计方法以解决LSST天文图像编目中的统计一致性问题

**关键词**：神经后验估计, 天文图像编目, 贝叶斯推断, 深度学习, LSST数据, 模拟评估

## 3 点简述
- 传统天文图像编目方法缺乏统计一致性，现有概率方法计算效率低或不准确
- 采用神经后验估计，利用深度学习实现高效准确的后验近似
- 在模拟LSST数据上评估，NPE在检测、测量和分类方面优于标准方法

## 摘要（原文）

> The Vera C. Rubin Observatory Legacy Survey of Space and Time (LSST) will
> commence full-scale operations in 2026, yielding an unprecedented volume of
> astronomical images. Constructing an astronomical catalog, a table of imaged
> stars, galaxies, and their properties, is a fundamental step in most scientific
> workflows based on astronomical image data. Traditional deterministic
> cataloging methods lack statistical coherence as cataloging is an ill-posed
> problem, while existing probabilistic approaches suffer from computational
> inefficiency, inaccuracy, or the inability to perform inference with multiband
> coadded images, the primary output format for LSST images. In this article, we
> explore a recently developed Bayesian inference method called neural posterior
> estimation (NPE) as an approach to cataloging. NPE leverages deep learning to
> achieve both computational efficiency and high accuracy. When evaluated on the
> DC2 Simulated Sky Survey -- a highly realistic synthetic dataset designed to
> mimic LSST data -- NPE systematically outperforms the standard LSST pipeline in
> light source detection, flux measurement, star/galaxy classification, and
> galaxy shape measurement. Additionally, NPE provides well-calibrated posterior
> approximations. These promising results, obtained using simulated data,
> illustrate the potential of NPE in the absence of model misspecification.
> Although some degree of model misspecification is inevitable in the application
> of NPE to real LSST images, there are a variety of strategies to mitigate its
> effects.

