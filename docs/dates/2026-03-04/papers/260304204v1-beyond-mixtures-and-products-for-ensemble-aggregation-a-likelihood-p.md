---
layout: default
title: Beyond Mixtures and Products for Ensemble Aggregation: A Likelihood Perspective on Generalized Means
---

# Beyond Mixtures and Products for Ensemble Aggregation: A Likelihood Perspective on Generalized Means
**arXiv**：[2603.04204v1](https://arxiv.org/abs/2603.04204) · [PDF](https://arxiv.org/pdf/2603.04204.pdf)  
**作者**：Raphaël Razafindralambo, Rémy Sun, Frédéric Precioso, Damien Garreau, Pierre-Alexandre Mattei  

**一句话要点**：提出基于对数似然的广义均值聚合方法，以优化深度集成中的密度聚合问题。

**关键词**：密度聚合, 深度集成, 广义均值, 对数似然, 图像分类, 文本分类

## 3 点简述
- 研究密度聚合问题，如深度集成中的预测组合，聚焦线性与几何池化的选择。
- 通过对数似然视角分析归一化广义均值，揭示r∈[0,1]区间能确保系统性改进。
- 理论分析结合图像和文本分类基准的深度集成实验，验证聚合规则的有效性。

## 摘要（原文）

> Density aggregation is a central problem in machine learning, for instance when combining predictions from a Deep Ensemble. The choice of aggregation remains an open question with two commonly proposed approaches being linear pooling (probability averaging) and geometric pooling (logit averaging). In this work, we address this question by studying the normalized generalized mean of order $r \in \mathbb{R} \cup \{-\infty,+\infty\}$ through the lens of log-likelihood, the standard evaluation criterion in machine learning. This provides a unifying aggregation formalism and shows different optimal configurations for different situations. We show that the regime $r \in [0,1]$ is the only range ensuring systematic improvements relative to individual distributions, thereby providing a principled justification for the reliability and widespread practical use of linear ($r=1$) and geometric ($r=0$) pooling. In contrast, we show that aggregation rules with $r \notin [0,1]$ may fail to provide consistent gains with explicit counterexamples. Finally, we corroborate our theoretical findings with empirical evaluations using Deep Ensembles on image and text classification benchmarks.

