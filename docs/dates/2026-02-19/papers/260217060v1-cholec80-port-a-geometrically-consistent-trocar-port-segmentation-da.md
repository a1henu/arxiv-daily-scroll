---
layout: default
title: Cholec80-port: A Geometrically Consistent Trocar Port Segmentation Dataset for Robust Surgical Scene Understanding
---

# Cholec80-port: A Geometrically Consistent Trocar Port Segmentation Dataset for Robust Surgical Scene Understanding
**arXiv**：[2602.17060v1](https://arxiv.org/abs/2602.17060) · [PDF](https://arxiv.org/pdf/2602.17060.pdf)  
**作者**：Shunsuke Kikuchi, Atsushi Kouno, Hiroki Matsuzaki  

**一句话要点**：提出Cholec80-port数据集以解决腹腔镜手术中套管端口几何一致分割问题

**关键词**：腹腔镜手术, 套管端口分割, 几何一致性, 数据集标注, 手术场景理解, 跨数据集鲁棒性

## 3 点简述
- 套管端口在腹腔镜视图中持续遮挡，影响几何下游任务如3D重建和SLAM
- 数据集提供高保真端口分割标注，排除中央开口以保持几何一致性
- 实验显示几何一致标注显著提升跨数据集鲁棒性，优于仅增加数据量

## 摘要（原文）

> Trocar ports are camera-fixed, pseudo-static structures that can persistently occlude laparoscopic views and attract disproportionate feature points due to specular, textured surfaces. This makes ports particularly detrimental to geometry-based downstream pipelines such as image stitching, 3D reconstruction, and visual SLAM, where dynamic or non-anatomical outliers degrade alignment and tracking stability. Despite this practical importance, explicit port labels are rare in public surgical datasets, and existing annotations often violate geometric consistency by masking the central lumen (opening), even when anatomical regions are visible through it. We present Cholec80-port, a high-fidelity trocar port segmentation dataset derived from Cholec80, together with a rigorous standard operating procedure (SOP) that defines a port-sleeve mask excluding the central opening. We additionally cleanse and unify existing public datasets under the same SOP. Experiments demonstrate that geometrically consistent annotations substantially improve cross-dataset robustness beyond what dataset size alone provides.

