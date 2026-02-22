---
layout: default
title: Inferring Height from Earth Embeddings: First insights using Google AlphaEarth
---

# Inferring Height from Earth Embeddings: First insights using Google AlphaEarth
**arXiv**：[2602.17250v1](https://arxiv.org/abs/2602.17250) · [PDF](https://arxiv.org/pdf/2602.17250.pdf)  
**作者**：Alireza Hamoudzadeh, Valeria Belloni, Roberta Ravanelli  

**一句话要点**：利用AlphaEarth嵌入指导深度学习模型进行区域地表高度映射

**关键词**：地球嵌入, 深度学习回归, 高度映射, U-Net++, 地理空间特征, 泛化能力

## 3 点简述
- 研究探索地球嵌入中的地理空间和多模态特征能否有效支持深度学习回归模型进行高度映射。
- 采用U-Net和U-Net++作为轻量卷积解码器，评估嵌入信息转化为高度估计的准确性。
- 实验显示U-Net++在测试集上表现更优，但泛化能力仍面临分布偏移和偏差挑战。

## 摘要（原文）

> This study investigates whether the geospatial and multimodal features encoded in \textit{Earth Embeddings} can effectively guide deep learning (DL) regression models for regional surface height mapping. In particular, we focused on AlphaEarth Embeddings at 10 m spatial resolution and evaluated their capability to support terrain height inference using a high-quality Digital Surface Model (DSM) as reference. U-Net and U-Net++ architectures were thus employed as lightweight convolutional decoders to assess how well the geospatial information distilled in the embeddings can be translated into accurate surface height estimates. Both architectures achieved strong training performance (both with $R^2 = 0.97$), confirming that the embeddings encode informative and decodable height-related signals. On the test set, performance decreased due to distribution shifts in height frequency between training and testing areas. Nevertheless, U-Net++ shows better generalization ($R^2 = 0.84$, median difference = -2.62 m) compared with the standard U-Net ($R^2 = 0.78$, median difference = -7.22 m), suggesting enhanced robustness to distribution mismatch. While the testing RMSE (approximately 16 m for U-Net++) and residual bias highlight remaining challenges in generalization, strong correlations indicate that the embeddings capture transferable topographic patterns. Overall, the results demonstrate the promising potential of AlphaEarth Embeddings to guide DL-based height mapping workflows, particularly when combined with spatially aware convolutional architectures, while emphasizing the need to address bias for improved regional transferability.

