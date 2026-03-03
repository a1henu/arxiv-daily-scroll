---
layout: default
title: Diagnosing Generalization Failures from Representational Geometry Markers
---

# Diagnosing Generalization Failures from Representational Geometry Markers
**arXiv**：[2603.01879v1](https://arxiv.org/abs/2603.01879) · [PDF](https://arxiv.org/pdf/2603.01879.pdf)  
**作者**：Chi-Ning Chou, Artem Kirsanov, Yao-Yuan Yang, SueYeon Chung  

**一句话要点**：提出基于表征几何标记的通用方法，以预测模型在分布外场景的泛化失败。

**关键词**：泛化失败预测, 表征几何, 分布外泛化, 模型选择, AI可解释性, 图像分类

## 3 点简述
- 核心问题：传统方法难以提供高层预测信号来预判模型在真实部署中的泛化失败。
- 方法要点：采用“自上而下”策略，设计网络标记作为系统级指标，关联任务相关几何属性与泛化性能。
- 实验或效果：在图像分类中，发现有效流形维度和效用等几何度量能可靠预测分布外性能，优于分布内准确率。

## 摘要（原文）

> Generalization, the ability to perform well beyond the training context, is a hallmark of biological and artificial intelligence, yet anticipating unseen failures remains a central challenge. Conventional approaches often take a ``bottom-up'' mechanistic route by reverse-engineering interpretable features or circuits to build explanatory models. While insightful, these methods often struggle to provide the high-level, predictive signals for anticipating failure in real-world deployment. Here, we propose using a ``top-down'' approach to studying generalization failures inspired by medical biomarkers: identifying system-level measurements that serve as robust indicators of a model's future performance. Rather than mapping out detailed internal mechanisms, we systematically design and test network markers to probe structure, function links, identify prognostic indicators, and validate predictions in real-world settings. In image classification, we find that task-relevant geometric properties of in-distribution (ID) object manifolds consistently forecast poor out-of-distribution (OOD) generalization. In particular, reductions in two geometric measures, effective manifold dimensionality and utility, predict weaker OOD performance across diverse architectures, optimizers, and datasets. We apply this finding to transfer learning with ImageNet-pretrained models. We consistently find that the same geometric patterns predict OOD transfer performance more reliably than ID accuracy. This work demonstrates that representational geometry can expose hidden vulnerabilities, offering more robust guidance for model selection and AI interpretability.

