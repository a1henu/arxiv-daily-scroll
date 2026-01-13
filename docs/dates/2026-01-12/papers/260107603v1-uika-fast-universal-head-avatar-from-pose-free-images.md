---
layout: default
title: UIKA: Fast Universal Head Avatar from Pose-Free Images
---

# UIKA: Fast Universal Head Avatar from Pose-Free Images
**arXiv**：[2601.07603v1](https://arxiv.org/abs/2601.07603) · [PDF](https://arxiv.org/pdf/2601.07603.pdf)  
**作者**：Zijian Wu, Boyao Zhou, Liangxiao Hu, Hongyu Liu, Yuan Sun, Xuan Wang, Xun Cao, Yujun Shen, Hao Zhu  

**一句话要点**：提出UIKA以从无姿态图像快速生成通用头部化身

**关键词**：头部化身生成, UV引导建模, 可学习令牌, 高斯模型, 合成数据集

## 3 点简述
- 核心问题：传统化身方法依赖多视图捕获和长时间优化，难以从单图或视频快速生成。
- 方法要点：引入UV引导建模策略，通过像素级对应估计和可学习UV令牌，实现姿态无关的化身重建。
- 实验或效果：在单目和多视图设置中显著优于现有方法，支持从单图、多视图或视频输入生成。

## 摘要（原文）

> We present UIKA, a feed-forward animatable Gaussian head model from an arbitrary number of unposed inputs, including a single image, multi-view captures, and smartphone-captured videos. Unlike the traditional avatar method, which requires a studio-level multi-view capture system and reconstructs a human-specific model through a long-time optimization process, we rethink the task through the lenses of model representation, network design, and data preparation. First, we introduce a UV-guided avatar modeling strategy, in which each input image is associated with a pixel-wise facial correspondence estimation. Such correspondence estimation allows us to reproject each valid pixel color from screen space to UV space, which is independent of camera pose and character expression. Furthermore, we design learnable UV tokens on which the attention mechanism can be applied at both the screen and UV levels. The learned UV tokens can be decoded into canonical Gaussian attributes using aggregated UV information from all input views. To train our large avatar model, we additionally prepare a large-scale, identity-rich synthetic training dataset. Our method significantly outperforms existing approaches in both monocular and multi-view settings. Project page: https://zijian-wu.github.io/uika-page/

