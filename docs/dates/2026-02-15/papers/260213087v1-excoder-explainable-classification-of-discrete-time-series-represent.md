---
layout: default
title: EXCODER: EXplainable Classification Of DiscretE time series Representations
---

# EXCODER: EXplainable Classification Of DiscretE time series Representations
**arXiv**：[2602.13087v1](https://arxiv.org/abs/2602.13087) · [PDF](https://arxiv.org/pdf/2602.13087.pdf)  
**作者**：Yannik Hahn, Antonin Königsfeld, Hasan Tercan, Tobias Meisen  

**一句话要点**：提出EXCODER框架，通过离散潜在表示增强时间序列分类的可解释性，并引入SSA指标验证解释忠实度。

**关键词**：时间序列分类, 可解释人工智能, 离散潜在表示, VQ-VAE, DVAE, SSA指标

## 3 点简述
- 核心问题：深度学习时间序列分类模型缺乏可解释性，原始数据高维和噪声阻碍XAI效果。
- 方法要点：使用VQ-VAE和DVAE将时间序列转换为离散潜在表示，以减少冗余并聚焦信息模式，提升XAI解释的简洁性和结构化。
- 实验或效果：应用XAI于压缩表示，保持分类性能，提出SSA指标定量评估XAI识别特征与训练数据标签分布的对齐度。

## 摘要（原文）

> Deep learning has significantly improved time series classification, yet the lack of explainability in these models remains a major challenge. While Explainable AI (XAI) techniques aim to make model decisions more transparent, their effectiveness is often hindered by the high dimensionality and noise present in raw time series data. In this work, we investigate whether transforming time series into discrete latent representations-using methods such as Vector Quantized Variational Autoencoders (VQ-VAE) and Discrete Variational Autoencoders (DVAE)-not only preserves but enhances explainability by reducing redundancy and focusing on the most informative patterns. We show that applying XAI methods to these compressed representations leads to concise and structured explanations that maintain faithfulness without sacrificing classification performance. Additionally, we propose Similar Subsequence Accuracy (SSA), a novel metric that quantitatively assesses the alignment between XAI-identified salient subsequences and the label distribution in the training data. SSA provides a systematic way to validate whether the features highlighted by XAI methods are truly representative of the learned classification patterns. Our findings demonstrate that discrete latent representations not only retain the essential characteristics needed for classification but also offer a pathway to more compact, interpretable, and computationally efficient explanations in time series analysis.

