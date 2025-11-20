---
layout: default
title: FunnyNodules: A Customizable Medical Dataset Tailored for Evaluating Explainable AI
---

# FunnyNodules: A Customizable Medical Dataset Tailored for Evaluating Explainable AI
**arXiv**：[2511.15481v1](https://arxiv.org/abs/2511.15481) · [PDF](https://arxiv.org/pdf/2511.15481.pdf)  
**作者**：Luisa Gallée, Yiheng Xiong, Meinrad Beer, Michael Götz  

**一句话要点**：提出FunnyNodules合成数据集以评估医学图像中可解释AI的属性推理能力

**关键词**：可解释AI, 合成医学数据集, 属性推理, 肺结节分析, 模型评估, 注意力对齐

## 3 点简述
- 医学图像数据集缺乏推理相关标注，阻碍可解释AI模型开发与评估
- FunnyNodules生成可控属性肺结节形状，支持自定义决策规则与属性-类别关系
- 用于模型无关评估，分析属性预测性能与注意力对齐，提供完整真实信息

## 摘要（原文）

> Densely annotated medical image datasets that capture not only diagnostic labels but also the underlying reasoning behind these diagnoses are scarce. Such reasoning-related annotations are essential for developing and evaluating explainable AI (xAI) models that reason similarly to radiologists: making correct predictions for the right reasons. To address this gap, we introduce FunnyNodules, a fully parameterized synthetic dataset designed for systematic analysis of attribute-based reasoning in medical AI models. The dataset generates abstract, lung nodule-like shapes with controllable visual attributes such as roundness, margin sharpness, and spiculation. Target class is derived from a predefined attribute combination, allowing full control over the decision rule that links attributes to the diagnostic class. We demonstrate how FunnyNodules can be used in model-agnostic evaluations to assess whether models learn correct attribute-target relations, to interpret over- or underperformance in attribute prediction, and to analyze attention alignment with attribute-specific regions of interest. The framework is fully customizable, supporting variations in dataset complexity, target definitions, class balance, and beyond. With complete ground truth information, FunnyNodules provides a versatile foundation for developing, benchmarking, and conducting in-depth analyses of explainable AI methods in medical image analysis.

