---
layout: default
title: Skarimva: Skeleton-based Action Recognition is a Multi-view Application
---

# Skarimva: Skeleton-based Action Recognition is a Multi-view Application
**arXiv**：[2602.23231v1](https://arxiv.org/abs/2602.23231) · [PDF](https://arxiv.org/pdf/2602.23231.pdf)  
**作者**：Daniel Bermuth, Alexander Poeppel, Wolfgang Reif  

**一句话要点**：提出多视角三角化提升骨架数据质量，以增强骨架动作识别性能

**关键词**：骨架动作识别, 多视角三角化, 3D骨架数据, 输入数据质量, 动作识别模型

## 3 点简述
- 核心问题：骨架动作识别中，输入骨架数据质量常被忽视，成为模型性能瓶颈
- 方法要点：利用多相机视角三角化生成更精确的3D骨架，作为改进输入
- 实验或效果：实验表明，该方法能显著提升现有先进模型的识别准确率

## 摘要（原文）

> Human action recognition plays an important role when developing intelligent interactions between humans and machines. While there is a lot of active research on improving the machine learning algorithms for skeleton-based action recognition, not much attention has been given to the quality of the input skeleton data itself. This work demonstrates that by making use of multiple camera views to triangulate more accurate 3D~skeletons, the performance of state-of-the-art action recognition models can be improved significantly. This suggests that the quality of the input data is currently a limiting factor for the performance of these models. Based on these results, it is argued that the cost-benefit ratio of using multiple cameras is very favorable in most practical use-cases, therefore future research in skeleton-based action recognition should consider multi-view applications as the standard setup.

