---
layout: default
title: MM-algorithms for traditional and convex NMF with Tweedie and Negative Binomial cost functions and empirical evaluation
---

# MM-algorithms for traditional and convex NMF with Tweedie and Negative Binomial cost functions and empirical evaluation
**arXiv**：[2603.09601v1](https://arxiv.org/abs/2603.09601) · [PDF](https://arxiv.org/pdf/2603.09601.pdf)  
**作者**：Elisabeth Sommer James, Asger Hobolth, Marta Pelizzola  

**一句话要点**：提出基于Majorize-Minimisation的NMF统一框架，支持Tweedie和负二项分布，提升过分散数据建模能力。

**关键词**：非负矩阵分解, Majorize-Minimisation算法, Tweedie分布, 负二项分布, 凸NMF, 过分散数据

## 3 点简述
- 核心问题：传统NMF基于高斯或泊松噪声假设，不适用于过分散或复杂均值-方差关系的数据。
- 方法要点：使用Majorize-Minimisation推导乘性更新规则，涵盖传统和凸NMF，首次实现多个凸NMF模型。
- 实验或效果：在突变和词频数据上验证噪声模型选择对拟合和特征恢复的关键影响，凸NMF在大类场景中更高效稳健。

## 摘要（原文）

> Non-negative matrix factorisation (NMF) is a widely used tool for unsupervised learning and feature extraction, with applications ranging from genomics to text analysis and signal processing. Standard formulations of NMF are typically derived under Gaussian or Poisson noise assumptions, which may be inadequate for data exhibiting overdispersion or other complex mean-variance relationships. In this paper, we develop a unified framework for both traditional and convex NMF under a broad class of distributional assumptions, including Negative Binomial and Tweedie models, where the connection between the Tweedie and the $β$-divergence is also highlighted. Using a Majorize-Minimisation approach, we derive multiplicative update rules for all considered models, and novel updates for convex NMF with Poisson and Negative Binomial cost functions. We provide a unified implementation of all considered models, including the first implementations of several convex NMF models. Empirical evaluations on mutational and word count data demonstrate that the choice of noise model critically affects model fit and feature recovery, and that convex NMF can provide an efficient and robust alternative to traditional NMF in scenarios where the number of classes is large. The code for our proposed updates is available in the R package nmfgenr and can be found at https://github.com/MartaPelizzola/nmfgenr.

