---
layout: default
title: Small molecule retrieval from tandem mass spectrometry: what are we optimizing for?
---

# Small molecule retrieval from tandem mass spectrometry: what are we optimizing for?
**arXiv**：[2602.16507v1](https://arxiv.org/abs/2602.16507) · [PDF](https://arxiv.org/pdf/2602.16507.pdf)  
**作者**：Gaetan De Waele, Marek Wydmuch, Krzysztof Dembczyński, Wojciech Kotłowski, Willem Waegeman  

**一句话要点**：分析损失函数对质谱小分子检索的影响，揭示指纹相似性与检索性能的权衡

**关键词**：质谱分析, 小分子检索, 损失函数, 深度学习, 指纹预测, 贝叶斯优化

## 3 点简述
- 研究质谱数据中小分子鉴定问题，聚焦深度学习模型训练中的损失函数选择
- 推导遗憾界理论分析，揭示贝叶斯最优决策在不同目标下的分歧
- 实验显示优化指纹预测精度会损害检索结果，反之亦然，提供损失函数设计指导

## 摘要（原文）

> One of the central challenges in the computational analysis of liquid chromatography-tandem mass spectrometry (LC-MS/MS) data is to identify the compounds underlying the output spectra. In recent years, this problem is increasingly tackled using deep learning methods. A common strategy involves predicting a molecular fingerprint vector from an input mass spectrum, which is then used to search for matches in a chemical compound database. While various loss functions are employed in training these predictive models, their impact on model performance remains poorly understood. In this study, we investigate commonly used loss functions, deriving novel regret bounds that characterize when Bayes-optimal decisions for these objectives must diverge. Our results reveal a fundamental trade-off between the two objectives of (1) fingerprint similarity and (2) molecular retrieval. Optimizing for more accurate fingerprint predictions typically worsens retrieval results, and vice versa. Our theoretical analysis shows this trade-off depends on the similarity structure of candidate sets, providing guidance for loss function and fingerprint selection.

