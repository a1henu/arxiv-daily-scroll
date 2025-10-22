---
layout: default
title: Bayesian Fully-Connected Tensor Network for Hyperspectral-Multispectral Image Fusion
---

# Bayesian Fully-Connected Tensor Network for Hyperspectral-Multispectral Image Fusion
**arXiv**：[2510.18400v1](https://arxiv.org/abs/2510.18400) · [PDF](https://arxiv.org/pdf/2510.18400.pdf)  
**作者**：Linsong Shan, Zecan Yang, Laurence T. Yang, Changlong Li, Honglu Zhao, Xin Nie  

**一句话要点**：提出贝叶斯全连接张量网络以解决高光谱-多光谱图像融合中的结构破坏和参数调优问题

**关键词**：高光谱-多光谱图像融合, 贝叶斯张量网络, 变分贝叶斯推理, 层次稀疏先验, 参数自动调优, 鲁棒性建模

## 3 点简述
- 现有张量分解方法破坏空间-光谱结构，且需大量手动参数调优
- 引入贝叶斯框架和层次稀疏先验，建模跨维度相关性和物理耦合
- 基于变分贝叶斯和EM算法学习，实验显示高精度、强鲁棒性和实用价值

## 摘要（原文）

> Tensor decomposition is a powerful tool for data analysis and has been
> extensively employed in the field of hyperspectral-multispectral image fusion
> (HMF). Existing tensor decomposition-based fusion methods typically rely on
> disruptive data vectorization/reshaping or impose rigid constraints on the
> arrangement of factor tensors, hindering the preservation of spatial-spectral
> structures and the modeling of cross-dimensional correlations. Although recent
> advances utilizing the Fully-Connected Tensor Network (FCTN) decomposition have
> partially alleviated these limitations, the process of reorganizing data into
> higher-order tensors still disrupts the intrinsic spatial-spectral structure.
> Furthermore, these methods necessitate extensive manual parameter tuning and
> exhibit limited robustness against noise and spatial degradation. To alleviate
> these issues, we propose the Bayesian FCTN (BFCTN) method. Within this
> probabilistic framework, a hierarchical sparse prior that characterizing the
> sparsity of physical elements, establishes connections between the factor
> tensors. This framework explicitly models the intrinsic physical coupling among
> spatial structures, spectral signatures, and local scene homogeneity. For model
> learning, we develop a parameter estimation method based on Variational
> Bayesian inference (VB) and the Expectation-Maximization (EM) algorithm, which
> significantly reduces the need for manual parameter tuning. Extensive
> experiments demonstrate that BFCTN not only achieves state-of-the-art fusion
> accuracy and strong robustness but also exhibits practical applicability in
> complex real-world scenarios.

