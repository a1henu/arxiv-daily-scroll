---
layout: default
title: A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments
---

# A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments
**arXiv**：[2512.16184v1](https://arxiv.org/abs/2512.16184) · [PDF](https://arxiv.org/pdf/2512.16184.pdf)  
**作者**：Jaeho Yang, Kijung Yoon  

**一句话要点**：提出基于图表示的多模态框架，用于阿尔茨海默病早期诊断，结合立方体绘图与认知评估。

**关键词**：阿尔茨海默病诊断, 图神经网络, 多模态融合, 立方体绘图分析, 可解释性分析, 神经心理评估

## 3 点简述
- 核心问题：阿尔茨海默病早期检测困难，立方体绘图任务可评估视觉空间功能。
- 方法要点：将手绘立方体转换为图结构，融合人口统计和神经心理测试分数进行多模态分类。
- 实验或效果：图表示优于像素模型，多模态集成提升性能，SHAP分析揭示关键几何特征。

## 摘要（原文）

> Early and accessible detection of Alzheimer's disease (AD) remains a critical clinical challenge, and cube-copying tasks offer a simple yet informative assessment of visuospatial function. This work proposes a multimodal framework that converts hand-drawn cube sketches into graph-structured representations capturing geometric and topological properties, and integrates these features with demographic information and neuropsychological test (NPT) scores for AD classification. Cube drawings are modeled as graphs with node features encoding spatial coordinates, local graphlet-based topology, and angular geometry, which are processed using graph neural networks and fused with age, education, and NPT features in a late-fusion model. Experimental results show that graph-based representations provide a strong unimodal baseline and substantially outperform pixel-based convolutional models, while multimodal integration further improves performance and robustness to class imbalance. SHAP-based interpretability analysis identifies specific graphlet motifs and geometric distortions as key predictors, closely aligning with clinical observations of disorganized cube drawings in AD. Together, these results establish graph-based analysis of cube copying as an interpretable, non-invasive, and scalable approach for Alzheimer's disease screening.

