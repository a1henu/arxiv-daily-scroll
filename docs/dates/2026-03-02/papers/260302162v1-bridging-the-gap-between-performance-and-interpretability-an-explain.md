---
layout: default
title: Bridging the gap between Performance and Interpretability: An Explainable Disentangled Multimodal Framework for Cancer Survival Prediction
---

# Bridging the gap between Performance and Interpretability: An Explainable Disentangled Multimodal Framework for Cancer Survival Prediction
**arXiv**：[2603.02162v1](https://arxiv.org/abs/2603.02162) · [PDF](https://arxiv.org/pdf/2603.02162.pdf)  
**作者**：Aniek Eijpe, Soufyan Lakbir, Melis Erdal Cesur, Sara P. Oliveira, Angelos Chatzimparmpas, Sanne Abeln, Wilson Silva  

**一句话要点**：提出可解释解耦多模态框架DIMAFx，用于癌症生存预测，以平衡性能与可解释性。

**关键词**：癌症生存预测, 多模态学习, 可解释人工智能, 解耦表示, 组织病理学图像, 转录组学

## 3 点简述
- 问题：多模态生存预测模型准确但复杂，可解释性差，限制对数据源影响的理解。
- 方法：DIMAFx从组织病理学全切片图像和转录组数据生成解耦、可解释的模态特定和模态共享表示。
- 效果：在多个癌症队列中实现最先进性能，通过SHAP揭示关键多模态交互和生物学信息。

## 摘要（原文）

> While multimodal survival prediction models are increasingly more accurate, their complexity often reduces interpretability, limiting insight into how different data sources influence predictions. To address this, we introduce DIMAFx, an explainable multimodal framework for cancer survival prediction that produces disentangled, interpretable modality-specific and modality-shared representations from histopathology whole-slide images and transcriptomics data. Across multiple cancer cohorts, DIMAFx achieves state-of-the-art performance and improved representation disentanglement. Leveraging its interpretable design and SHapley Additive exPlanations, DIMAFx systematically reveals key multimodal interactions and the biological information encoded in the disentangled representations. In breast cancer survival prediction, the most predictive features contain modality-shared information, including one capturing solid tumor morphology contextualized primarily by late estrogen response, where higher-grade morphology aligned with pathway upregulation and increased risk, consistent with known breast cancer biology. Key modality-specific features capture microenvironmental signals from interacting adipose and stromal morphologies. These results show that multimodal models can overcome the traditional trade-off between performance and explainability, supporting their application in precision medicine.

