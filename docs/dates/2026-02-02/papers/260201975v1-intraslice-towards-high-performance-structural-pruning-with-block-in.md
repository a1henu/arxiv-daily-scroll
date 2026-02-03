---
layout: default
title: IntraSlice: Towards High-Performance Structural Pruning with Block-Intra PCA for LLMs
---

# IntraSlice: Towards High-Performance Structural Pruning with Block-Intra PCA for LLMs
**arXiv**：[2602.01975v1](https://arxiv.org/abs/2602.01975) · [PDF](https://arxiv.org/pdf/2602.01975.pdf)  
**作者**：Meng Li, Peisong Wang, Yuantian Shao, Qinghao Hu, Hongjian Fang, Yifan Zhang, Zhihui Wei, Jian Cheng  

**一句话要点**：提出IntraSlice框架，通过块内PCA压缩剪枝解决大语言模型结构化剪枝中的性能下降问题。

**关键词**：大语言模型剪枝, 结构化剪枝, PCA压缩, Transformer优化, 模型加速

## 3 点简述
- 核心问题：结构化剪枝虽能加速大语言模型，但导致显著性能下降，现有PCA方法因模块间应用引入额外参数并破坏激活分布。
- 方法要点：设计块内PCA压缩剪枝，利用Transformer结构特性实现近似PCA，变换矩阵可无参融合，并引入基于PCA的全局剪枝比估计器。
- 实验或效果：在Llama2、Llama3和Phi系列模型上验证，相同压缩比或推理速度下优于基线方法。

## 摘要（原文）

> Large Language Models (LLMs) achieve strong performance across diverse tasks but face deployment challenges due to their massive size. Structured pruning offers acceleration benefits but leads to significant performance degradation. Recent PCA-based pruning methods have alleviated this issue by retaining key activation components, but are only applied between modules in order to fuse the transformation matrix, which introduces extra parameters and severely disrupts activation distributions due to residual connections. To address these issues, we propose IntraSlice, a framework that applies block-wise module-intra PCA compression pruning. By leveraging the structural characteristics of Transformer modules, we design an approximate PCA method whose transformation matrices can be fully fused into the model without additional parameters. We also introduce a PCA-based global pruning ratio estimator that further considers the distribution of compressed activations, building on conventional module importance. We validate our method on Llama2, Llama3, and Phi series across various language benchmarks. Experimental results demonstrate that our approach achieves superior compression performance compared to recent baselines at the same compression ratio or inference speed.

