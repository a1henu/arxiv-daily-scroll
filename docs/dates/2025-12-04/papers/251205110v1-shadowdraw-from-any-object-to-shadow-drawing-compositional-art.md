---
layout: default
title: ShadowDraw: From Any Object to Shadow-Drawing Compositional Art
---

# ShadowDraw: From Any Object to Shadow-Drawing Compositional Art
**arXiv**：[2512.05110v1](https://arxiv.org/abs/2512.05110) · [PDF](https://arxiv.org/pdf/2512.05110.pdf)  
**作者**：Rundong Luo, Noah Snavely, Wei-Chiu Ma  

**一句话要点**：提出ShadowDraw框架，将3D对象转化为阴影绘画组合艺术

**关键词**：阴影绘画, 3D对象转换, 场景参数优化, 线稿生成, 计算视觉艺术

## 3 点简述
- 核心问题：如何从3D对象生成阴影绘画，使阴影补全线稿成可识别图像
- 方法要点：优化场景参数预测，用阴影笔画引导线稿生成，自动评估阴影绘画一致性
- 实验或效果：在真实扫描、数据集和生成资产上验证，支持多对象场景和动画

## 摘要（原文）

> We introduce ShadowDraw, a framework that transforms ordinary 3D objects into shadow-drawing compositional art. Given a 3D object, our system predicts scene parameters, including object pose and lighting, together with a partial line drawing, such that the cast shadow completes the drawing into a recognizable image. To this end, we optimize scene configurations to reveal meaningful shadows, employ shadow strokes to guide line drawing generation, and adopt automatic evaluation to enforce shadow-drawing coherence and visual quality. Experiments show that ShadowDraw produces compelling results across diverse inputs, from real-world scans and curated datasets to generative assets, and naturally extends to multi-object scenes, animations, and physical deployments. Our work provides a practical pipeline for creating shadow-drawing art and broadens the design space of computational visual art, bridging the gap between algorithmic design and artistic storytelling. Check out our project page https://red-fairy.github.io/ShadowDraw/ for more results and an end-to-end real-world demonstration of our pipeline!

