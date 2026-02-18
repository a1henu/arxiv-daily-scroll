---
layout: default
title: Symbolic recovery of PDEs from measurement data
---

# Symbolic recovery of PDEs from measurement data
**arXiv**：[2602.15603v1](https://arxiv.org/abs/2602.15603) · [PDF](https://arxiv.org/pdf/2602.15603.pdf)  
**作者**：Erion Morina, Philipp Scholl, Martin Holler  

**一句话要点**：提出基于有理函数神经网络的符号恢复方法，从测量数据中重建偏微分方程模型。

**关键词**：偏微分方程重建, 符号恢复, 有理函数神经网络, 可识别性分析, 正则化方法, 物理定律建模

## 3 点简述
- 核心问题：从噪声间接测量中识别偏微分方程模型，传统方法难以获得可解释的符号表达式。
- 方法要点：利用有理函数神经网络架构，结合可识别性理论，在无噪声完整测量下唯一重建最简单物理定律。
- 实验或效果：通过ParFam架构实证验证，正则化促进稀疏性和可解释性，支持理论结果。

## 摘要（原文）

> Models based on partial differential equations (PDEs) are powerful for describing a wide range of complex relationships in the natural sciences. Accurately identifying the PDE model, which represents the underlying physical law, is essential for a proper understanding of the problem. This reconstruction typically relies on indirect and noisy measurements of the system's state and, without specifically tailored methods, rarely yields symbolic expressions, thereby hindering interpretability. In this work, we address this issue by considering existing neural network architectures based on rational functions for the symbolic representation of physical laws. These networks leverage the approximation power of rational functions while also benefiting from their flexibility in representing arithmetic operations. Our main contribution is an identifiability result, showing that, in the limit of noiseless, complete measurements, such symbolic networks can uniquely reconstruct the simplest physical law within the PDE model. Specifically, reconstructed laws remain expressible within the symbolic network architecture, with regularization-minimizing parameterizations promoting interpretability and sparsity in case of $L^1$-regularization. In addition, we provide regularity results for symbolic networks. Empirical validation using the ParFam architecture supports these theoretical findings, providing evidence for the practical reconstructibility of physical laws.

