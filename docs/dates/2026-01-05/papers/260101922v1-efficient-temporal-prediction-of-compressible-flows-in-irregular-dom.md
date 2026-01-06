---
layout: default
title: Efficient temporal prediction of compressible flows in irregular domains using Fourier neural operators
---

# Efficient temporal prediction of compressible flows in irregular domains using Fourier neural operators
**arXiv**：[2601.01922v1](https://arxiv.org/abs/2601.01922) · [PDF](https://arxiv.org/pdf/2601.01922.pdf)  
**作者**：Yifan Nie, Qiaoxin Li  

**一句话要点**：提出基于傅里叶神经算子的高效时间预测方法，用于不规则域中高速可压缩流体的演化模拟。

**关键词**：傅里叶神经算子, 可压缩流体模拟, 不规则流场, 时间序列预测, 循环神经网络

## 3 点简述
- 研究不规则流场中高速可压缩流体的时间演化问题，传统数值方法效率较低。
- 采用傅里叶神经算子处理不规则点集，结合循环神经网络和复合损失函数进行多步预测。
- 在多种不规则流场实验中，方法在计算效率上显著超越传统方法，同时保持高精度。

## 摘要（原文）

> This paper investigates the temporal evolution of high-speed compressible fluids in irregular flow fields using the Fourier Neural Operator (FNO). We reconstruct the irregular flow field point set into sequential format compatible with FNO input requirements, and then embed temporal bundling technique within a recurrent neural network (RNN) for multi-step prediction. We further employ a composite loss function to balance errors across different physical quantities. Experiments are conducted on three different types of irregular flow fields, including orthogonal and non-orthogonal grid configurations. Then we comprehensively analyze the physical component loss curves, flow field visualizations, and physical profiles. Results demonstrate that our approach significantly surpasses traditional numerical methods in computational efficiency while achieving high accuracy, with maximum relative $L_2$ errors of (0.78, 0.57, 0.35)% for ($p$, $T$, $\mathbf{u}$) respectively. This verifies that the method can efficiently and accurately simulate the temporal evolution of high-speed compressible flows in irregular domains.

