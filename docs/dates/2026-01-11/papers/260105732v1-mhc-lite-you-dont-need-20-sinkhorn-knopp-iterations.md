---
layout: default
title: mHC-lite: You Don't Need 20 Sinkhorn-Knopp Iterations
---

# mHC-lite: You Don't Need 20 Sinkhorn-Knopp Iterations
**arXiv**：[2601.05732v1](https://arxiv.org/abs/2601.05732) · [PDF](https://arxiv.org/pdf/2601.05732.pdf)  
**作者**：Yongyi Yang, Jianyang Gao  

**一句话要点**：提出mHC-lite，通过凸组合置换矩阵构造双随机矩阵，解决超连接训练不稳定和实现复杂性问题。

**关键词**：超连接, 双随机矩阵, 训练稳定性, 神经网络优化, 重参数化, 置换矩阵

## 3 点简述
- 超连接中动态残差矩阵未约束导致训练不稳定，mHC的Sinkhorn-Knopp迭代存在近似误差和工程障碍。
- mHC-lite基于Birkhoff-von Neumann定理，将双随机矩阵重参数化为置换矩阵的凸组合，保证精确性且易于实现。
- 实验显示mHC-lite性能匹配或优于mHC，提高训练吞吐量，消除HC和mHC的残余不稳定性。

## 摘要（原文）

> Hyper-Connections (HC) generalizes residual connections by introducing dynamic residual matrices that mix information across multiple residual streams, accelerating convergence in deep neural networks. However, unconstrained residual matrices can compromise training stability. To address this, DeepSeek's Manifold-Constrained Hyper-Connections (mHC) approximately projects these matrices onto the Birkhoff polytope via iterative Sinkhorn--Knopp (SK) normalization. We identify two limitations of this approach: (i) finite SK iterations do not guarantee exact doubly stochasticity, leaving an approximation gap that can accumulate through network depth and undermine stability; (ii) efficient SK implementation requires highly specialized CUDA kernels, raising engineering barriers and reducing portability. Motivated by the Birkhoff--von Neumann theorem, we propose mHC-lite, a simple reparameterization that explicitly constructs doubly stochastic matrices as convex combinations of permutation matrices. This approach guarantees exact doubly stochasticity by construction and can be implemented using only native matrix operations. Extensive experiments demonstrate that mHC-lite matches or exceeds mHC in performance while achieving higher training throughput with a naive implementation and eliminating the residual instabilities observed in both HC and mHC. The code is publicly available at https://github.com/FFTYYY/mhc-lite.

