---
layout: default
title: Polaffini: A feature-based approach for robust affine and polyaffine image registration
---

# Polaffini: A feature-based approach for robust affine and polyaffine image registration
**arXiv**：[2602.17337v1](https://arxiv.org/abs/2602.17337) · [PDF](https://arxiv.org/pdf/2602.17337.pdf)  
**作者**：Antoine Legouhy, Cosimo Campo, Ross Callaghan, Hojjat Azadbakht, Hui Zhang  

**一句话要点**：提出Polaffini框架，利用深度学习分割特征点实现稳健的仿射与多仿射医学图像配准。

**关键词**：医学图像配准, 特征点配准, 仿射变换, 多仿射变换, 深度学习分割, 解剖学配准

## 3 点简述
- 核心问题：传统基于强度的医学图像配准方法依赖对齐质量的替代度量，而基于特征的方法因特征提取困难未广泛应用。
- 方法要点：利用预训练分割模型获取解剖区域质心作为特征点，通过闭式解实现高效全局与局部仿射匹配，并扩展至可调平滑度的多仿射变换。
- 实验或效果：Polaffini在结构对齐上优于主流基于强度方法，并提升后续非线性配准的初始化效果，具有快速、稳健和准确的特点。

## 摘要（原文）

> In this work we present Polaffini, a robust and versatile framework for anatomically grounded registration. Medical image registration is dominated by intensity-based registration methods that rely on surrogate measures of alignment quality. In contrast, feature-based approaches that operate by identifying explicit anatomical correspondences, while more desirable in theory, have largely fallen out of favor due to the challenges of reliably extracting features. However, such challenges are now significantly overcome thanks to recent advances in deep learning, which provide pre-trained segmentation models capable of instantly delivering reliable, fine-grained anatomical delineations. We aim to demonstrate that these advances can be leveraged to create new anatomically-grounded image registration algorithms. To this end, we propose Polaffini, which obtains, from these segmented regions, anatomically grounded feature points with 1-to-1 correspondence in a particularly simple way: extracting their centroids. These enable efficient global and local affine matching via closed-form solutions. Those are used to produce an overall transformation ranging from affine to polyaffine with tunable smoothness. Polyaffine transformations can have many more degrees of freedom than affine ones allowing for finer alignment, and their embedding in the log-Euclidean framework ensures diffeomorphic properties. Polaffini has applications both for standalone registration and as pre-alignment for subsequent non-linear registration, and we evaluate it against popular intensity-based registration techniques. Results demonstrate that Polaffini outperforms competing methods in terms of structural alignment and provides improved initialisation for downstream non-linear registration. Polaffini is fast, robust, and accurate, making it particularly well-suited for integration into medical image processing pipelines.

