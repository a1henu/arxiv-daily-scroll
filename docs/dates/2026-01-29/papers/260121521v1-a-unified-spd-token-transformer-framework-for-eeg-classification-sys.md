---
layout: default
title: A Unified SPD Token Transformer Framework for EEG Classification: Systematic Comparison of Geometric Embeddings
---

# A Unified SPD Token Transformer Framework for EEG Classification: Systematic Comparison of Geometric Embeddings
**arXiv**：[2601.21521v1](https://arxiv.org/abs/2601.21521) · [PDF](https://arxiv.org/pdf/2601.21521.pdf)  
**作者**：Chi-Sheng Chen, En-Jui Kuo, Guan-Ying Chen, Xinyu Zhang, Fan Zhang  

**一句话要点**：提出统一SPD令牌Transformer框架，系统比较几何嵌入对EEG分类的影响

**关键词**：EEG分类, SPD矩阵, 几何嵌入, Transformer框架, 梯度条件分析

## 3 点简述
- 核心问题：SPD矩阵嵌入几何与优化动态的理论联系未知，影响EEG分类性能
- 方法要点：分析BWSPD和Log-Euclidean嵌入的梯度条件，提出嵌入空间批归一化
- 实验或效果：在三种EEG范式上验证，Log-Euclidean Transformer达到最优性能

## 摘要（原文）

> Spatial covariance matrices of EEG signals are Symmetric Positive Definite (SPD) and lie on a Riemannian manifold, yet the theoretical connection between embedding geometry and optimization dynamics remains unexplored. We provide a formal analysis linking embedding choice to gradient conditioning and numerical stability for SPD manifolds, establishing three theoretical results: (1) BWSPD's $\sqrtκ$ gradient conditioning (vs $κ$ for Log-Euclidean) via Daleckii-Kreĭn matrices provides better gradient conditioning on high-dimensional inputs ($d \geq 22$), with this advantage reducing on low-dimensional inputs ($d \leq 8$) where eigendecomposition overhead dominates; (2) Embedding-Space Batch Normalization (BN-Embed) approximates Riemannian normalization up to $O(\varepsilon^2)$ error, yielding $+26\%$ accuracy on 56-channel ERP data but negligible effect on 8-channel SSVEP data, matching the channel-count-dependent prediction; (3) bi-Lipschitz bounds prove BWSPD tokens preserve manifold distances with distortion governed solely by the condition ratio $κ$. We validate these predictions via a unified Transformer framework comparing BWSPD, Log-Euclidean, and Euclidean embeddings within identical architecture across 1,500+ runs on three EEG paradigms (motor imagery, ERP, SSVEP; 36 subjects). Our Log-Euclidean Transformer achieves state-of-the-art performance on all datasets, substantially outperforming classical Riemannian classifiers and recent SPD baselines, while BWSPD offers competitive accuracy with similar training time.

