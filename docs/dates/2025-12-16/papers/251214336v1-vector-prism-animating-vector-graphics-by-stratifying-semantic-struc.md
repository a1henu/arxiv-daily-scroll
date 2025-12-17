---
layout: default
title: Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure
---

# Vector Prism: Animating Vector Graphics by Stratifying Semantic Structure
**arXiv**：[2512.14336v1](https://arxiv.org/abs/2512.14336) · [PDF](https://arxiv.org/pdf/2512.14336.pdf)  
**作者**：Jooyeol Yun, Jaegul Choo  

**一句话要点**：提出Vector Prism框架，通过语义结构分层解决SVG动画自动化中的视觉语言模型误处理问题。

**关键词**：矢量图形动画, 语义结构恢复, 视觉语言模型, SVG处理, 弱预测聚合

## 3 点简述
- 核心问题：SVG中视觉连贯部分常被分割为低层级形状，导致视觉语言模型难以识别应一起移动的元素。
- 方法要点：通过统计聚合多个弱部分预测，稳定推断语义，将SVG重组为语义组。
- 实验或效果：相比现有方法，显著提升动画连贯性，支持视觉语言模型与矢量图形更可解释的交互。

## 摘要（原文）

> Scalable Vector Graphics (SVG) are central to modern web design, and the demand to animate them continues to grow as web environments become increasingly dynamic. Yet automating the animation of vector graphics remains challenging for vision-language models (VLMs) despite recent progress in code generation and motion planning. VLMs routinely mis-handle SVGs, since visually coherent parts are often fragmented into low-level shapes that offer little guidance of which elements should move together. In this paper, we introduce a framework that recovers the semantic structure required for reliable SVG animation and reveals the missing layer that current VLM systems overlook. This is achieved through a statistical aggregation of multiple weak part predictions, allowing the system to stably infer semantics from noisy predictions. By reorganizing SVGs into semantic groups, our approach enables VLMs to produce animations with far greater coherence. Our experiments demonstrate substantial gains over existing approaches, suggesting that semantic recovery is the key step that unlocks robust SVG animation and supports more interpretable interactions between VLMs and vector graphics.

