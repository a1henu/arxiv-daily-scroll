---
layout: default
title: Fair feature attribution for multi-output prediction: a Shapley-based perspective
---

# Fair feature attribution for multi-output prediction: a Shapley-based perspective
**arXiv**：[2602.22882v1](https://arxiv.org/abs/2602.22882) · [PDF](https://arxiv.org/pdf/2602.22882.pdf)  
**作者**：Umberto Biccari, Alain Ibáñez de Opakua, José María Mato, Óscar Millet, Roberto Morales, Enrique Zuazua  

**一句话要点**：基于Shapley框架，为多输出预测提供公平特征归因的刚性定理

**关键词**：特征归因, Shapley值, 多输出预测, 可解释性, 合作博弈, 公平性

## 3 点简述
- 核心问题：多输出预测中特征归因的公平性缺乏理论依据，SHAP解释独立计算各输出的必要性未知
- 方法要点：扩展Shapley公理到向量值合作博弈，证明满足效率等公理的归因规则必须按输出分量分解
- 实验或效果：在生物医学基准上验证多输出模型可节省计算，SHAP解释与Shapley公理强加的分解结构一致

## 摘要（原文）

> In this article, we provide an axiomatic characterization of feature attribution for multi-output predictors within the Shapley framework. While SHAP explanations are routinely computed independently for each output coordinate, the theoretical necessity of this practice has remained unclear. By extending the classical Shapley axioms to vector-valued cooperative games, we establish a rigidity theorem showing that any attribution rule satisfying efficiency, symmetry, dummy player, and additivity must necessarily decompose component-wise across outputs. Consequently, any joint-output attribution rule must relax at least one of the classical Shapley axioms. This result identifies a previously unformalized structural constraint in Shapley-based interpretability, clarifying the precise scope of fairness-consistent explanations in multi-output learning. Numerical experiments on a biomedical benchmark illustrate that multi-output models can yield computational savings in training and deployment, while producing SHAP explanations that remain fully consistent with the component-wise structure imposed by the Shapley axioms.

