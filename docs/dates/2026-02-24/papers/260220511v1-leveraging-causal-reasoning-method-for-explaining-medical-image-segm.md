---
layout: default
title: Leveraging Causal Reasoning Method for Explaining Medical Image Segmentation Models
---

# Leveraging Causal Reasoning Method for Explaining Medical Image Segmentation Models
**arXiv**：[2602.20511v1](https://arxiv.org/abs/2602.20511) · [PDF](https://arxiv.org/pdf/2602.20511.pdf)  
**作者**：Limai Jiang, Ruitao Xie, Bokai Yang, Huazhen Huang, Juan He, Yufu Huo, Zikai Wang, Yang Wei, Yunpeng Cai  

**一句话要点**：提出基于因果推理的医学图像分割模型解释方法，以提升模型可信度。

**关键词**：医学图像分割, 模型解释性, 因果推理, 平均处理效应, 深度学习

## 3 点简述
- 核心问题：医学图像分割模型的黑盒特性在临床应用中引发信任担忧。
- 方法要点：利用因果推断框架，通过平均处理效应量化输入区域和网络组件对分割结果的影响。
- 实验或效果：在多个数据集上验证，相比现有方法提供更忠实解释，并揭示模型感知策略异质性。

## 摘要（原文）

> Medical image segmentation plays a vital role in clinical decision-making, enabling precise localization of lesions and guiding interventions. Despite significant advances in segmentation accuracy, the black-box nature of most deep models has raised growing concerns about their trustworthiness in high-stakes medical scenarios. Current explanation techniques have primarily focused on classification tasks, leaving the segmentation domain relatively underexplored. We introduced an explanation model for segmentation task which employs the causal inference framework and backpropagates the average treatment effect (ATE) into a quantification metric to determine the influence of input regions, as well as network components, on target segmentation areas. Through comparison with recent segmentation explainability techniques on two representative medical imaging datasets, we demonstrated that our approach provides more faithful explanations than existing approaches. Furthermore, we carried out a systematic causal analysis of multiple foundational segmentation models using our method, which reveals significant heterogeneity in perceptual strategies across different models, and even between different inputs for the same model. Suggesting the potential of our method to provide notable insights for optimizing segmentation models. Our code can be found at https://github.com/lcmmai/PdCR.

