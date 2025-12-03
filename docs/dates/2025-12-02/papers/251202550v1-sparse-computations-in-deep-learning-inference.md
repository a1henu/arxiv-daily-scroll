---
layout: default
title: Sparse Computations in Deep Learning Inference
---

# Sparse Computations in Deep Learning Inference
**arXiv**：[2512.02550v1](https://arxiv.org/abs/2512.02550) · [PDF](https://arxiv.org/pdf/2512.02550.pdf)  
**作者**：Ioanna Tasou, Panagiotis Mpakos, Angelos Vlachos, Dionysios Adamopoulos, Georgios Giannakopoulos, Konstantinos Katsikopoulos, Ioannis Karaparisis, Maria Lazou, Spyridon Loukovitis, Areti Mei, Anastasia Poulopoulou, Angeliki Dimitriou, Giorgos Filandrianos, Dimitrios Galanopoulos, Vasileios Karampinis, Ilias Mitsouras, Nikolaos Spanos, Petros Anastasiadis, Ioannis Doudalis, Konstantinos Nikas, George Retsinas, Paraskevi Tzouveli, Christina Giannoula, Nectarios Koziris, Nikela Papadopoulou, Giorgos Stamou, Athanasios Voulodimos, Georgios Goumas  

**一句话要点**：综述稀疏计算在深度学习推理中的优化方法，为性能工程师提供资源指南

**关键词**：深度学习推理, 稀疏计算, 性能优化, SpMM核, SDDMM核, CPU/GPU实现

## 3 点简述
- 核心问题：深度学习推理的计算需求巨大，稀疏性作为关键机制未被充分利用
- 方法要点：讨论稀疏形式、稀疏核实现、软件工具，并评估SpMM和SDDMM核性能
- 实验或效果：提供CPU和GPU平台上的稀疏核实现评估结果，支持高效模型部署

## 摘要（原文）

> The computational demands of modern Deep Neural Networks (DNNs) are immense and constantly growing. While training costs usually capture public attention, inference demands are also contributing in significant computational, energy and environmental footprints. Sparsity stands out as a critical mechanism for drastically reducing these resource demands. However, its potential remains largely untapped and is not yet fully incorporated in production AI systems. To bridge this gap, this work provides the necessary knowledge and insights for performance engineers keen to get involved in deep learning inference optimization. In particular, in this work we: a) discuss the various forms of sparsity that can be utilized in DNN inference, b) explain how the original dense computations translate to sparse kernels, c) provide an extensive bibliographic review of the state-of-the-art in the implementation of these kernels for CPUs and GPUs, d) discuss the availability of sparse datasets in support of sparsity-related research and development, e) explore the current software tools and frameworks that provide robust sparsity support, and f) present evaluation results of different implementations of the key SpMM and SDDMM kernels on CPU and GPU platforms. Ultimately, this paper aims to serve as a resource for performance engineers seeking to develop and deploy highly efficient sparse deep learning models in productions.

