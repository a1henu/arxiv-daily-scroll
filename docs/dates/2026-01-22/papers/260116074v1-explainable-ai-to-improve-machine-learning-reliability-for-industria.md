---
layout: default
title: Explainable AI to Improve Machine Learning Reliability for Industrial Cyber-Physical Systems
---

# Explainable AI to Improve Machine Learning Reliability for Industrial Cyber-Physical Systems
**arXiv**：[2601.16074v1](https://arxiv.org/abs/2601.16074) · [PDF](https://arxiv.org/pdf/2601.16074.pdf)  
**作者**：Annemarie Jutte, Uraz Odyurt  

**一句话要点**：应用可解释AI提升工业信息物理系统中机器学习模型的预测性能

**关键词**：可解释人工智能, 工业信息物理系统, 机器学习可靠性, 时间序列分析, SHAP值

## 3 点简述
- 工业信息物理系统依赖机器学习，但模型不透明性威胁可靠性。
- 使用SHAP值分析时间序列分解组件对预测的影响，揭示训练中上下文信息不足。
- 基于可解释AI发现增加数据窗口大小，从而改善模型性能。

## 摘要（原文）

> Industrial Cyber-Physical Systems (CPS) are sensitive infrastructure from both safety and economics perspectives, making their reliability critically important. Machine Learning (ML), specifically deep learning, is increasingly integrated in industrial CPS, but the inherent complexity of ML models results in non-transparent operation. Rigorous evaluation is needed to prevent models from exhibiting unexpected behaviour on future, unseen data. Explainable AI (XAI) can be used to uncover model reasoning, allowing a more extensive analysis of behaviour. We apply XAI to to improve predictive performance of ML models intended for industrial CPS. We analyse the effects of components from time-series data decomposition on model predictions using SHAP values. Through this method, we observe evidence on the lack of sufficient contextual information during model training. By increasing the window size of data instances, informed by the XAI findings, we are able to improve model performance.

