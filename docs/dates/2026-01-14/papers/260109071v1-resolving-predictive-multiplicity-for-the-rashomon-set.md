---
layout: default
title: Resolving Predictive Multiplicity for the Rashomon Set
---

# Resolving Predictive Multiplicity for the Rashomon Set
**arXiv**：[2601.09071v1](https://arxiv.org/abs/2601.09071) · [PDF](https://arxiv.org/pdf/2601.09071.pdf)  
**作者**：Parian Haghighat, Hadis Anahideh, Cynthia Rudin  

**一句话要点**：提出三种方法以减少Rashomon集合中的预测不一致性，适用于高风险应用场景。

**关键词**：预测多重性, Rashomon集合, 模型一致性, 异常值校正, 局部修补, 成对调和

## 3 点简述
- 核心问题：预测多重性导致模型预测不一致，影响高风险应用的可信度。
- 方法要点：包括异常值校正、局部修补和成对调和，以降低预测方差和偏差。
- 实验或效果：在多个数据集上实验，减少不一致性指标同时保持准确率竞争力。

## 摘要（原文）

> The existence of multiple, equally accurate models for a given predictive task leads to predictive multiplicity, where a ``Rashomon set'' of models achieve similar accuracy but diverges in their individual predictions. This inconsistency undermines trust in high-stakes applications where we want consistent predictions. We propose three approaches to reduce inconsistency among predictions for the members of the Rashomon set. The first approach is \textbf{outlier correction}. An outlier has a label that none of the good models are capable of predicting correctly. Outliers can cause the Rashomon set to have high variance predictions in a local area, so fixing them can lower variance. Our second approach is local patching. In a local region around a test point, models may disagree with each other because some of them are biased. We can detect and fix such biases using a validation set, which also reduces multiplicity. Our third approach is pairwise reconciliation, where we find pairs of models that disagree on a region around the test point. We modify predictions that disagree, making them less biased. These three approaches can be used together or separately, and they each have distinct advantages. The reconciled predictions can then be distilled into a single interpretable model for real-world deployment. In experiments across multiple datasets, our methods reduce disagreement metrics while maintaining competitive accuracy.

