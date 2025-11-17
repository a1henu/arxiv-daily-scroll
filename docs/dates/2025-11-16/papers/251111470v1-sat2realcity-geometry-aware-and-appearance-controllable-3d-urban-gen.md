---
layout: default
title: Sat2RealCity: Geometry-Aware and Appearance-Controllable 3D Urban Generation from Satellite Imagery
---

# Sat2RealCity: Geometry-Aware and Appearance-Controllable 3D Urban Generation from Satellite Imagery
**arXiv**：[2511.11470v1](https://arxiv.org/abs/2511.11470) · [PDF](https://arxiv.org/pdf/2511.11470.pdf)  
**作者**：Yijie Kang, Xinliang Wang, Zhenyu Wu, Yifeng Shi, Hailong Zhu  

**一句话要点**：提出Sat2RealCity框架，从卫星图像生成几何感知和外观可控的3D城市，解决数据依赖和真实性问题

**关键词**：3D城市生成, 卫星图像处理, 几何感知建模, 外观可控生成, 语义引导重建, OSM空间先验

## 3 点简述
- 核心问题：现有方法依赖大规模3D城市资产和语义/高度图，缺乏真实外观连接，限制生成城市真实性和泛化性
- 方法要点：基于OSM空间先验实现几何生成，外观引导建模控制风格，MLLM语义指导桥接语义与几何重建
- 实验或效果：实验显示在结构一致性和外观真实性上显著超越基线，支持真实世界对齐的3D城市内容创建

## 摘要（原文）

> Recent advances in generative modeling have substantially enhanced 3D urban generation, enabling applications in digital twins, virtual cities, and large-scale simulations. However, existing methods face two key challenges: (1) the need for large-scale 3D city assets for supervised training, which are difficult and costly to obtain, and (2) reliance on semantic or height maps, which are used exclusively for generating buildings in virtual worlds and lack connection to real-world appearance, limiting the realism and generalizability of generated cities. To address these limitations, we propose Sat2RealCity, a geometry-aware and appearance-controllable framework for 3D urban generation from real-world satellite imagery. Unlike previous city-level generation methods, Sat2RealCity builds generation upon individual building entities, enabling the use of rich priors and pretrained knowledge from 3D object generation while substantially reducing dependence on large-scale 3D city assets. Specifically, (1) we introduce the OSM-based spatial priors strategy to achieve interpretable geometric generation from spatial topology to building instances; (2) we design an appearance-guided controllable modeling mechanism for fine-grained appearance realism and style control; and (3) we construct an MLLM-powered semantic-guided generation pipeline, bridging semantic interpretation and geometric reconstruction. Extensive quantitative and qualitative experiments demonstrate that Sat2RealCity significantly surpasses existing baselines in structural consistency and appearance realism, establishing a strong foundation for real-world aligned 3D urban content creation. The code will be released soon.

