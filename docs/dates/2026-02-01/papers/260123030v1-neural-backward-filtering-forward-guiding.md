---
layout: default
title: Neural Backward Filtering Forward Guiding
---

# Neural Backward Filtering Forward Guiding
**arXiv**：[2601.23030v1](https://arxiv.org/abs/2601.23030) · [PDF](https://arxiv.org/pdf/2601.23030.pdf)  
**作者**：Gefan Yang, Frank van der Meulen, Stefan Sommer  

**一句话要点**：提出神经后向滤波前向引导框架，以解决树结构非线性连续随机过程的稀疏观测推理问题。

**关键词**：树结构推理, 非线性随机过程, 后向滤波前向引导, 神经残差学习, 系统发育分析, 高维推理

## 3 点简述
- 核心问题：树结构非线性连续随机过程在稀疏观测下的推理困难，传统方法如Doob's h-变换或粒子方法在高维或复杂拓扑中不适用。
- 方法要点：利用辅助线性高斯过程构建闭式后向滤波器作为引导，结合神经残差（如归一化流或受控SDE）捕获非线性差异，实现无偏路径子采样。
- 实验或效果：在合成基准上优于基线，应用于高维系统发育分析中蝴蝶翅膀形状的重建任务。

## 摘要（原文）

> Inference in non-linear continuous stochastic processes on trees is challenging, particularly when observations are sparse (leaf-only) and the topology is complex. Exact smoothing via Doob's $h$-transform is intractable for general non-linear dynamics, while particle-based methods degrade in high dimensions. We propose Neural Backward Filtering Forward Guiding (NBFFG), a unified framework for both discrete transitions and continuous diffusions. Our method constructs a variational posterior by leveraging an auxiliary linear-Gaussian process. This auxiliary process yields a closed-form backward filter that serves as a ``guide'', steering the generative path toward high-likelihood regions. We then learn a neural residual--parameterized as a normalizing flow or a controlled SDE--to capture the non-linear discrepancies. This formulation allows for an unbiased path-wise subsampling scheme, reducing the training complexity from tree-size dependent to path-length dependent. Empirical results show that NBFFG outperforms baselines on synthetic benchmarks, and we demonstrate the method on a high-dimensional inference task in phylogenetic analysis with reconstruction of ancestral butterfly wing shapes.

