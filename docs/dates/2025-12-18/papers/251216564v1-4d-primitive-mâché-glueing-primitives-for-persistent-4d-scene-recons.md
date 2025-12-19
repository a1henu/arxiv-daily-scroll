---
layout: default
title: 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction
---

# 4D Primitive-Mâché: Glueing Primitives for Persistent 4D Scene Reconstruction
**arXiv**：[2512.16564v1](https://arxiv.org/abs/2512.16564) · [PDF](https://arxiv.org/pdf/2512.16564.pdf)  
**作者**：Kirill Mazur, Marwan Taher, Andrew J. Davison  

**一句话要点**：提出4D Primitive-Mâché方法，通过粘合刚性基元实现持久4D场景重建

**关键词**：4D场景重建, 刚性基元分解, 运动外推, 单目视频处理, 持久重建

## 3 点简述
- 核心问题：从单目RGB视频重建完整且持久的4D场景，包括可见和不可见部分
- 方法要点：分解场景为刚性3D基元，通过优化推断其运动，并外推不可见物体运动
- 实验或效果：在物体扫描和多物体数据集上，定量和定性均显著优于现有方法

## 摘要（原文）

> We present a dynamic reconstruction system that receives a casual monocular RGB video as input, and outputs a complete and persistent reconstruction of the scene. In other words, we reconstruct not only the the currently visible parts of the scene, but also all previously viewed parts, which enables replaying the complete reconstruction across all timesteps.
>   Our method decomposes the scene into a set of rigid 3D primitives, which are assumed to be moving throughout the scene. Using estimated dense 2D correspondences, we jointly infer the rigid motion of these primitives through an optimisation pipeline, yielding a 4D reconstruction of the scene, i.e. providing 3D geometry dynamically moving through time. To achieve this, we also introduce a mechanism to extrapolate motion for objects that become invisible, employing motion-grouping techniques to maintain continuity.
>   The resulting system enables 4D spatio-temporal awareness, offering capabilities such as replayable 3D reconstructions of articulated objects through time, multi-object scanning, and object permanence. On object scanning and multi-object datasets, our system significantly outperforms existing methods both quantitatively and qualitatively.

