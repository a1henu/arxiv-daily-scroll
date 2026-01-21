---
layout: default
title: torch-sla: Differentiable Sparse Linear Algebra with Adjoint Solvers and Sparse Tensor Parallelism for PyTorch
---

# torch-sla: Differentiable Sparse Linear Algebra with Adjoint Solvers and Sparse Tensor Parallelism for PyTorch
**arXiv**：[2601.13994v1](https://arxiv.org/abs/2601.13994) · [PDF](https://arxiv.org/pdf/2601.13994.pdf)  
**作者**：Mingyuan Chi  

**一句话要点**：提出torch-sla库以解决PyTorch中GPU加速、可扩展和可微稀疏线性代数计算问题

**关键词**：稀疏线性代数, GPU加速, 可微计算, 多GPU并行, PyTorch库

## 3 点简述
- 核心问题：工业科学计算中稀疏矩阵处理缺乏高效、可微的GPU加速解决方案
- 方法要点：提供GPU加速稀疏求解器、多GPU域分解并行和伴随微分优化计算图
- 实验或效果：在3个GPU上实现4亿自由度线性求解，计算图节点和内存开销独立于迭代次数

## 摘要（原文）

> Industrial scientific computing predominantly uses sparse matrices to represent unstructured data -- finite element meshes, graphs, point clouds. We present \torchsla{}, an open-source PyTorch library that enables GPU-accelerated, scalable, and differentiable sparse linear algebra. The library addresses three fundamental challenges: (1) GPU acceleration for sparse linear solves, nonlinear solves (Newton, Picard, Anderson), and eigenvalue computation; (2) Multi-GPU scaling via domain decomposition with halo exchange, reaching \textbf{400 million DOF linear solve on 3 GPUs}; and (3) Adjoint-based differentiation} achieving $\mathcal{O}(1)$ computational graph nodes (for autograd) and $\mathcal{O}(\text{nnz})$ memory -- independent of solver iterations. \torchsla{} supports multiple backends (SciPy, cuDSS, PyTorch-native) and seamlessly integrates with PyTorch autograd for end-to-end differentiable simulations. Code is available at https://github.com/walkerchi/torch-sla.

