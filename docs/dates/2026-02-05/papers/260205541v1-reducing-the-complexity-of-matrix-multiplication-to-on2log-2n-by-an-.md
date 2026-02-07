---
layout: default
title: Reducing the Complexity of Matrix Multiplication to $O(N^2log_2N)$ by an Asymptotically Optimal Quantum Algorithm
---

# Reducing the Complexity of Matrix Multiplication to $O(N^2log_2N)$ by an Asymptotically Optimal Quantum Algorithm
**arXiv**：[2602.05541v1](https://arxiv.org/abs/2602.05541) · [PDF](https://arxiv.org/pdf/2602.05541.pdf)  
**作者**：Jiaqi Yao, Ding Liu  

**一句话要点**：提出量子核矩阵乘法算法，以降低大规模矩阵乘法复杂度至O(N²log₂N)。

**关键词**：量子计算, 矩阵乘法, 算法复杂度, 机器学习, 量子模拟

## 3 点简述
- 核心问题：经典矩阵乘法在大规模机器学习中效率受限，复杂度为O(N^{2.371552})。
- 方法要点：利用量子计算的并行性和指数存储，设计量子核算法实现O(N²log₂N)的渐近最优复杂度。
- 实验或效果：通过无噪声和含噪声量子模拟，验证算法在运行时间和稳定性上的实际优势。

## 摘要（原文）

> Matrix multiplication is a fundamental classical computing operation whose efficiency becomes a major challenge at scale, especially for machine learning applications. Quantum computing, with its inherent parallelism and exponential storage capacity, offers a potential solution to these limitations. This work presents a quantum kernel-based matrix multiplication algorithm (QKMM) that achieves an asymptotically optimal computational complexity of $ O(N^2 \log_2 N) $, outperforming the classical optimal complexity of $ O(N^{2.371552}) $, where $N$ denotes the matrix dimension. Through noiseless and noisy quantum simulation experiments, we demonstrate that the proposed algorithm not only exhibits superior theoretical efficiency but also shows practical advantages in runtime performance and stability.

