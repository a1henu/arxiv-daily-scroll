---
layout: default
title: VC4VG: Optimizing Video Captions for Text-to-Video Generation
---

# VC4VG: Optimizing Video Captions for Text-to-Video Generation
**arXiv**：[2510.24134v1](https://arxiv.org/abs/2510.24134) · [PDF](https://arxiv.org/pdf/2510.24134.pdf)  
**作者**：Yang Du, Zhuoran Lin, Kaiqiang Song, Biao Wang, Zhicheng Zheng, Tiezheng Ge, Bo Zheng, Qin Jin  

**一句话要点**：提出VC4VG框架优化视频字幕以提升文本到视频生成性能

**关键词**：文本到视频生成, 视频字幕优化, 基准构建, 多维度评估, 字幕设计方法

## 3 点简述
- 核心问题：文本到视频生成中高质量视频-文本对优化策略不足。
- 方法要点：设计多维度字幕分解与优化方法，构建VC4VG-Bench基准。
- 实验或效果：微调实验显示字幕质量与视频生成性能强相关。

## 摘要（原文）

> Recent advances in text-to-video (T2V) generation highlight the critical role
> of high-quality video-text pairs in training models capable of producing
> coherent and instruction-aligned videos. However, strategies for optimizing
> video captions specifically for T2V training remain underexplored. In this
> paper, we introduce VC4VG (Video Captioning for Video Generation), a
> comprehensive caption optimization framework tailored to the needs of T2V
> models.We begin by analyzing caption content from a T2V perspective,
> decomposing the essential elements required for video reconstruction into
> multiple dimensions, and proposing a principled caption design methodology. To
> support evaluation, we construct VC4VG-Bench, a new benchmark featuring
> fine-grained, multi-dimensional, and necessity-graded metrics aligned with
> T2V-specific requirements.Extensive T2V fine-tuning experiments demonstrate a
> strong correlation between improved caption quality and video generation
> performance, validating the effectiveness of our approach. We release all
> benchmark tools and code at https://github.com/qyr0403/VC4VG to support further
> research.

