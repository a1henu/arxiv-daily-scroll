---
layout: default
title: CAMO: Category-Agnostic 3D Motion Transfer from Monocular 2D Videos
---

# CAMO: Category-Agnostic 3D Motion Transfer from Monocular 2D Videos
**arXiv**：[2601.02716v1](https://arxiv.org/abs/2601.02716) · [PDF](https://arxiv.org/pdf/2601.02716.pdf)  
**作者**：Taeyeon Kim, Youngju Na, Jumin Lee, Minhyuk Sung, Sung-Eui Yoon  

**一句话要点**：提出CAMO框架，从单目2D视频向多样3D网格进行类别无关的运动迁移，无需模板或3D监督。

**关键词**：3D运动迁移, 类别无关学习, 单目视频, 高斯溅射, 语义对应, 形状姿态优化

## 3 点简述
- 核心问题：2D视频到3D资产运动迁移存在姿态歧义和形状多样性，常依赖类别特定模板。
- 方法要点：结合形态参数化关节3D高斯溅射模型和密集语义对应，通过优化联合调整形状与姿态。
- 实验或效果：在多样类别和日常视频场景中，实现更优运动准确性、效率和视觉一致性。

## 摘要（原文）

> Motion transfer from 2D videos to 3D assets is a challenging problem, due to inherent pose ambiguities and diverse object shapes, often requiring category-specific parametric templates. We propose CAMO, a category-agnostic framework that transfers motion to diverse target meshes directly from monocular 2D videos without relying on predefined templates or explicit 3D supervision. The core of CAMO is a morphology-parameterized articulated 3D Gaussian splatting model combined with dense semantic correspondences to jointly adapt shape and pose through optimization. This approach effectively alleviates shape-pose ambiguities, enabling visually faithful motion transfer for diverse categories. Experimental results demonstrate superior motion accuracy, efficiency, and visual coherence compared to existing methods, significantly advancing motion transfer in varied object categories and casual video scenarios.

