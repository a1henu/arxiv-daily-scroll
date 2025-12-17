---
layout: default
title: ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM
---

# ACE-SLAM: Scene Coordinate Regression for Neural Implicit Real-Time SLAM
**arXiv**：[2512.14032v1](https://arxiv.org/abs/2512.14032) · [PDF](https://arxiv.org/pdf/2512.14032.pdf)  
**作者**：Ignacio Alzugaray, Marwan Taher, Andrew J. Davison  

**一句话要点**：提出基于场景坐标回归的神经隐式实时SLAM系统，实现严格实时RGB-D建图与定位。

**关键词**：神经隐式SLAM, 场景坐标回归, 实时RGB-D建图, 轻量级网络, 动态环境鲁棒性

## 3 点简述
- 核心问题：神经隐式SLAM中实时性与地图表示效率的挑战。
- 方法要点：采用轻量级网络直接映射2D图像特征到3D全局坐标作为核心地图表示。
- 实验或效果：在合成和真实基准测试中展示竞争性能，支持动态环境无需特殊适应。

## 摘要（原文）

> We present a novel neural RGB-D Simultaneous Localization And Mapping (SLAM) system that learns an implicit map of the scene in real time. For the first time, we explore the use of Scene Coordinate Regression (SCR) as the core implicit map representation in a neural SLAM pipeline, a paradigm that trains a lightweight network to directly map 2D image features to 3D global coordinates. SCR networks provide efficient, low-memory 3D map representations, enable extremely fast relocalization, and inherently preserve privacy, making them particularly suitable for neural implicit SLAM.
>   Our system is the first one to achieve strict real-time in neural implicit RGB-D SLAM by relying on a SCR-based representation. We introduce a novel SCR architecture specifically tailored for this purpose and detail the critical design choices required to integrate SCR into a live SLAM pipeline. The resulting framework is simple yet flexible, seamlessly supporting both sparse and dense features, and operates reliably in dynamic environments without special adaptation. We evaluate our approach on established synthetic and real-world benchmarks, demonstrating competitive performance against the state of the art. Project Page: https://github.com/ialzugaray/ace-slam

