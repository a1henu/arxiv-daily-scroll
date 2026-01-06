---
layout: default
title: SketchRodGS: Sketch-based Extraction of Slender Geometries for Animating Gaussian Splatting Scenes
---

# SketchRodGS: Sketch-based Extraction of Slender Geometries for Animating Gaussian Splatting Scenes
**arXiv**：[2601.02072v1](https://arxiv.org/abs/2601.02072) · [PDF](https://arxiv.org/pdf/2601.02072.pdf)  
**作者**：Haato Watanabe, Nobuyuki Umetani  

**一句话要点**：提出基于草图的细长几何提取方法，用于高斯溅射场景的物理动画模拟。

**关键词**：高斯溅射, 细长几何提取, 草图交互, 物理模拟, 折线表示, 动态规划

## 3 点简述
- 核心问题：高斯溅射缺乏连接信息，难以直接构建细长物体的折线表示。
- 方法要点：利用用户草图输入，通过屏幕空间最短路径分析稳健提取折线网格。
- 实验或效果：在多个实际场景中验证了方法的有效性和鲁棒性。

## 摘要（原文）

> Physics simulation of slender elastic objects often requires discretization as a polyline. However, constructing a polyline from Gaussian splatting is challenging as Gaussian splatting lacks connectivity information and the configuration of Gaussian primitives contains much noise. This paper presents a method to extract a polyline representation of the slender part of the objects in a Gaussian splatting scene from the user's sketching input. Our method robustly constructs a polyline mesh that represents the slender parts using the screen-space shortest path analysis that can be efficiently solved using dynamic programming. We demonstrate the effectiveness of our approach in several in-the-wild examples.

