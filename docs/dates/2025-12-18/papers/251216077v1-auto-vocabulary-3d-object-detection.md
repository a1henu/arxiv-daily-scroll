---
layout: default
title: Auto-Vocabulary 3D Object Detection
---

# Auto-Vocabulary 3D Object Detection
**arXiv**：[2512.16077v1](https://arxiv.org/abs/2512.16077) · [PDF](https://arxiv.org/pdf/2512.16077.pdf)  
**作者**：Haomeng Zhang, Kuan-Chuan Peng, Suhas Lohit, Raymond A. Yeh  

**一句话要点**：提出AV3DOD框架，实现无需用户输入的自动词汇3D物体检测

**关键词**：自动词汇3D检测, 视觉语言模型, 语义评分, 开放词汇检测, 3D物体定位

## 3 点简述
- 核心问题：现有开放词汇3D检测依赖用户指定类别，需自动生成类别名称
- 方法要点：利用2D视觉语言模型生成语义候选，通过图像描述和特征扩展提升语义质量
- 实验或效果：在ScanNetV2和SUNRGB-D数据集上实现SOTA，定位和语义质量均领先

## 摘要（原文）

> Open-vocabulary 3D object detection methods are able to localize 3D boxes of classes unseen during training. Despite the name, existing methods rely on user-specified classes both at training and inference. We propose to study Auto-Vocabulary 3D Object Detection (AV3DOD), where the classes are automatically generated for the detected objects without any user input. To this end, we introduce Semantic Score (SS) to evaluate the quality of the generated class names. We then develop a novel framework, AV3DOD, which leverages 2D vision-language models (VLMs) to generate rich semantic candidates through image captioning, pseudo 3D box generation, and feature-space semantics expansion. AV3DOD achieves the state-of-the-art (SOTA) performance on both localization (mAP) and semantic quality (SS) on the ScanNetV2 and SUNRGB-D datasets. Notably, it surpasses the SOTA, CoDA, by 3.48 overall mAP and attains a 24.5% relative improvement in SS on ScanNetV2.

