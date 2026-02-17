---
layout: default
title: Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery
---

# Wrivinder: Towards Spatial Intelligence for Geo-locating Ground Images onto Satellite Imagery
**arXiv**：[2602.14929v1](https://arxiv.org/abs/2602.14929) · [PDF](https://arxiv.org/pdf/2602.14929.pdf)  
**作者**：Chandrakanth Gudavalli, Tajuddin Manhar Mohammed, Abhay Yadav, Ananth Vishnu Bhaskar, Hardik Prajapati, Cheng Peng, Rama Chellappa, Shivkumar Chandrasekaran, B. S. Manjunath  

**一句话要点**：提出Wrivinder框架，通过几何驱动方法实现无监督地面图像到卫星图像的跨视角对齐

**关键词**：跨视角对齐, 几何驱动框架, 零样本定位, 3D场景重建, 卫星图像匹配, 数据集基准

## 3 点简述
- 核心问题：地面图像与卫星图像对齐在视角差异大或GPS不可靠时仍具挑战性
- 方法要点：结合SfM重建、3D高斯溅射、语义接地和单目深度线索，生成稳定天顶视图渲染
- 实验或效果：在零样本实验中实现亚30米定位精度，并发布MC-Sat数据集支持评估

## 摘要（原文）

> Aligning ground-level imagery with geo-registered satellite maps is crucial for mapping, navigation, and situational awareness, yet remains challenging under large viewpoint gaps or when GPS is unreliable. We introduce Wrivinder, a zero-shot, geometry-driven framework that aggregates multiple ground photographs to reconstruct a consistent 3D scene and align it with overhead satellite imagery. Wrivinder combines SfM reconstruction, 3D Gaussian Splatting, semantic grounding, and monocular depth--based metric cues to produce a stable zenith-view rendering that can be directly matched to satellite context for metrically accurate camera geo-localization. To support systematic evaluation of this task, which lacks suitable benchmarks, we also release MC-Sat, a curated dataset linking multi-view ground imagery with geo-registered satellite tiles across diverse outdoor environments. Together, Wrivinder and MC-Sat provide a first comprehensive baseline and testbed for studying geometry-centered cross-view alignment without paired supervision. In zero-shot experiments, Wrivinder achieves sub-30\,m geolocation accuracy across both dense and large-area scenes, highlighting the promise of geometry-based aggregation for robust ground-to-satellite localization.

