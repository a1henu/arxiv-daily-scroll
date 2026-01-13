---
layout: default
title: Leveraging 3D Representation Alignment and RGB Pretrained Priors for LiDAR Scene Generation
---

# Leveraging 3D Representation Alignment and RGB Pretrained Priors for LiDAR Scene Generation
**arXiv**：[2601.07692v1](https://arxiv.org/abs/2601.07692) · [PDF](https://arxiv.org/pdf/2601.07692.pdf)  
**作者**：Nicolas Sereyjol-Garros, Ellington Kirby, Victor Besnier, Nermin Samet  

**一句话要点**：提出R3DPA方法，利用3D表示对齐和RGB预训练先验解决LiDAR场景生成数据稀缺问题。

**关键词**：LiDAR场景生成, 3D表示对齐, RGB预训练先验, 点云控制, 自动驾驶数据增强

## 3 点简述
- 核心问题：LiDAR数据稀缺，限制自动驾驶等机器人任务中的场景生成。
- 方法要点：通过3D特征对齐和图像预训练模型知识迁移，提升生成质量并实现点云控制。
- 实验或效果：在KITTI-360基准上达到最先进性能，支持无条件模型下的对象修复和场景混合。

## 摘要（原文）

> LiDAR scene synthesis is an emerging solution to scarcity in 3D data for robotic tasks such as autonomous driving. Recent approaches employ diffusion or flow matching models to generate realistic scenes, but 3D data remains limited compared to RGB datasets with millions of samples. We introduce R3DPA, the first LiDAR scene generation method to unlock image-pretrained priors for LiDAR point clouds, and leverage self-supervised 3D representations for state-of-the-art results. Specifically, we (i) align intermediate features of our generative model with self-supervised 3D features, which substantially improves generation quality; (ii) transfer knowledge from large-scale image-pretrained generative models to LiDAR generation, mitigating limited LiDAR datasets; and (iii) enable point cloud control at inference for object inpainting and scene mixing with solely an unconditional model. On the KITTI-360 benchmark R3DPA achieves state of the art performance. Code and pretrained models are available at https://github.com/valeoai/R3DPA.

