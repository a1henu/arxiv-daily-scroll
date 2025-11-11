---
layout: default
title: Mono3DVG-EnSD: Enhanced Spatial-aware and Dimension-decoupled Text Encoding for Monocular 3D Visual Grounding
---

# Mono3DVG-EnSD: Enhanced Spatial-aware and Dimension-decoupled Text Encoding for Monocular 3D Visual Grounding
**arXiv**：[2511.06908v1](https://arxiv.org/abs/2511.06908) · [PDF](https://arxiv.org/pdf/2511.06908.pdf)  
**作者**：Yuzhen Li, Min Liu, Zhaoyang Li, Yuan Bian, Xueping Wang, Erbo Zhai, Yaonan Wang  

**一句话要点**：提出Mono3DVG-EnSD框架，通过增强空间感知和维度解耦解决单目3D视觉定位中的问题。

**关键词**：单目3D视觉定位, 文本编码增强, 空间感知, 维度解耦, 跨模态交互, CLIP引导

## 3 点简述
- 核心问题：现有方法过度依赖高确定性关键词，忽视空间描述，且文本特征存在跨维度干扰。
- 方法要点：引入CLIP-LCA动态掩码关键词保留空间描述，D2M解耦维度特征以指导视觉特征。
- 实验或效果：在Mono3DRefer数据集上实现SOTA，Far(Acc@0.5)场景提升13.54%。

## 摘要（原文）

> Monocular 3D Visual Grounding (Mono3DVG) is an emerging task that locates 3D
> objects in RGB images using text descriptions with geometric cues. However,
> existing methods face two key limitations. Firstly, they often over-rely on
> high-certainty keywords that explicitly identify the target object while
> neglecting critical spatial descriptions. Secondly, generalized textual
> features contain both 2D and 3D descriptive information, thereby capturing an
> additional dimension of details compared to singular 2D or 3D visual features.
> This characteristic leads to cross-dimensional interference when refining
> visual features under text guidance. To overcome these challenges, we propose
> Mono3DVG-EnSD, a novel framework that integrates two key components: the
> CLIP-Guided Lexical Certainty Adapter (CLIP-LCA) and the Dimension-Decoupled
> Module (D2M). The CLIP-LCA dynamically masks high-certainty keywords while
> retaining low-certainty implicit spatial descriptions, thereby forcing the
> model to develop a deeper understanding of spatial relationships in captions
> for object localization. Meanwhile, the D2M decouples dimension-specific
> (2D/3D) textual features from generalized textual features to guide
> corresponding visual features at same dimension, which mitigates
> cross-dimensional interference by ensuring dimensionally-consistent cross-modal
> interactions. Through comprehensive comparisons and ablation studies on the
> Mono3DRefer dataset, our method achieves state-of-the-art (SOTA) performance
> across all metrics. Notably, it improves the challenging Far(Acc@0.5) scenario
> by a significant +13.54%.

