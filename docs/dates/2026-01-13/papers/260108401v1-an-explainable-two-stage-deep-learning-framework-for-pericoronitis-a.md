---
layout: default
title: An Explainable Two Stage Deep Learning Framework for Pericoronitis Assessment in Panoramic Radiographs Using YOLOv8 and ResNet-50
---

# An Explainable Two Stage Deep Learning Framework for Pericoronitis Assessment in Panoramic Radiographs Using YOLOv8 and ResNet-50
**arXiv**：[2601.08401v1](https://arxiv.org/abs/2601.08401) · [PDF](https://arxiv.org/pdf/2601.08401.pdf)  
**作者**：Ajo Babu George, Pranav S, Kunal Agarwal  

**一句话要点**：提出基于YOLOv8和ResNet-50的两阶段深度学习框架，用于全景X光片中的冠周炎评估，并集成可解释性AI增强临床信任。

**关键词**：全景X光片分析, 冠周炎评估, 两阶段深度学习, YOLOv8, ResNet-50, 可解释性AI

## 3 点简述
- 核心问题：全景X光片中冠周炎诊断存在挑战，需结合解剖定位、病理分类和可解释性。
- 方法要点：采用两阶段流程，YOLOv8检测第三磨牙并分类，ResNet-50识别冠周炎特征，使用Grad-CAM提供可视化解释。
- 实验或效果：YOLOv8精度达92%，ResNet-50分类F1分数为88%（正常）和86%（冠周炎），Grad-CAM与放射科医生诊断一致性为84%。

## 摘要（原文）

> Objectives: To overcome challenges in diagnosing pericoronitis on panoramic radiographs, an AI-assisted assessment system integrating anatomical localization, pathological classification, and interpretability. Methods: A two-stage deep learning pipeline was implemented. The first stage used YOLOv8 to detect third molars and classify their anatomical positions and angulations based on Winter's classification. Detected regions were then fed into a second-stage classifier, a modified ResNet-50 architecture, for detecting radiographic features suggestive of pericoronitis. To enhance clinical trust, Grad-CAM was used to highlight key diagnostic regions on the radiographs. Results: The YOLOv8 component achieved 92% precision and 92.5% mean average precision. The ResNet-50 classifier yielded F1-scores of 88% for normal cases and 86% for pericoronitis. Radiologists reported 84% alignment between Grad-CAM and their diagnostic impressions, supporting the radiographic relevance of the interpretability output. Conclusion: The system shows strong potential for AI-assisted panoramic assessment, with explainable AI features that support clinical confidence.

