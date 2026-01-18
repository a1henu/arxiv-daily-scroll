---
layout: default
title: WildRayZer: Self-supervised Large View Synthesis in Dynamic Environments
---

# WildRayZer: Self-supervised Large View Synthesis in Dynamic Environments
**arXiv**：[2601.10716v1](https://arxiv.org/abs/2601.10716) · [PDF](https://arxiv.org/pdf/2601.10716.pdf)  
**作者**：Xuweiyi Chen, Wentao Zhou, Zezhou Cheng  

**一句话要点**：提出WildRayZer自监督框架以解决动态环境中新视角合成的多视图一致性问题。

**关键词**：新视角合成, 动态环境, 自监督学习, 运动估计, 数据集构建

## 3 点简述
- 核心问题：动态内容破坏多视图一致性，导致鬼影、几何幻觉和姿态估计不稳定。
- 方法要点：通过分析-合成测试分离静态与瞬态区域，构建伪运动掩码并蒸馏运动估计器以聚焦背景监督。
- 实验或效果：在动态数据集上优于基线方法，实现单次前向传播的高质量新视角合成。

## 摘要（原文）

> We present WildRayZer, a self-supervised framework for novel view synthesis (NVS) in dynamic environments where both the camera and objects move. Dynamic content breaks the multi-view consistency that static NVS models rely on, leading to ghosting, hallucinated geometry, and unstable pose estimation. WildRayZer addresses this by performing an analysis-by-synthesis test: a camera-only static renderer explains rigid structure, and its residuals reveal transient regions. From these residuals, we construct pseudo motion masks, distill a motion estimator, and use it to mask input tokens and gate loss gradients so supervision focuses on cross-view background completion. To enable large-scale training and evaluation, we curate Dynamic RealEstate10K (D-RE10K), a real-world dataset of 15K casually captured dynamic sequences, and D-RE10K-iPhone, a paired transient and clean benchmark for sparse-view transient-aware NVS. Experiments show that WildRayZer consistently outperforms optimization-based and feed-forward baselines in both transient-region removal and full-frame NVS quality with a single feed-forward pass.

