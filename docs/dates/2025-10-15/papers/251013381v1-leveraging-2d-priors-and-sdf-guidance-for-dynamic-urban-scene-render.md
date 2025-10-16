---
layout: default
title: Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering
---

# Leveraging 2D Priors and SDF Guidance for Dynamic Urban Scene Rendering
**arXiv**：[2510.13381v1](https://arxiv.org/abs/2510.13381) · [PDF](https://arxiv.org/pdf/2510.13381.pdf)  
**作者**：Siddharth Tourani, Jayaram Reddy, Akash Kumbar, Satyajit Tourani, Nishant Goyal, Madhava Krishna, N. Dinesh Reddy, Muhammad Haris Khan  

**一句话要点**：提出结合2D先验与SDF的3D高斯泼溅方法，提升动态城市场景渲染精度

**关键词**：动态场景渲染, 3D高斯泼溅, 符号距离函数, 城市场景重建, 场景编辑

## 3 点简述
- 核心问题：动态城市场景渲染需LiDAR和3D运动标注，依赖性强。
- 方法要点：集成SDF与3D高斯泼溅，利用深度和点跟踪先验优化几何与变形。
- 实验或效果：无LiDAR时渲染指标领先，结合LiDAR可增强重建与编辑能力。

## 摘要（原文）

> Dynamic scene rendering and reconstruction play a crucial role in computer
> vision and augmented reality. Recent methods based on 3D Gaussian Splatting
> (3DGS), have enabled accurate modeling of dynamic urban scenes, but for urban
> scenes they require both camera and LiDAR data, ground-truth 3D segmentations
> and motion data in the form of tracklets or pre-defined object templates such
> as SMPL. In this work, we explore whether a combination of 2D object agnostic
> priors in the form of depth and point tracking coupled with a signed distance
> function (SDF) representation for dynamic objects can be used to relax some of
> these requirements. We present a novel approach that integrates Signed Distance
> Functions (SDFs) with 3D Gaussian Splatting (3DGS) to create a more robust
> object representation by harnessing the strengths of both methods. Our unified
> optimization framework enhances the geometric accuracy of 3D Gaussian splatting
> and improves deformation modeling within the SDF, resulting in a more adaptable
> and precise representation. We demonstrate that our method achieves
> state-of-the-art performance in rendering metrics even without LiDAR data on
> urban scenes. When incorporating LiDAR, our approach improved further in
> reconstructing and generating novel views across diverse object categories,
> without ground-truth 3D motion annotation. Additionally, our method enables
> various scene editing tasks, including scene decomposition, and scene
> composition.

