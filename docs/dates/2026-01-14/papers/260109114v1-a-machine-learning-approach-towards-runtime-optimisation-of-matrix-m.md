---
layout: default
title: A Machine Learning Approach Towards Runtime Optimisation of Matrix Multiplication
---

# A Machine Learning Approach Towards Runtime Optimisation of Matrix Multiplication
**arXiv**：[2601.09114v1](https://arxiv.org/abs/2601.09114) · [PDF](https://arxiv.org/pdf/2601.09114.pdf)  
**作者**：Yufan Xia, Marco De La Pierre, Amanda S. Barnard, Giuseppe Maria Junior Barca  

**一句话要点**：提出基于机器学习的运行时优化方法，以自动选择GEMM任务的最优线程数。

**关键词**：矩阵乘法优化, 机器学习应用, 高性能计算, 线程调度, BLAS库

## 3 点简述
- 核心问题：现代多核共享内存系统中，确定最小化多线程GEMM运行时的线程数具有挑战性。
- 方法要点：构建ADSALA软件库，使用机器学习模型动态选择最优线程数。
- 实验或效果：在两种HPC节点架构上测试，相比传统BLAS实现，内存使用100 MB内GEMM加速25%至40%。

## 摘要（原文）

> The GEneral Matrix Multiplication (GEMM) is one of the essential algorithms in scientific computing. Single-thread GEMM implementations are well-optimised with techniques like blocking and autotuning. However, due to the complexity of modern multi-core shared memory systems, it is challenging to determine the number of threads that minimises the multi-thread GEMM runtime. We present a proof-of-concept approach to building an Architecture and Data-Structure Aware Linear Algebra (ADSALA) software library that uses machine learning to optimise the runtime performance of BLAS routines. More specifically, our method uses a machine learning model on-the-fly to automatically select the optimal number of threads for a given GEMM task based on the collected training data. Test results on two different HPC node architectures, one based on a two-socket Intel Cascade Lake and the other on a two-socket AMD Zen 3, revealed a 25 to 40 per cent speedup compared to traditional GEMM implementations in BLAS when using GEMM of memory usage within 100 MB.

