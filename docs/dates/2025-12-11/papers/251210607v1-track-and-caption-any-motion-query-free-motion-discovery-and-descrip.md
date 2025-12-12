---
layout: default
title: Track and Caption Any Motion: Query-Free Motion Discovery and Description in Videos
---

# Track and Caption Any Motion: Query-Free Motion Discovery and Description in Videos
**arXiv**：[2512.10607v1](https://arxiv.org/abs/2512.10607) · [PDF](https://arxiv.org/pdf/2512.10607.pdf)  
**作者**：Bishoy Galoaa, Sarah Ostadabbas  

**一句话要点**：提出TCAM框架以无查询方式发现和描述视频中的运动模式，适用于遮挡、伪装等挑战场景。

**关键词**：视频理解, 运动模式发现, 视觉-语言对齐, 空间定位, 无查询学习

## 3 点简述
- 核心问题：视频理解在遮挡、伪装或快速运动条件下依赖运动动态而非静态外观，需自动发现和描述运动模式。
- 方法要点：通过运动场注意力机制对齐运动模式与对比视觉-语言表示，结合全局视频-文本对齐和细粒度空间对应进行统一训练。
- 实验或效果：在MeViS基准上，TCAM实现58.4%视频到文本检索、64.9 JF空间定位，每视频发现4.8个相关表达，精度84.7%。

## 摘要（原文）

> We propose Track and Caption Any Motion (TCAM), a motion-centric framework for automatic video understanding that discovers and describes motion patterns without user queries. Understanding videos in challenging conditions like occlusion, camouflage, or rapid movement often depends more on motion dynamics than static appearance. TCAM autonomously observes a video, identifies multiple motion activities, and spatially grounds each natural language description to its corresponding trajectory through a motion-field attention mechanism. Our key insight is that motion patterns, when aligned with contrastive vision-language representations, provide powerful semantic signals for recognizing and describing actions. Through unified training that combines global video-text alignment with fine-grained spatial correspondence, TCAM enables query-free discovery of multiple motion expressions via multi-head cross-attention. On the MeViS benchmark, TCAM achieves 58.4% video-to-text retrieval, 64.9 JF for spatial grounding, and discovers 4.8 relevant expressions per video with 84.7% precision, demonstrating strong cross-task generalization.

