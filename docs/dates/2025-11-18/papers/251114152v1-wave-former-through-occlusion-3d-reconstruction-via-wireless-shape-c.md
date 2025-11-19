---
layout: default
title: Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion
---

# Wave-Former: Through-Occlusion 3D Reconstruction via Wireless Shape Completion
**arXiv**：[2511.14152v1](https://arxiv.org/abs/2511.14152) · [PDF](https://arxiv.org/pdf/2511.14152.pdf)  
**作者**：Laura Dodds, Maisy Lam, Waleed Akbar, Yibo Cheng, Fadel Adib  

**一句话要点**：提出Wave-Former以通过无线信号完成遮挡物体的3D重建

**关键词**：3D重建, 毫米波信号, 形状补全, 变换器模型, 遮挡处理

## 3 点简述
- 核心问题：毫米波重建方法在遮挡场景下覆盖有限且噪声高
- 方法要点：采用三阶段流程，结合物理感知和变换器模型进行形状补全
- 实验或效果：在真实数据上召回率从54%提升至72%，精度保持85%

## 摘要（原文）

> We present Wave-Former, a novel method capable of high-accuracy 3D shape reconstruction for completely occluded, diverse, everyday objects. This capability can open new applications spanning robotics, augmented reality, and logistics. Our approach leverages millimeter-wave (mmWave) wireless signals, which can penetrate common occlusions and reflect off hidden objects. In contrast to past mmWave reconstruction methods, which suffer from limited coverage and high noise, Wave-Former introduces a physics-aware shape completion model capable of inferring full 3D geometry. At the heart of Wave-Former's design is a novel three-stage pipeline which bridges raw wireless signals with recent advancements in vision-based shape completion by incorporating physical properties of mmWave signals. The pipeline proposes candidate geometric surfaces, employs a transformer-based shape completion model designed specifically for mmWave signals, and finally performs entropy-guided surface selection. This enables Wave-Former to be trained using entirely synthetic point-clouds, while demonstrating impressive generalization to real-world data.In head-to-head comparisons with state-of-the-art baselines, Wave-Former raises recall from 54% to 72% while maintaining a high precision of 85%.

