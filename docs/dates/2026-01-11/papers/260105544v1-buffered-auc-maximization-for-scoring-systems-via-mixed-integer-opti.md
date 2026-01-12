---
layout: default
title: Buffered AUC maximization for scoring systems via mixed-integer optimization
---

# Buffered AUC maximization for scoring systems via mixed-integer optimization
**arXiv**：[2601.05544v1](https://arxiv.org/abs/2601.05544) · [PDF](https://arxiv.org/pdf/2601.05544.pdf)  
**作者**：Moe Shiina, Shunnosuke Ikeda, Yuichi Takano  

**一句话要点**：提出基于混合整数优化的缓冲AUC最大化方法以构建高可解释性评分系统

**关键词**：评分系统, 混合整数优化, AUC最大化, 可解释分类, 缓冲AUC, 组稀疏约束

## 3 点简述
- 针对评分系统未直接优化AUC的问题，提出最大化缓冲AUC作为紧致凹下界
- 采用混合整数线性优化框架，结合组稀疏约束限制变量数量，提升模型可解释性
- 在真实数据集上验证，相比正则化和逐步回归基线，获得更优AUC性能

## 摘要（原文）

> A scoring system is a linear classifier composed of a small number of explanatory variables, each assigned a small integer coefficient. This system is highly interpretable and allows predictions to be made with simple manual calculations without the need for a calculator. Several previous studies have used mixed-integer optimization (MIO) techniques to develop scoring systems for binary classification; however, they have not focused on directly maximizing AUC (i.e., area under the receiver operating characteristic curve), even though AUC is recognized as an essential evaluation metric for scoring systems. Our goal herein is to establish an effective MIO framework for constructing scoring systems that directly maximize the buffered AUC (bAUC) as the tightest concave lower bound on AUC. Our optimization model is formulated as a mixed-integer linear optimization (MILO) problem that maximizes bAUC subject to a group sparsity constraint for limiting the number of questions in the scoring system. Computational experiments using publicly available real-world datasets demonstrate that our MILO method can build scoring systems with superior AUC values compared to the baseline methods based on regularization and stepwise regression. This research contributes to the advancement of MIO techniques for developing highly interpretable classification models.

