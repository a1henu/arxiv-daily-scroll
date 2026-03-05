---
layout: default
title: A Hypertoroidal Covering for Perfect Color Equivariance
---

# A Hypertoroidal Covering for Perfect Color Equivariance
**arXiv**：[2603.04256v1](https://arxiv.org/abs/2603.04256) · [PDF](https://arxiv.org/pdf/2603.04256.pdf)  
**作者**：Yulong Yang, Zhikun Xu, Yaojun Li, Christine Allen-Blanchette  

**一句话要点**：提出超环面覆盖方法以实现完美颜色等变性，提升神经网络对颜色变化的鲁棒性。

**关键词**：颜色等变性, 神经网络架构, 超环面覆盖, 细粒度分类, 医学成像, 几何变换

## 3 点简述
- 核心问题：现有颜色等变架构将饱和度和亮度近似为1D平移，导致显著伪影。
- 方法要点：通过将区间值提升到圆上的双覆盖，构建真正等变的表示。
- 实验或效果：在细粒度分类和医学成像任务中优于传统和等变基线，并扩展至尺度变换。

## 摘要（原文）

> When the color distribution of input images changes at inference, the performance of conventional neural network architectures drops considerably. A few researchers have begun to incorporate prior knowledge of color geometry in neural network design. These color equivariant architectures have modeled hue variation with 2D rotations, and saturation and luminance transformations as 1D translations. While this approach improves neural network robustness to color variations in a number of contexts, we find that approximating saturation and luminance (interval valued quantities) as 1D translations introduces appreciable artifacts. In this paper, we introduce a color equivariant architecture that is truly equivariant. Instead of approximating the interval with the real line, we lift values on the interval to values on the circle (a double-cover) and build equivariant representations there. Our approach resolves the approximation artifacts of previous methods, improves interpretability and generalizability, and achieves better predictive performance than conventional and equivariant baselines on tasks such as fine-grained classification and medical imaging tasks. Going beyond the context of color, we show that our proposed lifting can also extend to geometric transformations such as scale.

