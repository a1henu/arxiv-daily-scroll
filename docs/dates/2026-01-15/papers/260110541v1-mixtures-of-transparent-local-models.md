---
layout: default
title: Mixtures of Transparent Local Models
---

# Mixtures of Transparent Local Models
**arXiv**：[2601.10541v1](https://arxiv.org/abs/2601.10541) · [PDF](https://arxiv.org/pdf/2601.10541.pdf)  
**作者**：Niffa Cheick Oumar Diaby, Thierry Duchesne, Mario Marchand  

**一句话要点**：提出透明局部模型混合方法，以解决输入空间中局部区域模型突变时的可解释建模问题。

**关键词**：PAC-Bayes, 风险界, 局部模型, 透明模型, 模型混合

## 3 点简述
- 核心问题：机器学习模型在输入空间不同区域需透明建模，但模型可能随区域变化而突变。
- 方法要点：通过多预测器损失函数，同时学习透明标注函数及其低风险输入空间局部区域。
- 实验或效果：在合成和真实数据集上验证，与现有方法及不透明模型相比具有竞争力。

## 摘要（原文）

> The predominance of machine learning models in many spheres of human activity has led to a growing demand for their transparency. The transparency of models makes it possible to discern some factors, such as security or non-discrimination. In this paper, we propose a mixture of transparent local models as an alternative solution for designing interpretable (or transparent) models. Our approach is designed for the situations where a simple and transparent function is suitable for modeling the label of instances in some localities/regions of the input space, but may change abruptly as we move from one locality to another. Consequently, the proposed algorithm is to learn both the transparent labeling function and the locality of the input space where the labeling function achieves a small risk in its assigned locality. By using a new multi-predictor (and multi-locality) loss function, we established rigorous PAC-Bayesian risk bounds for the case of binary linear classification problem and that of linear regression. In both cases, synthetic data sets were used to illustrate how the learning algorithms work. The results obtained from real data sets highlight the competitiveness of our approach compared to other existing methods as well as certain opaque models. Keywords: PAC-Bayes, risk bounds, local models, transparent models, mixtures of local transparent models.

