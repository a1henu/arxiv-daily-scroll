---
layout: default
title: EditCtrl: Disentangled Local and Global Control for Real-Time Generative Video Editing
---

# EditCtrl: Disentangled Local and Global Control for Real-Time Generative Video Editing
**arXiv**：[2602.15031v1](https://arxiv.org/abs/2602.15031) · [PDF](https://arxiv.org/pdf/2602.15031.pdf)  
**作者**：Yehonathan Litman, Shikun Liu, Dario Seyb, Nicholas Milef, Yang Zhou, Carl Marshall, Shubham Tulsiani, Caleb Leak  

**一句话要点**：提出EditCtrl框架，通过解耦局部与全局控制实现高效实时生成式视频编辑

**关键词**：生成式视频编辑, 视频修复, 局部全局解耦, 计算效率优化, 实时编辑, 多区域编辑

## 3 点简述
- 核心问题：现有视频编辑方法计算成本高，即使局部编辑也需处理全视频上下文，效率低下
- 方法要点：设计局部视频上下文模块仅处理掩码标记，计算成本与编辑大小成正比；轻量级全局上下文嵌入器确保视频一致性
- 实验或效果：EditCtrl计算效率比现有方法高10倍，编辑质量优于全注意力方法，支持多区域编辑和自回归内容传播

## 摘要（原文）

> High-fidelity generative video editing has seen significant quality improvements by leveraging pre-trained video foundation models. However, their computational cost is a major bottleneck, as they are often designed to inefficiently process the full video context regardless of the inpainting mask's size, even for sparse, localized edits. In this paper, we introduce EditCtrl, an efficient video inpainting control framework that focuses computation only where it is needed. Our approach features a novel local video context module that operates solely on masked tokens, yielding a computational cost proportional to the edit size. This local-first generation is then guided by a lightweight temporal global context embedder that ensures video-wide context consistency with minimal overhead. Not only is EditCtrl 10 times more compute efficient than state-of-the-art generative editing methods, it even improves editing quality compared to methods designed with full-attention. Finally, we showcase how EditCtrl unlocks new capabilities, including multi-region editing with text prompts and autoregressive content propagation.

