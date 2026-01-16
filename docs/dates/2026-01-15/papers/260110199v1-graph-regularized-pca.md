---
layout: default
title: Graph Regularized PCA
---

# Graph Regularized PCA
**arXiv**：[2601.10199v1](https://arxiv.org/abs/2601.10199) · [PDF](https://arxiv.org/pdf/2601.10199.pdf)  
**作者**：Antonio Briola, Marwin Schmidt, Fabio Caccioli, Carlos Ros Perez, James Singleton, Christian Michler, Tomaso Aste  

**一句话要点**：提出图正则化PCA以处理高维数据中非各向同性噪声的降维问题。

**关键词**：图正则化, 主成分分析, 降维, 稀疏精度图, 图拉普拉斯, 结构感知

## 3 点简述
- 核心问题：PCA在噪声非独立同分布时性能下降，需考虑特征间依赖结构。
- 方法要点：通过稀疏精度图学习，将载荷偏向图拉普拉斯低频傅里叶模式，抑制高频信号。
- 实验或效果：在合成数据上验证，提升结构保真度，保持预测性能竞争力。

## 摘要（原文）

> High-dimensional data often exhibit dependencies among variables that violate the isotropic-noise assumption under which principal component analysis (PCA) is optimal. For cases where the noise is not independent and identically distributed across features (i.e., the covariance is not spherical) we introduce Graph Regularized PCA (GR-PCA). It is a graph-based regularization of PCA that incorporates the dependency structure of the data features by learning a sparse precision graph and biasing loadings toward the low-frequency Fourier modes of the corresponding graph Laplacian. Consequently, high-frequency signals are suppressed, while graph-coherent low-frequency ones are preserved, yielding interpretable principal components aligned with conditional relationships. We evaluate GR-PCA on synthetic data spanning diverse graph topologies, signal-to-noise ratios, and sparsity levels. Compared to mainstream alternatives, it concentrates variance on the intended support, produces loadings with lower graph-Laplacian energy, and remains competitive in out-of-sample reconstruction. When high-frequency signals are present, the graph Laplacian penalty prevents overfitting, reducing the reconstruction accuracy but improving structural fidelity. The advantage over PCA is most pronounced when high-frequency signals are graph-correlated, whereas PCA remains competitive when such signals are nearly rotationally invariant. The procedure is simple to implement, modular with respect to the precision estimator, and scalable, providing a practical route to structure-aware dimensionality reduction that improves structural fidelity without sacrificing predictive performance.

