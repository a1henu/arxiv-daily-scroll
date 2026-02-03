---
layout: default
title: NAB: Neural Adaptive Binning for Sparse-View CT reconstruction
---

# NAB: Neural Adaptive Binning for Sparse-View CT reconstruction
**arXiv**：[2602.02356v1](https://arxiv.org/abs/2602.02356) · [PDF](https://arxiv.org/pdf/2602.02356.pdf)  
**作者**：Wangduo Xie, Matthew B. Blaschko  

**一句话要点**：提出神经自适应分箱方法，以整合矩形先验提升稀疏视图CT重建质量

**关键词**：稀疏视图CT重建, 形状先验整合, 神经自适应分箱, 工业对象检测, 端到端优化, 坐标映射

## 3 点简述
- 核心问题：稀疏视图CT重建中经典隐式神经网络无法利用物体形状先验，影响工业对象内部结构检测。
- 方法要点：通过基于移位双曲正切函数差分的创新分箱机制，将坐标空间映射到分箱向量空间，并扩展支持旋转，实现端到端优化编码参数。
- 实验或效果：在工业数据集上表现优异，通过调整分箱函数平滑度可泛化至更复杂几何对象，在医学数据集上扩展后保持稳健。

## 摘要（原文）

> Computed Tomography (CT) plays a vital role in inspecting the internal structures of industrial objects. Furthermore, achieving high-quality CT reconstruction from sparse views is essential for reducing production costs. While classic implicit neural networks have shown promising results for sparse reconstruction, they are unable to leverage shape priors of objects. Motivated by the observation that numerous industrial objects exhibit rectangular structures, we propose a novel \textbf{N}eural \textbf{A}daptive \textbf{B}inning (\textbf{NAB}) method that effectively integrates rectangular priors into the reconstruction process. Specifically, our approach first maps coordinate space into a binned vector space. This mapping relies on an innovative binning mechanism based on differences between shifted hyperbolic tangent functions, with our extension enabling rotations around the input-plane normal vector. The resulting representations are then processed by a neural network to predict CT attenuation coefficients. This design enables end-to-end optimization of the encoding parameters -- including position, size, steepness, and rotation -- via gradient flow from the projection data, thus enhancing reconstruction accuracy. By adjusting the smoothness of the binning function, NAB can generalize to objects with more complex geometries. This research provides a new perspective on integrating shape priors into neural network-based reconstruction. Extensive experiments demonstrate that NAB achieves superior performance on two industrial datasets. It also maintains robust on medical datasets when the binning function is extended to more general expression. The code will be made available.

