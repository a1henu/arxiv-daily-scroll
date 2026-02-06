---
layout: default
title: Predicting Camera Pose from Perspective Descriptions for Spatial Reasoning
---

# Predicting Camera Pose from Perspective Descriptions for Spatial Reasoning
**arXiv**：[2602.06041v1](https://arxiv.org/abs/2602.06041) · [PDF](https://arxiv.org/pdf/2602.06041.pdf)  
**作者**：Xuejun Zhang, Aditi Tiwari, Zhenhailong Wang, Heng Ji  

**一句话要点**：提出CAMCUE框架，利用相机姿态作为几何锚点解决多图像空间推理中的视角转换问题。

**关键词**：多图像空间推理, 相机姿态预测, 视角转换, 多模态大语言模型, 几何锚点, 姿态条件视图合成

## 3 点简述
- 核心问题：多模态大语言模型在多图像空间推理中难以构建跨视角的连贯3D理解。
- 方法要点：通过注入每视角姿态到视觉令牌，将自然语言视角描述映射到目标相机姿态，并合成姿态条件的目标视图。
- 实验或效果：在CAMCUE-DATA数据集上提升9.06%准确率，姿态预测旋转精度超90%在20°内，推理时间从256.6秒降至1.45秒。

## 摘要（原文）

> Multi-image spatial reasoning remains challenging for current multimodal large language models (MLLMs). While single-view perception is inherently 2D, reasoning over multiple views requires building a coherent scene understanding across viewpoints. In particular, we study perspective taking, where a model must build a coherent 3D understanding from multi-view observations and use it to reason from a new, language-specified viewpoint. We introduce CAMCUE, a pose-aware multi-image framework that uses camera pose as an explicit geometric anchor for cross-view fusion and novel-view reasoning. CAMCUE injects per-view pose into visual tokens, grounds natural-language viewpoint descriptions to a target camera pose, and synthesizes a pose-conditioned imagined target view to support answering. To support this setting, we curate CAMCUE-DATA with 27,668 training and 508 test instances pairing multi-view images and poses with diverse target-viewpoint descriptions and perspective-shift questions. We also include human-annotated viewpoint descriptions in the test split to evaluate generalization to human language. CAMCUE improves overall accuracy by 9.06% and predicts target poses from natural-language viewpoint descriptions with over 90% rotation accuracy within 20° and translation accuracy within a 0.5 error threshold. This direct grounding avoids expensive test-time search-and-match, reducing inference time from 256.6s to 1.45s per example and enabling fast, interactive use in real-world scenarios.

