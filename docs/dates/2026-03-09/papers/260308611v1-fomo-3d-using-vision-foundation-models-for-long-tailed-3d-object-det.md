---
layout: default
title: FOMO-3D: Using Vision Foundation Models for Long-Tailed 3D Object Detection
---

# FOMO-3D: Using Vision Foundation Models for Long-Tailed 3D Object Detection
**arXiv**：[2603.08611v1](https://arxiv.org/abs/2603.08611) · [PDF](https://arxiv.org/pdf/2603.08611.pdf)  
**作者**：Anqi Joyce Yang, James Tu, Nikita Dvornik, Enxu Li, Raquel Urtasun  

**一句话要点**：提出FOMO-3D，利用视觉基础模型解决自动驾驶中长尾3D物体检测问题。

**关键词**：长尾3D检测, 视觉基础模型, 多模态融合, 自动驾驶, 两阶段检测, 语义先验

## 3 点简述
- 核心问题：自动驾驶需识别安全关键但训练数据稀少的物体，如施工工人，导致长尾检测困难。
- 方法要点：采用两阶段检测范式，结合LiDAR和相机分支生成提议，并利用OWLv2和Metric3Dv2的语义与深度先验进行精炼。
- 实验或效果：在真实驾驶数据上评估，显示通过精心设计的多模态融合，视觉基础模型先验带来显著性能提升。

## 摘要（原文）

> In order to navigate complex traffic environments, self-driving vehicles must recognize many semantic classes pertaining to vulnerable road users or traffic control devices. However, many safety-critical objects (e.g., construction worker) appear infrequently in nominal traffic conditions, leading to a severe shortage of training examples from driving data alone. Recent vision foundation models, which are trained on a large corpus of data, can serve as a good source of external prior knowledge to improve generalization. We propose FOMO-3D, the first multi-modal 3D detector to leverage vision foundation models for long-tailed 3D detection. Specifically, FOMO-3D exploits rich semantic and depth priors from OWLv2 and Metric3Dv2 within a two-stage detection paradigm that first generates proposals with a LiDAR-based branch and a novel camera-based branch, and refines them with attention especially to image features from OWL. Evaluations on real-world driving data show that using rich priors from vision foundation models with careful multi-modal fusion designs leads to large gains for long-tailed 3D detection. Project website is at https://waabi.ai/fomo3d/.

