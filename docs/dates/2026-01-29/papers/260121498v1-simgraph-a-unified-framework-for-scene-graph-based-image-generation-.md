---
layout: default
title: SimGraph: A Unified Framework for Scene Graph-Based Image Generation and Editing
---

# SimGraph: A Unified Framework for Scene Graph-Based Image Generation and Editing
**arXiv**：[2601.21498v1](https://arxiv.org/abs/2601.21498) · [PDF](https://arxiv.org/pdf/2601.21498.pdf)  
**作者**：Thanh-Nhan Vo, Trong-Thuan Nguyen, Tam V. Nguyen, Minh-Triet Tran  

**一句话要点**：提出SimGraph统一框架，基于场景图实现图像生成与编辑的精确控制

**关键词**：场景图, 图像生成, 图像编辑, 扩散模型, 结构化控制, 空间一致性

## 3 点简述
- 核心问题：现有方法分离图像生成与编辑，导致空间一致性和语义连贯性不足，缺乏对对象关系和布局的结构化控制。
- 方法要点：集成基于令牌的生成和基于扩散的编辑于单一场景图驱动模型，提供对对象交互、布局和空间一致性的精确控制。
- 实验或效果：通过广泛实验，实证显示该方法在图像生成和编辑任务上优于现有最先进方法，确保高质量和一致结果。

## 摘要（原文）

> Recent advancements in Generative Artificial Intelligence (GenAI) have significantly enhanced the capabilities of both image generation and editing. However, current approaches often treat these tasks separately, leading to inefficiencies and challenges in maintaining spatial consistency and semantic coherence between generated content and edits. Moreover, a major obstacle is the lack of structured control over object relationships and spatial arrangements. Scene graph-based methods, which represent objects and their interrelationships in a structured format, offer a solution by providing greater control over composition and interactions in both image generation and editing. To address this, we introduce SimGraph, a unified framework that integrates scene graph-based image generation and editing, enabling precise control over object interactions, layouts, and spatial coherence. In particular, our framework integrates token-based generation and diffusion-based editing within a single scene graph-driven model, ensuring high-quality and consistent results. Through extensive experiments, we empirically demonstrate that our approach outperforms existing state-of-the-art methods.

