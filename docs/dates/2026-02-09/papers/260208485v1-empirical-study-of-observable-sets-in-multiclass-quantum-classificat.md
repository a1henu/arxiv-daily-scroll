---
layout: default
title: Empirical Study of Observable Sets in Multiclass Quantum Classification
---

# Empirical Study of Observable Sets in Multiclass Quantum Classification
**arXiv**：[2602.08485v1](https://arxiv.org/abs/2602.08485) · [PDF](https://arxiv.org/pdf/2602.08485.pdf)  
**作者**：Paul San Sebastian, Mikel Cañizo, Roman Orus  

**一句话要点**：研究多类量子分类中可观测集选择对模型性能的影响

**关键词**：多类量子分类, 可观测集, 变分量子算法, Barren Plateaus, Neural Collapse, 量子机器学习

## 3 点简述
- 核心问题：多类量子机器学习中可观测集选择缺乏理论依据，影响模型设计
- 方法要点：比较基于期望值最大化和保真度最大化的分类准则，使用泡利字符串和计算基投影作为可观测集
- 实验或效果：分析可观测集选择在Barren Plateaus和Neural Collapse背景下对性能的影响，为未来模型设计提供指导

## 摘要（原文）

> Variational quantum algorithms have gained attention as early applications of quantum computers for learning tasks. In the context of supervised learning, most of the works that tackle classification problems with parameterized quantum circuits constrain their scope to the setting of binary classification or perform multiclass classification via ensembles of binary classifiers (strategies such as one versus rest). Those few works that propose native multiclass models, however, do not justify the choice of observables that perform the classification. This work studies two main classification criteria in multiclass quantum machine learning: maximizing the expected value of an observable representing a class or maximizing the fidelity of the encoded quantum state with a reference state representing a class. To compare both approaches, sets of Pauli strings and sets of projectors into the computational basis are chosen as observables in the quantum machine learning models. Observing the empirical behavior of each model type, the effect of different observable set choices on the performance of quantum machine learning models is analyzed in the context of Barren Plateaus and Neural Collapse. The results provide insights that may guide the design of future multiclass quantum machine learning models.

