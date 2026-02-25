---
layout: default
title: TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering
---

# TextPecker: Rewarding Structural Anomaly Quantification for Enhancing Visual Text Rendering
**arXiv**：[2602.20903v1](https://arxiv.org/abs/2602.20903) · [PDF](https://arxiv.org/pdf/2602.20903.pdf)  
**作者**：Hanshen Zhu, Yuliang Liu, Xuecheng Wu, An-Lan Wang, Hao Feng, Dingkang Yang, Chao Feng, Can Huang, Jingqun Tang, Xiang Bai  

**一句话要点**：提出TextPecker以解决视觉文本渲染中的结构异常感知与优化问题

**关键词**：视觉文本渲染, 结构异常感知, 强化学习优化, 文本到图像生成, 字符级标注, 笔画编辑合成

## 3 点简述
- 核心问题：现有模型难以感知文本结构异常，如扭曲、模糊，阻碍评估与优化
- 方法要点：构建字符级结构异常数据集，开发笔画编辑合成引擎，设计即插即用强化学习策略
- 实验或效果：在多种文本到图像模型中提升结构保真度与语义对齐，例如在Qwen-Image上中文渲染平均增益4%和8.7%

## 摘要（原文）

> Visual Text Rendering (VTR) remains a critical challenge in text-to-image generation, where even advanced models frequently produce text with structural anomalies such as distortion, blurriness, and misalignment. However, we find that leading MLLMs and specialist OCR models largely fail to perceive these structural anomalies, creating a critical bottleneck for both VTR evaluation and RL-based optimization. As a result, even state-of-the-art generators (e.g., SeedDream4.0, Qwen-Image) still struggle to render structurally faithful text. To address this, we propose TextPecker, a plug-and-play structural anomaly perceptive RL strategy that mitigates noisy reward signals and works with any textto-image generator. To enable this capability, we construct a recognition dataset with character-level structural-anomaly annotations and develop a stroke-editing synthesis engine to expand structural-error coverage. Experiments show that TextPecker consistently improves diverse text-to-image models; even on the well-optimized Qwen-Image, it significantly yields average gains of 4% in structural fidelity and 8.7% in semantic alignment for Chinese text rendering, establishing a new state-of-the-art in high-fidelity VTR. Our work fills a gap in VTR optimization, providing a foundational step towards reliable and structural faithful visual text generation.

