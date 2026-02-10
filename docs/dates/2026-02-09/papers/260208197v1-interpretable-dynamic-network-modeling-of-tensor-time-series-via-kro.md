---
layout: default
title: Interpretable Dynamic Network Modeling of Tensor Time Series via Kronecker Time-Varying Graphical Lasso
---

# Interpretable Dynamic Network Modeling of Tensor Time Series via Kronecker Time-Varying Graphical Lasso
**arXiv**：[2602.08197v1](https://arxiv.org/abs/2602.08197) · [PDF](https://arxiv.org/pdf/2602.08197.pdf)  
**作者**：Shingo Higashiguchi, Koki Kawabata, Yasuko Matsubara, Yasushi Sakurai  

**一句话要点**：提出Kronecker时变图套索以建模张量时间序列，解决动态网络估计中的复杂性与计算效率问题。

**关键词**：张量时间序列, 动态网络建模, Kronecker积, 图套索, 可解释性, 流算法

## 3 点简述
- 核心问题：张量时间序列的动态网络估计存在结构复杂、计算量大和可解释性差的问题。
- 方法要点：通过Kronecker积形式估计模式特定动态网络，避免纠缠结构并提升计算效率。
- 实验或效果：合成数据实验显示，该方法在边估计精度和计算时间上优于现有方法，并提供了真实案例验证。

## 摘要（原文）

> With the rapid development of web services, large amounts of time series data are generated and accumulated across various domains such as finance, healthcare, and online platforms. As such data often co-evolves with multiple variables interacting with each other, estimating the time-varying dependencies between variables (i.e., the dynamic network structure) has become crucial for accurate modeling. However, real-world data is often represented as tensor time series with multiple modes, resulting in large, entangled networks that are hard to interpret and computationally intensive to estimate. In this paper, we propose Kronecker Time-Varying Graphical Lasso (KTVGL), a method designed for modeling tensor time series. Our approach estimates mode-specific dynamic networks in a Kronecker product form, thereby avoiding overly complex entangled structures and producing interpretable modeling results. Moreover, the partitioned network structure prevents the exponential growth of computational time with data dimension. In addition, our method can be extended to stream algorithms, making the computational time independent of the sequence length. Experiments on synthetic data show that the proposed method achieves higher edge estimation accuracy than existing methods while requiring less computation time. To further demonstrate its practical value, we also present a case study using real-world data. Our source code and datasets are available at https://github.com/Higashiguchi-Shingo/KTVGL.

