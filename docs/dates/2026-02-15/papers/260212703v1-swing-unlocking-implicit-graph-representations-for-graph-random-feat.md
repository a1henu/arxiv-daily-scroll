---
layout: default
title: SWING: Unlocking Implicit Graph Representations for Graph Random Features
---

# SWING: Unlocking Implicit Graph Representations for Graph Random Features
**arXiv**：[2602.12703v1](https://arxiv.org/abs/2602.12703) · [PDF](https://arxiv.org/pdf/2602.12703.pdf)  
**作者**：Alessandro Manenti, Avinava Dubey, Arijit Sehanobish, Cesare Alippi, Krzysztof Choromanski  

**一句话要点**：提出SWING算法，通过空间行走处理隐式图表示，以高效近似图随机特征计算。

**关键词**：隐式图表示, 图随机特征, 空间行走算法, Gumbel-softmax采样, 傅里叶分析, 重要性采样

## 3 点简述
- 核心问题：针对隐式图（如ε-邻域图），传统图随机特征计算需显式构建图，效率低且不适用于大规模场景。
- 方法要点：基于隐式图与傅里叶分析的关联，设计空间行走算法，结合Gumbel-softmax采样和线性化核，避免图显式化。
- 实验或效果：算法加速器友好，在多种隐式图上验证了准确性和效率，无需输入图具体化。

## 摘要（原文）

> We propose SWING: Space Walks for Implicit Network Graphs, a new class of algorithms for computations involving Graph Random Features on graphs given by implicit representations (i-graphs), where edge-weights are defined as bi-variate functions of feature vectors in the corresponding nodes. Those classes of graphs include several prominent examples, such as: $ε$-neighborhood graphs, used on regular basis in machine learning. Rather than conducting walks on graphs' nodes, those methods rely on walks in continuous spaces, in which those graphs are embedded. To accurately and efficiently approximate original combinatorial calculations, SWING applies customized Gumbel-softmax sampling mechanism with linearized kernels, obtained via random features coupled with importance sampling techniques. This algorithm is of its own interest. SWING relies on the deep connection between implicitly defined graphs and Fourier analysis, presented in this paper. SWING is accelerator-friendly and does not require input graph materialization. We provide detailed analysis of SWING and complement it with thorough experiments on different classes of i-graphs.

