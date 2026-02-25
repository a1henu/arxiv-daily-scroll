---
layout: default
title: CAD-Prompted SAM3: Geometry-Conditioned Instance Segmentation for Industrial Objects
---

# CAD-Prompted SAM3: Geometry-Conditioned Instance Segmentation for Industrial Objects
**arXiv**：[2602.20551v1](https://arxiv.org/abs/2602.20551) · [PDF](https://arxiv.org/pdf/2602.20551.pdf)  
**作者**：Zhenran Tang, Rohan Nagabhirava, Changliu Liu  

**一句话要点**：提出CAD提示的SAM3框架，以解决工业场景中基于几何的实例分割问题。

**关键词**：实例分割, CAD提示, 几何条件, 工业视觉, 合成数据训练

## 3 点简述
- 核心问题：语言或外观提示在工业对象分割中不可靠，因对象可能材质多样或难以描述。
- 方法要点：使用CAD模型多视图渲染作为几何提示，训练基于SAM3的单阶段分割模型。
- 实验或效果：通过合成数据训练，实现独立于外观的稳健分割，适用于制造和3D打印环境。

## 摘要（原文）

> Verbal-prompted segmentation is inherently limited by the expressiveness of natural language and struggles with uncommon, instance-specific, or difficult-to-describe objects: scenarios frequently encountered in manufacturing and 3D printing environments. While image exemplars provide an alternative, they primarily encode appearance cues such as color and texture, which are often unrelated to a part's geometric identity. In industrial settings, a single component may be produced in different materials, finishes, or colors, making appearance-based prompting unreliable. In contrast, such objects are typically defined by precise CAD models that capture their canonical geometry. We propose a CAD-prompted segmentation framework built on SAM3 that uses canonical multi-view renderings of a CAD model as prompt input. The rendered views provide geometry-based conditioning independent of surface appearance. The model is trained using synthetic data generated from mesh renderings in simulation under diverse viewpoints and scene contexts. Our approach enables single-stage, CAD-prompted mask prediction, extending promptable segmentation to objects that cannot be robustly described by language or appearance alone.

