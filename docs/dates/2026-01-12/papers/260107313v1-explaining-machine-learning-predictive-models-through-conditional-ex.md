---
layout: default
title: Explaining Machine Learning Predictive Models through Conditional Expectation Methods
---

# Explaining Machine Learning Predictive Models through Conditional Expectation Methods
**arXiv**：[2601.07313v1](https://arxiv.org/abs/2601.07313) · [PDF](https://arxiv.org/pdf/2601.07313.pdf)  
**作者**：Silvia Ruiz-España, Laura Arnal, François Signol, Juan-Carlos Perez-Cortes, Joaquim Arlandis  

**一句话要点**：提出MUCE方法以增强复杂机器学习模型的局部可解释性

**关键词**：可解释人工智能, 局部可解释性, 条件期望方法, 特征交互, 模型可靠性评估

## 3 点简述
- 核心问题：复杂AI模型缺乏透明度，影响用户理解和信任，尤其在风险应用中。
- 方法要点：MUCE扩展ICE，通过多变量条件期望探索特征交互，提供图形和量化解释。
- 实验或效果：在合成和真实数据集上验证，MUCE有效捕捉局部行为，稳定性与不确定性指数提供预测置信度洞察。

## 摘要（原文）

> The rapid adoption of complex Artificial Intelligence (AI) and Machine Learning (ML) models has led to their characterization as black boxes due to the difficulty of explaining their internal decision-making processes. This lack of transparency hinders users' ability to understand, validate and trust model behavior, particularly in high-risk applications. Although explainable AI (XAI) has made significant progress, there remains a need for versatile and effective techniques to address increasingly complex models. This work introduces Multivariate Conditional Expectation (MUCE), a model-agnostic method for local explainability designed to capture prediction changes from feature interactions. MUCE extends Individual Conditional Expectation (ICE) by exploring a multivariate grid of values in the neighborhood of a given observation at inference time, providing graphical explanations that illustrate the local evolution of model predictions. In addition, two quantitative indices, stability and uncertainty, summarize local behavior and assess model reliability. Uncertainty is further decomposed into uncertainty+ and uncertainty- to capture asymmetric effects that global measures may overlook. The proposed method is validated using XGBoost models trained on three datasets: two synthetic (2D and 3D) to evaluate behavior near decision boundaries, and one transformed real-world dataset to test adaptability to heterogeneous feature types. Results show that MUCE effectively captures complex local model behavior, while the stability and uncertainty indices provide meaningful insight into prediction confidence. MUCE, together with the ICE modification and the proposed indices, offers a practical contribution to local explainability, enabling both graphical and quantitative insights that enhance the interpretability of predictive models and support more trustworthy and transparent decision-making.

