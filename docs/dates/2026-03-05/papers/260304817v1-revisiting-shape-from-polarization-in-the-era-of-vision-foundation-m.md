---
layout: default
title: Revisiting Shape from Polarization in the Era of Vision Foundation Models
---

# Revisiting Shape from Polarization in the Era of Vision Foundation Models
**arXiv**：[2603.04817v1](https://arxiv.org/abs/2603.04817) · [PDF](https://arxiv.org/pdf/2603.04817.pdf)  
**作者**：Chenhao Li, Taishi Ono, Takeshi Uemori, Yusuke Moriuchi  

**一句话要点**：提出基于高质量合成数据与传感器感知增强的偏振形状重建方法，在单次物体表面法线估计中超越RGB视觉基础模型。

**关键词**：偏振形状重建, 表面法线估计, 视觉基础模型, 合成数据增强, 传感器噪声建模

## 3 点简述
- 核心问题：现有偏振形状重建方法因合成数据域差距和传感器噪声建模不足，性能落后于RGB视觉基础模型。
- 方法要点：使用1,954个真实扫描对象渲染高质量偏振数据集，结合DINOv3先验和传感器感知数据增强。
- 实验或效果：仅需4万训练场景，显著优于现有偏振和RGB方法，实现数据或参数大幅减少。

## 摘要（原文）

> We show that, with polarization cues, a lightweight model trained on a small dataset can outperform RGB-only vision foundation models (VFMs) in single-shot object-level surface normal estimation. Shape from polarization (SfP) has long been studied due to the strong physical relationship between polarization and surface geometry. Meanwhile, driven by scaling laws, RGB-only VFMs trained on large datasets have recently achieved impressive performance and surpassed existing SfP methods. This situation raises questions about the necessity of polarization cues, which require specialized hardware and have limited training data. We argue that the weaker performance of prior SfP methods does not come from the polarization modality itself, but from domain gaps. These domain gaps mainly arise from two sources. First, existing synthetic datasets use limited and unrealistic 3D objects, with simple geometry and random texture maps that do not match the underlying shapes. Second, real-world polarization signals are often affected by sensor noise, which is not well modeled during training. To address the first issue, we render a high-quality polarization dataset using 1,954 3D-scanned real-world objects. We further incorporate pretrained DINOv3 priors to improve generalization to unseen objects. To address the second issue, we introduce polarization sensor-aware data augmentation that better reflects real-world conditions. With only 40K training scenes, our method significantly outperforms both state-of-the-art SfP approaches and RGB-only VFMs. Extensive experiments show that polarization cues enable a 33x reduction in training data or an 8x reduction in model parameters, while still achieving better performance than RGB-only counterparts.

