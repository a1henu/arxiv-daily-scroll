---
layout: default
title: Radar2Shape: 3D Shape Reconstruction from High-Frequency Radar using Multiresolution Signed Distance Functions
---

# Radar2Shape: 3D Shape Reconstruction from High-Frequency Radar using Multiresolution Signed Distance Functions
**arXiv**：[2511.17484v1](https://arxiv.org/abs/2511.17484) · [PDF](https://arxiv.org/pdf/2511.17484.pdf)  
**作者**：Neel Sortur, Justin Goodwin, Purvik Patel, Luis Enrique Martinez, Tzofi Klinghoffer, Rajmonda S. Caceres, Robin Walters  

**一句话要点**：提出Radar2Shape扩散模型，从部分观测高频雷达信号重建任意3D形状

**关键词**：3D形状重建, 高频雷达, 去噪扩散模型, 多分辨率特征, 部分观测信号

## 3 点简述
- 核心问题：高频雷达信号形状重建复杂，现有方法难处理部分观测和任意形状
- 方法要点：使用去噪扩散模型，关联雷达频率与多分辨率形状特征
- 实验或效果：在模拟和真实数据上验证，能泛化并重建任意形状

## 摘要（原文）

> Determining the shape of 3D objects from high-frequency radar signals is analytically complex but critical for commercial and aerospace applications. Previous deep learning methods have been applied to radar modeling; however, they often fail to represent arbitrary shapes or have difficulty with real-world radar signals which are collected over limited viewing angles. Existing methods in optical 3D reconstruction can generate arbitrary shapes from limited camera views, but struggle when they naively treat the radar signal as a camera view. In this work, we present Radar2Shape, a denoising diffusion model that handles a partially observable radar signal for 3D reconstruction by correlating its frequencies with multiresolution shape features. Our method consists of a two-stage approach: first, Radar2Shape learns a regularized latent space with hierarchical resolutions of shape features, and second, it diffuses into this latent space by conditioning on the frequencies of the radar signal in an analogous coarse-to-fine manner. We demonstrate that Radar2Shape can successfully reconstruct arbitrary 3D shapes even from partially-observed radar signals, and we show robust generalization to two different simulation methods and real-world data. Additionally, we release two synthetic benchmark datasets to encourage future research in the high-frequency radar domain so that models like Radar2Shape can safely be adapted into real-world radar systems.

