---
layout: default
title: Compressed BC-LISTA via Low-Rank Convolutional Decomposition
---

# Compressed BC-LISTA via Low-Rank Convolutional Decomposition
**arXiv**：[2601.23148v1](https://arxiv.org/abs/2601.23148) · [PDF](https://arxiv.org/pdf/2601.23148.pdf)  
**作者**：Han Wang, Yhonatan Kvich, Eduardo Pérez, Florian Römer, Yonina C. Eldar  

**一句话要点**：提出基于低秩卷积分解的压缩BC-LISTA，用于多通道成像的稀疏信号恢复，减少参数并提升重建精度。

**关键词**：稀疏信号恢复, 低秩卷积分解, 压缩测量模型, 多通道成像, LISTA网络, 正交匹配追踪

## 3 点简述
- 研究多通道成像中压缩前向/后向算子的稀疏信号恢复方法，以保持重建准确性。
- 基于低秩CNN分解提出压缩块卷积测量模型，使用OMP选择基滤波器并计算线性混合系数。
- 在模拟多通道超声成像中，C-BC-LISTA相比SOTA方法参数更少、模型更小，且重建精度更高。

## 摘要（原文）

> We study Sparse Signal Recovery (SSR) methods for multichannel imaging with compressed {forward and backward} operators that preserve reconstruction accuracy. We propose a Compressed Block-Convolutional (C-BC) measurement model based on a low-rank Convolutional Neural Network (CNN) decomposition that is analytically initialized from a low-rank factorization of physics-derived forward/backward operators in time delay-based measurements. We use Orthogonal Matching Pursuit (OMP) to select a compact set of basis filters from the analytic model and compute linear mixing coefficients to approximate the full model. We consider the Learned Iterative Shrinkage-Thresholding Algorithm (LISTA) network as a representative example for which the C-BC-LISTA extension is presented. In simulated multichannel ultrasound imaging across multiple Signal-to-Noise Ratios (SNRs), C-BC-LISTA requires substantially fewer parameters and smaller model size than other state-of-the-art (SOTA) methods while improving reconstruction accuracy. In ablations over OMP, Singular Value Decomposition (SVD)-based, and random initializations, OMP-initialized structured compression performs best, yielding the most efficient training and the best performance.

