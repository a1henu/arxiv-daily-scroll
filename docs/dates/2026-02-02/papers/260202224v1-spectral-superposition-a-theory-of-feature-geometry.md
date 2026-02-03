---
layout: default
title: Spectral Superposition: A Theory of Feature Geometry
---

# Spectral Superposition: A Theory of Feature Geometry
**arXiv**：[2602.02224v1](https://arxiv.org/abs/2602.02224) · [PDF](https://arxiv.org/pdf/2602.02224.pdf)  
**作者**：Georgi Ivanov, Narmeen Oozeer, Shivam Raval, Tasana Pejovic, Shriyash Upadhyay, Amir Abdullah  

**一句话要点**：提出谱叠加理论，通过分析权重矩阵谱结构来研究神经网络特征几何

**关键词**：特征几何, 谱分析, 神经网络解释性, 叠加理论, 框架算子

## 3 点简述
- 核心问题：神经网络特征叠加导致几何结构被忽略，现有方法仅分解为稀疏线性特征
- 方法要点：引入框架算子分析特征在特征空间中的谱分布，捕获全局几何交互
- 实验或效果：在玩具模型中证明容量饱和迫使谱局部化，特征组织为紧框架并分类几何结构

## 摘要（原文）

> Neural networks represent more features than they have dimensions via superposition, forcing features to share representational space. Current methods decompose activations into sparse linear features but discard geometric structure. We develop a theory for studying the geometric structre of features by analyzing the spectra (eigenvalues, eigenspaces, etc.) of weight derived matrices. In particular, we introduce the frame operator $F = WW^\top$, which gives us a spectral measure that describes how each feature allocates norm across eigenspaces. While previous tools could describe the pairwise interactions between features, spectral methods capture the global geometry (``how do all features interact?''). In toy models of superposition, we use this theory to prove that capacity saturation forces spectral localization: features collapse onto single eigenspaces, organize into tight frames, and admit discrete classification via association schemes, classifying all geometries from prior work (simplices, polygons, antiprisms). The spectral measure formalism applies to arbitrary weight matrices, enabling diagnosis of feature localization beyond toy settings. These results point toward a broader program: applying operator theory to interpretability.

