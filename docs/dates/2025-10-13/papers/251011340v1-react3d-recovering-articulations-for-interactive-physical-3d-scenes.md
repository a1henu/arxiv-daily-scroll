---
layout: default
title: REACT3D: Recovering Articulations for Interactive Physical 3D Scenes
---

# REACT3D: Recovering Articulations for Interactive Physical 3D Scenes
**arXiv**：[2510.11340v1](https://arxiv.org/abs/2510.11340) · [PDF](https://arxiv.org/pdf/2510.11340.pdf)  
**作者**：Zhao Huang, Boyang Sun, Alexandros Delitzas, Jiaqi Chen, Marc Pollefeys  

**一句话要点**：提出REACT3D框架，将静态3D场景转换为交互式物理场景，以解决标注成本高的问题。

**关键词**：3D场景交互, 关节估计, 零样本学习, 物理模拟, 物体分割

## 3 点简述
- 核心问题：交互式3D场景标注成本高，限制数据集规模和下游任务应用。
- 方法要点：包括可开启物体检测、关节估计、隐藏几何补全和交互场景集成。
- 实验或效果：在检测/分割和关节指标上达到先进水平，支持大规模场景生成。

## 摘要（原文）

> Interactive 3D scenes are increasingly vital for embodied intelligence, yet
> existing datasets remain limited due to the labor-intensive process of
> annotating part segmentation, kinematic types, and motion trajectories. We
> present REACT3D, a scalable zero-shot framework that converts static 3D scenes
> into simulation-ready interactive replicas with consistent geometry, enabling
> direct use in diverse downstream tasks. Our contributions include: (i)
> openable-object detection and segmentation to extract candidate movable parts
> from static scenes, (ii) articulation estimation that infers joint types and
> motion parameters, (iii) hidden-geometry completion followed by interactive
> object assembly, and (iv) interactive scene integration in widely supported
> formats to ensure compatibility with standard simulation platforms. We achieve
> state-of-the-art performance on detection/segmentation and articulation metrics
> across diverse indoor scenes, demonstrating the effectiveness of our framework
> and providing a practical foundation for scalable interactive scene generation,
> thereby lowering the barrier to large-scale research on articulated scene
> understanding. Our project page is
> \textit{\hypersetup{urlcolor=black}\href{https://react3d.github.io/}{react3d.github.io}}.

