---
layout: default
title: ExplainerPFN: Towards tabular foundation models for model-free zero-shot feature importance estimations
---

# ExplainerPFN: Towards tabular foundation models for model-free zero-shot feature importance estimations
**arXiv**：[2601.23068v1](https://arxiv.org/abs/2601.23068) · [PDF](https://arxiv.org/pdf/2601.23068.pdf)  
**作者**：Joao Fonseca, Julia Stoyanovich  

**一句话要点**：提出ExplainerPFN，一种无需模型访问的零样本表格基础模型，用于估计特征重要性。

**关键词**：表格基础模型, 零样本学习, 特征重要性估计, Shapley值, 模型解释性, 合成数据训练

## 3 点简述
- 核心问题：Shapley值计算需模型访问且昂贵，实际部署中常不可行。
- 方法要点：基于TabPFN预训练，使用合成数据和Shapley值监督，实现零样本特征重要性预测。
- 实验或效果：在真实和合成数据集上，性能媲美依赖少量SHAP示例的少样本解释器。

## 摘要（原文）

> Computing the importance of features in supervised classification tasks is critical for model interpretability. Shapley values are a widely used approach for explaining model predictions, but require direct access to the underlying model, an assumption frequently violated in real-world deployments. Further, even when model access is possible, their exact computation may be prohibitively expensive. We investigate whether meaningful Shapley value estimations can be obtained in a zero-shot setting, using only the input data distribution and no evaluations of the target model. To this end, we introduce ExplainerPFN, a tabular foundation model built on TabPFN that is pretrained on synthetic datasets generated from random structural causal models and supervised using exact or near-exact Shapley values. Once trained, ExplainerPFN predicts feature attributions for unseen tabular datasets without model access, gradients, or example explanations.
>   Our contributions are fourfold: (1) we show that few-shot learning-based explanations can achieve high fidelity to SHAP values with as few as two reference observations; (2) we propose ExplainerPFN, the first zero-shot method for estimating Shapley values without access to the underlying model or reference explanations; (3) we provide an open-source implementation of ExplainerPFN, including the full training pipeline and synthetic data generator; and (4) through extensive experiments on real and synthetic datasets, we show that ExplainerPFN achieves performance competitive with few-shot surrogate explainers that rely on 2-10 SHAP examples.

