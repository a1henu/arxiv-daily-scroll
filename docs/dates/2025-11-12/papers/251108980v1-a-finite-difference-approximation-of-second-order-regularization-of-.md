---
layout: default
title: A Finite Difference Approximation of Second Order Regularization of Neural-SDFs
---

# A Finite Difference Approximation of Second Order Regularization of Neural-SDFs
**arXiv**：[2511.08980v1](https://arxiv.org/abs/2511.08980) · [PDF](https://arxiv.org/pdf/2511.08980.pdf)  
**作者**：Haotian Yin, Aleksander Plocharski, Michal Jan Wlodarczyk, Przemyslaw Musialski  

**一句话要点**：提出有限差分框架以高效正则化神经SDF的曲率

**关键词**：神经符号距离场, 曲率正则化, 有限差分方法, 自动微分, 三维重建, 计算效率

## 3 点简述
- 现有方法使用二阶自动微分计算曲率，计算成本高
- 采用有限差分模板近似二阶导数，降低内存和训练时间
- 实验显示重建质量相当，GPU使用和训练时间减半

## 摘要（原文）

> We introduce a finite-difference framework for curvature regularization in neural signed distance field (SDF) learning. Existing approaches enforce curvature priors using full Hessian information obtained via second-order automatic differentiation, which is accurate but computationally expensive. Others reduced this overhead by avoiding explicit Hessian assembly, but still required higher-order differentiation. In contrast, our method replaces these operations with lightweight finite-difference stencils that approximate second derivatives using the well known Taylor expansion with a truncation error of O(h^2), and can serve as drop-in replacements for Gaussian curvature and rank-deficiency losses. Experiments demonstrate that our finite-difference variants achieve reconstruction fidelity comparable to their automatic-differentiation counterparts, while reducing GPU memory usage and training time by up to a factor of two. Additional tests on sparse, incomplete, and non-CAD data confirm that the proposed formulation is robust and general, offering an efficient and scalable alternative for curvature-aware SDF learning.

