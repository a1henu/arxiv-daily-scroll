---
layout: default
title: REL-SF4PASS: Panoramic Semantic Segmentation with REL Depth Representation and Spherical Fusion
---

# REL-SF4PASS: Panoramic Semantic Segmentation with REL Depth Representation and Spherical Fusion
**arXiv**：[2601.16788v1](https://arxiv.org/abs/2601.16788) · [PDF](https://arxiv.org/pdf/2601.16788.pdf)  
**作者**：Xuewei Li, Xinghan Bao, Zhimin Chen, Xi Li  

**一句话要点**：提出REL-SF4PASS，通过圆柱坐标深度表示与球形动态融合解决全景语义分割问题。

**关键词**：全景语义分割, 深度表示, 圆柱坐标, 多模态融合, 球形几何, 3D扰动鲁棒性

## 3 点简述
- 全景语义分割中，现有方法未充分利用全景图像几何，如深度信息使用不足。
- 提出REL深度表示（含修正深度、仰角增益垂直倾角和横向方位角）和球形动态多模态融合SMMF。
- 在Stanford2D3D数据集上，平均mIoU提升2.35%，面对3D扰动时性能方差减少约70%。

## 摘要（原文）

> As an important and challenging problem in computer vision, Panoramic Semantic Segmentation (PASS) aims to give complete scene perception based on an ultra-wide angle of view. Most PASS methods often focus on spherical geometry with RGB input or using the depth information in original or HHA format, which does not make full use of panoramic image geometry. To address these shortcomings, we propose REL-SF4PASS with our REL depth representation based on cylindrical coordinate and Spherical-dynamic Multi-Modal Fusion SMMF. REL is made up of Rectified Depth, Elevation-Gained Vertical Inclination Angle, and Lateral Orientation Angle, which fully represents 3D space in cylindrical coordinate style and the surface normal direction. SMMF aims to ensure the diversity of fusion for different panoramic image regions and reduce the breakage of cylinder side surface expansion in ERP projection, which uses different fusion strategies to match the different regions in panoramic images. Experimental results show that REL-SF4PASS considerably improves performance and robustness on popular benchmark, Stanford2D3D Panoramic datasets. It gains 2.35% average mIoU improvement on all 3 folds and reduces the performance variance by approximately 70% when facing 3D disturbance.

