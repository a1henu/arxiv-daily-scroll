---
layout: default
title: Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction
---

# Pygmalion Effect in Vision: Image-to-Clay Translation for Reflective Geometry Reconstruction
**arXiv**：[2511.21098v1](https://arxiv.org/abs/2511.21098) · [PDF](https://arxiv.org/pdf/2511.21098.pdf)  
**作者**：Gayoung Lee, Junho Kim, Jin-Hwa Kim, Junmo Kim  

**一句话要点**：提出图像到黏土翻译框架以解决反射物体3D重建问题

**关键词**：3D重建, 反射处理, 图像翻译, 双分支网络, 几何学习

## 3 点简述
- 核心问题：反射导致外观与几何纠缠，阻碍3D重建。
- 方法要点：双分支网络抑制镜面反射，保持几何一致性。
- 实验效果：在合成和真实数据集上提升法向精度和网格完整性。

## 摘要（原文）

> Understanding reflection remains a long-standing challenge in 3D reconstruction due to the entanglement of appearance and geometry under view-dependent reflections. In this work, we present the Pygmalion Effect in Vision, a novel framework that metaphorically "sculpts" reflective objects into clay-like forms through image-to-clay translation. Inspired by the myth of Pygmalion, our method learns to suppress specular cues while preserving intrinsic geometric consistency, enabling robust reconstruction from multi-view images containing complex reflections. Specifically, we introduce a dual-branch network in which a BRDF-based reflective branch is complemented by a clay-guided branch that stabilizes geometry and refines surface normals. The two branches are trained jointly using the synthesized clay-like images, which provide a neutral, reflection-free supervision signal that complements the reflective views. Experiments on both synthetic and real datasets demonstrate substantial improvement in normal accuracy and mesh completeness over existing reflection-handling methods. Beyond technical gains, our framework reveals that seeing by unshining, translating radiance into neutrality, can serve as a powerful inductive bias for reflective object geometry learning.

