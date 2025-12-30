---
layout: default
title: Scalable Residual Feature Aggregation Framework with Hybrid Metaheuristic Optimization for Robust Early Pancreatic Neoplasm Detection in Multimodal CT Imaging
---

# Scalable Residual Feature Aggregation Framework with Hybrid Metaheuristic Optimization for Robust Early Pancreatic Neoplasm Detection in Multimodal CT Imaging
**arXiv**：[2512.23597v1](https://arxiv.org/abs/2512.23597) · [PDF](https://arxiv.org/pdf/2512.23597.pdf)  
**作者**：Janani Annur Thiruvengadam, Kiran Mayee Nabigaru, Anusha Kovi  

**一句话要点**：提出可扩展残差特征聚合框架，结合混合元启发式优化，用于多模态CT成像中胰腺肿瘤的早期检测。

**关键词**：胰腺肿瘤检测, 多模态CT成像, 残差特征聚合, 混合元启发式优化, Vision Transformer, 超参数优化

## 3 点简述
- 核心问题：胰腺肿瘤早期检测困难，因CT图像中肿瘤对比度低且患者解剖结构差异大。
- 方法要点：采用SRFA框架，包括MAGRes-UNet分割、DenseNet-121特征提取、HHO-BA特征选择及ViT与EfficientNet-B3混合分类。
- 实验或效果：模型达到96.23%准确率，优于传统CNN和基于Transformer的模型，显示高泛化能力。

## 摘要（原文）

> The early detection of pancreatic neoplasm is a major clinical dilemma, and it is predominantly so because tumors are likely to occur with minimal contrast margins and a large spread anatomy-wide variation amongst patients on a CT scan. These complexities require to be addressed with an effective and scalable system that can assist in enhancing the salience of the subtle visual cues and provide a high level of the generalization on the multimodal imaging data. A Scalable Residual Feature Aggregation (SRFA) framework is proposed to be used to meet these conditions in this study. The framework integrates a pipeline of preprocessing followed by the segmentation using the MAGRes-UNet that is effective in making the pancreatic structures and isolating regions of interest more visible. DenseNet-121 performed with residual feature storage is used to extract features to allow deep hierarchical features to be aggregated without properties loss. To go further, hybrid HHO-BA metaheuristic feature selection strategy is used, which guarantees the best feature subset refinement. To be classified, the system is trained based on a new hybrid model that integrates the ability to pay attention on the world, which is the Vision Transformer (ViT) with the high representational efficiency of EfficientNet-B3. A dual optimization mechanism incorporating SSA and GWO is used to fine-tune hyperparameters to enhance greater robustness and less overfitting. Experimental results support the significant improvement in performance, with the suggested model reaching 96.23% accuracy, 95.58% F1-score and 94.83% specificity, the model is significantly better than the traditional CNNs and contemporary transformer-based models. Such results highlight the possibility of the SRFA framework as a useful instrument in the early detection of pancreatic tumors.

