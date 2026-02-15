---
layout: default
title: PAC-Bayesian Generalization Guarantees for Fairness on Stochastic and Deterministic Classifiers
---

# PAC-Bayesian Generalization Guarantees for Fairness on Stochastic and Deterministic Classifiers
**arXiv**：[2602.11722v1](https://arxiv.org/abs/2602.11722) · [PDF](https://arxiv.org/pdf/2602.11722.pdf)  
**作者**：Julien Bastian, Benjamin Leblanc, Pascal Germain, Amaury Habrard, Christine Largeron, Guillaume Metzler, Emilie Morvant, Paul Viallard  

**一句话要点**：提出PAC-Bayesian框架以推导公平性泛化保证，适用于随机和确定性分类器。

**关键词**：公平性泛化保证, PAC-Bayesian框架, 随机分类器, 确定性分类器, 风险差异, 自边界算法

## 3 点简述
- 核心问题：传统PAC泛化界无法为平衡预测风险和公平约束的模型提供理论保证。
- 方法要点：基于PAC-Bayes技术，为随机分类器推导公平界，并扩展至确定性分类器。
- 实验或效果：在三种经典公平度量上实证评估，展示框架实用性和界紧致性。

## 摘要（原文）

> Classical PAC generalization bounds on the prediction risk of a classifier are insufficient to provide theoretical guarantees on fairness when the goal is to learn models balancing predictive risk and fairness constraints. We propose a PAC-Bayesian framework for deriving generalization bounds for fairness, covering both stochastic and deterministic classifiers. For stochastic classifiers, we derive a fairness bound using standard PAC-Bayes techniques. Whereas for deterministic classifiers, as usual PAC-Bayes arguments do not apply directly, we leverage a recent advance in PAC-Bayes to extend the fairness bound beyond the stochastic setting. Our framework has two advantages: (i) It applies to a broad class of fairness measures that can be expressed as a risk discrepancy, and (ii) it leads to a self-bounding algorithm in which the learning procedure directly optimizes a trade-off between generalization bounds on the prediction risk and on the fairness. We empirically evaluate our framework with three classical fairness measures, demonstrating not only its usefulness but also the tightness of our bounds.

