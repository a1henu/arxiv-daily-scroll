---
layout: default
title: DynamicVerse: A Physically-Aware Multimodal Framework for 4D World Modeling
---

# DynamicVerse: A Physically-Aware Multimodal Framework for 4D World Modeling
**arXiv**：[2512.03000v1](https://arxiv.org/abs/2512.03000) · [PDF](https://arxiv.org/pdf/2512.03000.pdf)  
**作者**：Kairun Wen, Yuzhi Huang, Runyu Chen, Hui Zheng, Yunlong Lin, Panwang Pan, Chenxin Li, Wenyan Cong, Jian Zhang, Junbin Lu, Chenguo Lin, Dilin Wang, Zhicheng Yan, Hongyu Xu, Justin Theiss, Yue Huang, Xinghao Ding, Rakesh Ranjan, Zhiwen Fan  

**一句话要点**：提出DynamicVerse框架，通过多模态4D建模解决动态真实世界视频的物理尺度理解问题。

**关键词**：4D世界建模, 动态视频理解, 多模态框架, 物理尺度估计, 长视频序列处理, 真实世界视频分析

## 3 点简述
- 现有数据集和方法在从单目视频准确解释真实世界动态方面存在限制，如模拟器依赖和描述性标注不足。
- 采用大型视觉、几何和多模态模型，结合基于窗口的捆绑调整与全局优化，实现度量尺度静态几何、动态运动、实例掩码和描述性字幕的整合。
- 在视频深度估计、相机姿态估计和相机内参估计三个基准任务上，实验显示该方法在捕获物理尺度测量方面优于现有方法。

## 摘要（原文）

> Understanding the dynamic physical world, characterized by its evolving 3D structure, real-world motion, and semantic content with textual descriptions, is crucial for human-agent interaction and enables embodied agents to perceive and act within real environments with human-like capabilities. However, existing datasets are often derived from limited simulators or utilize traditional Structurefrom-Motion for up-to-scale annotation and offer limited descriptive captioning, which restricts the capacity of foundation models to accurately interpret real-world dynamics from monocular videos, commonly sourced from the internet. To bridge these gaps, we introduce DynamicVerse, a physical-scale, multimodal 4D world modeling framework for dynamic real-world video. We employ large vision, geometric, and multimodal models to interpret metric-scale static geometry, real-world dynamic motion, instance-level masks, and holistic descriptive captions. By integrating window-based Bundle Adjustment with global optimization, our method converts long real-world video sequences into a comprehensive 4D multimodal format. DynamicVerse delivers a large-scale dataset consists of 100K+ videos with 800K+ annotated masks and 10M+ frames from internet videos. Experimental evaluations on three benchmark tasks, namely video depth estimation, camera pose estimation, and camera intrinsics estimation, demonstrate that our 4D modeling achieves superior performance in capturing physical-scale measurements with greater global accuracy than existing methods.

