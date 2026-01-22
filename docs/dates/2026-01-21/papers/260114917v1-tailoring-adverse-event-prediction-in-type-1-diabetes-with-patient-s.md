---
layout: default
title: Tailoring Adverse Event Prediction in Type 1 Diabetes with Patient-Specific Deep Learning Models
---

# Tailoring Adverse Event Prediction in Type 1 Diabetes with Patient-Specific Deep Learning Models
**arXiv**：[2601.14917v1](https://arxiv.org/abs/2601.14917) · [PDF](https://arxiv.org/pdf/2601.14917.pdf)  
**作者**：Giorgia Rigamonti, Mirko Paolo Barbato, Davide Marelli, Paolo Napoletano  

**一句话要点**：提出基于患者特定数据的深度学习模型，以提升1型糖尿病不良事件预测的准确性和个性化干预效果。

**关键词**：血糖预测, 个性化模型, 深度学习, 1型糖尿病, 不良事件预测, 可穿戴健康

## 3 点简述
- 核心问题：传统血糖预测模型忽略个体差异，难以在真实场景中有效预防高血糖和低血糖等不良事件。
- 方法要点：采用患者特定深度学习模型，结合多模态数据，通过留一受试者交叉验证和微调策略优化个性化预测。
- 实验或效果：个性化模型显著改善不良事件预测，并通过消融研究确定最小训练数据需求，支持可穿戴和移动健康平台应用。

## 摘要（原文）

> Effective management of Type 1 Diabetes requires continuous glucose monitoring and precise insulin adjustments to prevent hyperglycemia and hypoglycemia. With the growing adoption of wearable glucose monitors and mobile health applications, accurate blood glucose prediction is essential for enhancing automated insulin delivery and decision-support systems. This paper presents a deep learning-based approach for personalized blood glucose prediction, leveraging patient-specific data to improve prediction accuracy and responsiveness in real-world scenarios. Unlike traditional generalized models, our method accounts for individual variability, enabling more effective subject-specific predictions. We compare Leave-One-Subject-Out Cross-Validation with a fine-tuning strategy to evaluate their ability to model patient-specific dynamics. Results show that personalized models significantly improve the prediction of adverse events, enabling more precise and timely interventions in real-world scenarios. To assess the impact of patient-specific data, we conduct experiments comparing a multimodal, patient-specific approach against traditional CGM-only methods. Additionally, we perform an ablation study to investigate model performance with progressively smaller training sets, identifying the minimum data required for effective personalization-an essential consideration for real-world applications where extensive data collection is often challenging. Our findings underscore the potential of adaptive, personalized glucose prediction models for advancing next-generation diabetes management, particularly in wearable and mobile health platforms, enhancing consumer-oriented diabetes care solutions.

