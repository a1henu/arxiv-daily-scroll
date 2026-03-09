---
layout: default
title: Spatial Calibration of Diffuse LiDARs
---

# Spatial Calibration of Diffuse LiDARs
**arXiv**：[2603.06531v1](https://arxiv.org/abs/2603.06531) · [PDF](https://arxiv.org/pdf/2603.06531.pdf)  
**作者**：Nikhil Behari, Ramesh Raskar  

**一句话要点**：提出空间校准方法以解决漫反射LiDAR与RGB图像校准中的单射线假设违反问题。

**关键词**：漫反射LiDAR, 空间校准, 跨模态对齐, RGB图像融合, 像素响应图

## 3 点简述
- 核心问题：漫反射LiDAR像素因宽视场聚合光子返回，违反标准LiDAR-RGB校准的单射线假设。
- 方法要点：通过扫描反光贴片和背景减法，估计每个像素在RGB图像平面中的足迹和相对空间灵敏度。
- 实验或效果：在ams OSRAM TMF8828上演示，恢复像素响应图以支持跨模态对齐和融合。

## 摘要（原文）

> Diffuse direct time-of-flight LiDARs report per-pixel depth histograms formed by aggregating photon returns over a wide instantaneous field of view, violating the single-ray assumption behind standard LiDAR-RGB calibration. We present a simple spatial calibration procedure that estimates, for each diffuse LiDAR pixel, its footprint (effective support region) and relative spatial sensitivity in a co-located RGB image plane. Using a scanned retroreflective patch with background subtraction, we recover per-pixel response maps that provide an explicit LiDAR-to-RGB correspondence for cross-modal alignment and fusion. We demonstrate the method on the ams OSRAM TMF8828.

