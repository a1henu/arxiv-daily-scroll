---
layout: default
title: DreamingComics: A Story Visualization Pipeline via Subject and Layout Customized Generation using Video Models
---

# DreamingComics: A Story Visualization Pipeline via Subject and Layout Customized Generation using Video Models
**arXiv**：[2512.01686v1](https://arxiv.org/abs/2512.01686) · [PDF](https://arxiv.org/pdf/2512.01686.pdf)  
**作者**：Patrick Kwon, Chen Chen  

**一句话要点**：提出DreamingComics框架，通过布局定制生成解决故事可视化中主体定位和艺术一致性问题

**关键词**：故事可视化, 视频扩散模型, 布局控制, 位置编码, 一致性增强, 漫画生成

## 3 点简述
- 当前故事可视化方法依赖文本定位主体，难以保持艺术一致性。
- 基于视频扩散Transformer，引入RegionalRoPE编码和掩码条件损失，实现布局控制。
- 集成LLM布局生成器，评估显示角色一致性提升29.2%，风格相似性提升36.2%。

## 摘要（原文）

> Current story visualization methods tend to position subjects solely by text and face challenges in maintaining artistic consistency. To address these limitations, we introduce DreamingComics, a layout-aware story visualization framework. We build upon a pretrained video diffusion-transformer (DiT) model, leveraging its spatiotemporal priors to enhance identity and style consistency. For layout-based position control, we propose RegionalRoPE, a region-aware positional encoding scheme that re-indexes embeddings based on the target layout. Additionally, we introduce a masked condition loss to further constrain each subject's visual features to their designated region. To infer layouts from natural language scripts, we integrate an LLM-based layout generator trained to produce comic-style layouts, enabling flexible and controllable layout conditioning. We present a comprehensive evaluation of our approach, showing a 29.2% increase in character consistency and a 36.2% increase in style similarity compared to previous methods, while displaying high spatial accuracy. Our project page is available at https://yj7082126.github.io/dreamingcomics/

