---
layout: default
title: Optimal Transport-Induced Samples against Out-of-Distribution Overconfidence
---

# Optimal Transport-Induced Samples against Out-of-Distribution Overconfidence
**arXiv**：[2601.21320v1](https://arxiv.org/abs/2601.21320) · [PDF](https://arxiv.org/pdf/2601.21320.pdf)  
**作者**：Keke Tang, Ziyong Du, Xiaofei Wang, Weilong Peng, Peican Zhu, Zhihong Tian  

**一句话要点**：提出基于最优传输奇异边界的OTIS样本，以缓解深度神经网络在分布外输入上的过度自信问题。

**关键词**：分布外检测, 最优传输, 置信校准, 深度神经网络, 语义模糊性

## 3 点简述
- 核心问题：深度神经网络在分布外输入上常产生过度自信预测，影响开放世界可靠性。
- 方法要点：利用最优传输奇异边界构造几何基础的OTIS样本，通过置信抑制损失训练模型。
- 实验或效果：实验显示方法显著缓解过度自信，优于现有先进方法。

## 摘要（原文）

> Deep neural networks (DNNs) often produce overconfident predictions on out-of-distribution (OOD) inputs, undermining their reliability in open-world environments. Singularities in semi-discrete optimal transport (OT) mark regions of semantic ambiguity, where classifiers are particularly prone to unwarranted high-confidence predictions. Motivated by this observation, we propose a principled framework to mitigate OOD overconfidence by leveraging the geometry of OT-induced singular boundaries. Specifically, we formulate an OT problem between a continuous base distribution and the latent embeddings of training data, and identify the resulting singular boundaries. By sampling near these boundaries, we construct a class of OOD inputs, termed optimal transport-induced OOD samples (OTIS), which are geometrically grounded and inherently semantically ambiguous. During training, a confidence suppression loss is applied to OTIS to guide the model toward more calibrated predictions in structurally uncertain regions. Extensive experiments show that our method significantly alleviates OOD overconfidence and outperforms state-of-the-art methods.

