---
layout: default
title: From Data Statistics to Feature Geometry: How Correlations Shape Superposition
---

# From Data Statistics to Feature Geometry: How Correlations Shape Superposition
**arXiv**：[2603.09972v1](https://arxiv.org/abs/2603.09972) · [PDF](https://arxiv.org/pdf/2603.09972.pdf)  
**作者**：Lucas Prieto, Edward Stevinson, Melih Barsbey, Tolga Birdal, Pedro A. M. Mediano  

**一句话要点**：提出Bag-of-Words Superposition以揭示相关特征在叠加中的建设性干扰作用

**关键词**：特征叠加, 相关特征, 建设性干扰, Bag-of-Words Superposition, 几何结构, 语言模型

## 3 点简述
- 核心问题：传统叠加理论假设特征稀疏且不相关，不适用于现实数据中的相关特征。
- 方法要点：引入BOWS设置，编码互联网文本的二进制词袋表示，研究相关特征的叠加几何。
- 实验或效果：发现相关特征可产生建设性干扰，形成语义簇和循环结构，解释真实语言模型现象。

## 摘要（原文）

> A central idea in mechanistic interpretability is that neural networks represent more features than they have dimensions, arranging them in superposition to form an over-complete basis. This framing has been influential, motivating dictionary learning approaches such as sparse autoencoders. However, superposition has mostly been studied in idealized settings where features are sparse and uncorrelated. In these settings, superposition is typically understood as introducing interference that must be minimized geometrically and filtered out by non-linearities such as ReLUs, yielding local structures like regular polytopes. We show that this account is incomplete for realistic data by introducing Bag-of-Words Superposition (BOWS), a controlled setting to encode binary bag-of-words representations of internet text in superposition. Using BOWS, we find that when features are correlated, interference can be constructive rather than just noise to be filtered out. This is achieved by arranging features according to their co-activation patterns, making interference between active features constructive, while still using ReLUs to avoid false positives. We show that this kind of arrangement is more prevalent in models trained with weight decay and naturally gives rise to semantic clusters and cyclical structures which have been observed in real language models yet were not explained by the standard picture of superposition. Code for this paper can be found at https://github.com/LucasPrietoAl/correlations-feature-geometry.

