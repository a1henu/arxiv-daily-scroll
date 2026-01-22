---
layout: default
title: Enhancing Few-Shot Out-of-Distribution Detection via the Refinement of Foreground and Background
---

# Enhancing Few-Shot Out-of-Distribution Detection via the Refinement of Foreground and Background
**arXiv**：[2601.15065v1](https://arxiv.org/abs/2601.15065) · [PDF](https://arxiv.org/pdf/2601.15065.pdf)  
**作者**：Tianyu Li, Songyue Cai, Zongqian Wu, Ping Hu, Xiaofeng Zhu  

**一句话要点**：提出可插拔框架以优化前景背景分解，提升少样本分布外检测性能

**关键词**：少样本学习, 分布外检测, 前景背景分解, 自适应抑制, 可混淆校正, 可插拔框架

## 3 点简述
- 核心问题：现有前景背景分解方法在背景抑制和前景处理上存在局限性，影响少样本分布外检测效果
- 方法要点：引入自适应背景抑制和可混淆前景校正模块，优化前景背景分解的局部处理
- 实验或效果：实验表明该框架显著提升现有方法的性能，代码已开源

## 摘要（原文）

> CLIP-based foreground-background (FG-BG) decomposition methods have demonstrated remarkable effectiveness in improving few-shot out-of-distribution (OOD) detection performance. However, existing approaches still suffer from several limitations. For background regions obtained from decomposition, existing methods adopt a uniform suppression strategy for all patches, overlooking the varying contributions of different patches to the prediction. For foreground regions, existing methods fail to adequately consider that some local patches may exhibit appearance or semantic similarity to other classes, which may mislead the training process. To address these issues, we propose a new plug-and-play framework. This framework consists of three core components: (1) a Foreground-Background Decomposition module, which follows previous FG-BG methods to separate an image into foreground and background regions; (2) an Adaptive Background Suppression module, which adaptively weights patch classification entropy; and (3) a Confusable Foreground Rectification module, which identifies and rectifies confusable foreground patches. Extensive experimental results demonstrate that the proposed plug-and-play framework significantly improves the performance of existing FG-BG decomposition methods. Code is available at: https://github.com/lounwb/FoBoR.

