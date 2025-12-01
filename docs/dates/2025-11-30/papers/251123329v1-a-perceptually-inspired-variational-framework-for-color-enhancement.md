---
layout: default
title: A Perceptually Inspired Variational Framework for Color Enhancement
---

# A Perceptually Inspired Variational Framework for Color Enhancement
**arXiv**：[2511.23329v1](https://arxiv.org/abs/2511.23329) · [PDF](https://arxiv.org/pdf/2511.23329.pdf)  
**作者**：Rodrigo Palma-Amestoy, Edoardo Provenzi, Marcelo Bertalmío, Vicent Caselles  

**一句话要点**：提出基于感知启发的变分框架以增强图像色彩对比度

**关键词**：色彩增强, 变分框架, 感知启发, 对比度优化, 计算复杂度优化

## 3 点简述
- 核心问题：现有色彩校正模型在对比度和色散等图像特征上的行为难以表征
- 方法要点：基于颜色感知现象学设计变分能量函数，满足感知启发的基本要求
- 实验或效果：通过梯度下降计算能量最小值，并优化算法复杂度从O(N²)降至O(N log N)

## 摘要（原文）

> Basic phenomenology of human color vision has been widely taken as an inspiration to devise explicit color correction algorithms. The behavior of these models in terms of significative image features (such as contrast and dispersion) can be difficult to characterize. To cope with this, we propose to use a variational formulation of color contrast enhancement that is inspired by the basic phenomenology of color perception. In particular, we devise a set of basic requirements to be fulfilled by an energy to be considered as `perceptually inspired', showing that there is an explicit class of functionals satisfying all of them. We single out three explicit functionals that we consider of basic interest, showing similarities and differences with existing models. The minima of such functionals is computed using a gradient descent approach. We also present a general methodology to reduce the computational cost of the algorithms under analysis from ${\cal O}(N^2)$ to ${\cal O}(N\log N)$, being $N$ the number of input pixels.

