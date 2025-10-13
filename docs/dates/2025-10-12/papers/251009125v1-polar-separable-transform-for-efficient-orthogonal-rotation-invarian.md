---
layout: default
title: Polar Separable Transform for Efficient Orthogonal Rotation-Invariant Image Representation
---

# Polar Separable Transform for Efficient Orthogonal Rotation-Invariant Image Representation
**arXiv**：[2510.09125v1](https://arxiv.org/abs/2510.09125) · [PDF](https://arxiv.org/pdf/2510.09125.pdf)  
**作者**：Satya P. Singh, Rashmi Chaudhry, Anand Srivastava, Jagath C. Rajapakse  

**一句话要点**：提出PSepT变换以高效实现正交旋转不变图像表示

**关键词**：正交图像表示, 可分离变换, 旋转不变性, 计算效率, 数值稳定性

## 3 点简述
- 经典正交矩方法计算复杂度高且数值不稳定，阻碍高效图像分析
- PSepT通过可分离径向-角向基实现独立处理，大幅降低复杂度与内存需求
- 实验显示PSepT在数值稳定性和分类性能上优于传统方法，支持精确重建

## 摘要（原文）

> Orthogonal moment-based image representations are fundamental in computer
> vision, but classical methods suffer from high computational complexity and
> numerical instability at large orders. Zernike and pseudo-Zernike moments, for
> instance, require coupled radial-angular processing that precludes efficient
> factorization, resulting in $\mathcal{O}(n^3N^2)$ to $\mathcal{O}(n^6N^2)$
> complexity and $\mathcal{O}(N^4)$ condition number scaling for the $n$th-order
> moments on an $N\times N$ image. We introduce \textbf{PSepT} (Polar Separable
> Transform), a separable orthogonal transform that overcomes the
> non-separability barrier in polar coordinates. PSepT achieves complete kernel
> factorization via tensor-product construction of Discrete Cosine Transform
> (DCT) radial bases and Fourier harmonic angular bases, enabling independent
> radial and angular processing. This separable design reduces computational
> complexity to $\mathcal{O}(N^2 \log N)$, memory requirements to
> $\mathcal{O}(N^2)$, and condition number scaling to $\mathcal{O}(\sqrt{N})$,
> representing exponential improvements over polynomial approaches. PSepT
> exhibits orthogonality, completeness, energy conservation, and
> rotation-covariance properties. Experimental results demonstrate better
> numerical stability, computational efficiency, and competitive classification
> performance on structured datasets, while preserving exact reconstruction. The
> separable framework enables high-order moment analysis previously infeasible
> with classical methods, opening new possibilities for robust image analysis
> applications.

