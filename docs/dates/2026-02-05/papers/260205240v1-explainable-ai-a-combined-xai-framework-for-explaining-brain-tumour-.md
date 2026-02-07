---
layout: default
title: Explainable AI: A Combined XAI Framework for Explaining Brain Tumour Detection Models
---

# Explainable AI: A Combined XAI Framework for Explaining Brain Tumour Detection Models
**arXiv**：[2602.05240v1](https://arxiv.org/abs/2602.05240) · [PDF](https://arxiv.org/pdf/2602.05240.pdf)  
**作者**：Patrick McGonagle, William Farrelly, Kevin Curran  

**一句话要点**：提出集成XAI框架以增强脑肿瘤检测模型的解释性

**关键词**：可解释人工智能, 脑肿瘤检测, 卷积神经网络, GRAD-CAM, SHAP, 医疗影像分析

## 3 点简述
- 核心问题：深度学习模型在脑肿瘤检测中缺乏可解释性，影响医疗信任。
- 方法要点：结合GRAD-CAM、LRP和SHAP技术，提供从区域到像素的多层解释。
- 实验或效果：在BraTS 2021数据集上，模型准确率达91.24%，集成方法优于单一XAI技术。

## 摘要（原文）

> This study explores the integration of multiple Explainable AI (XAI) techniques to enhance the interpretability of deep learning models for brain tumour detection. A custom Convolutional Neural Network (CNN) was developed and trained on the BraTS 2021 dataset, achieving 91.24% accuracy in distinguishing between tumour and non-tumour regions. This research combines Gradient-weighted Class Activation Mapping (GRAD-CAM), Layer-wise Relevance Propagation (LRP) and SHapley Additive exPlanations (SHAP) to provide comprehensive insights into the model's decision-making process. This multi-technique approach successfully identified both full and partial tumours, offering layered explanations ranging from broad regions of interest to pixel-level details. GRAD-CAM highlighted important spatial regions, LRP provided detailed pixel-level relevance and SHAP quantified feature contributions. The integrated approach effectively explained model predictions, including cases with partial tumour visibility thus showing superior explanatory power compared to individual XAI methods. This research enhances transparency and trust in AI-driven medical imaging analysis by offering a more comprehensive perspective on the model's reasoning. The study demonstrates the potential of integrated XAI techniques in improving the reliability and interpretability of AI systems in healthcare, particularly for critical tasks like brain tumour detection.

