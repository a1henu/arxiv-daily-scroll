---
layout: default
title: Binary Quadratic Quantization: Beyond First-Order Quantization for Real-Valued Matrix Compression
---

# Binary Quadratic Quantization: Beyond First-Order Quantization for Real-Valued Matrix Compression
**arXiv**：[2510.18650v1](https://arxiv.org/abs/2510.18650) · [PDF](https://arxiv.org/pdf/2510.18650.pdf)  
**作者**：Kyo Kuroki, Yasuyuki Okoshi, Thiem Van Chu, Kazushi Kawamura, Masato Motomura  

**一句话要点**：提出二进制二次量化方法，用于高效矩阵压缩和神经网络量化。

**关键词**：矩阵量化, 二进制二次表达式, 后训练量化, 矩阵压缩, 神经网络压缩

## 3 点简述
- 传统一阶量化方法通过线性组合二进制基近似矩阵，表达力有限。
- BQQ利用二进制二次表达式增强表达力，保持紧凑数据格式。
- 实验显示在矩阵压缩和视觉Transformer后训练量化中，BQQ优于现有方法。

## 摘要（原文）

> This paper proposes a novel matrix quantization method, Binary Quadratic
> Quantization (BQQ). In contrast to conventional first-order quantization
> approaches, such as uniform quantization and binary coding quantization, that
> approximate real-valued matrices via linear combinations of binary bases, BQQ
> leverages the expressive power of binary quadratic expressions while
> maintaining an extremely compact data format. We validate our approach with two
> experiments: a matrix compression benchmark and post-training quantization
> (PTQ) on pretrained Vision Transformer-based models. Experimental results
> demonstrate that BQQ consistently achieves a superior trade-off between memory
> efficiency and reconstruction error than conventional methods for compressing
> diverse matrix data. It also delivers strong PTQ performance, even though we
> neither target state-of-the-art PTQ accuracy under tight memory constraints nor
> rely on PTQ-specific binary matrix optimization. For example, our proposed
> method outperforms the state-of-the-art PTQ method by up to 2.2\% and 59.1% on
> the ImageNet dataset under the calibration-based and data-free scenarios,
> respectively, with quantization equivalent to 2 bits. These findings highlight
> the surprising effectiveness of binary quadratic expressions for efficient
> matrix approximation and neural network compression.

