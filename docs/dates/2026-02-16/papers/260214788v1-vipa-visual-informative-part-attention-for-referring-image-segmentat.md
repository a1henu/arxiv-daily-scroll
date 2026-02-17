---
layout: default
title: VIPA: Visual Informative Part Attention for Referring Image Segmentation
---

# VIPA: Visual Informative Part Attention for Referring Image Segmentation
**arXiv**：[2602.14788v1](https://arxiv.org/abs/2602.14788) · [PDF](https://arxiv.org/pdf/2602.14788.pdf)  
**作者**：Yubin Cho, Hyunwoo Yu, Kyeongbo Kong, Kyomin Sohn, Bongjoon Hyun, Suk-Ju Kang  

**一句话要点**：提出视觉信息部分注意力框架以提升指称图像分割的细粒度对齐

**关键词**：指称图像分割, 视觉注意力, 跨模态对齐, 细粒度分割, 视觉表达生成

## 3 点简述
- 指称图像分割旨在根据自然语言描述分割目标对象，现有方法常将视觉信息融入语言标记。
- VIPA框架利用视觉表达作为信息部分，通过视觉表达生成器模块减少跨模态投影方差并增强语义一致性。
- 在四个公开基准测试中，VIPA优于现有最先进方法，实验验证了其有效性。

## 摘要（原文）

> Referring Image Segmentation (RIS) aims to segment a target object described by a natural language expression. Existing methods have evolved by leveraging the vision information into the language tokens. To more effectively exploit visual contexts for fine-grained segmentation, we propose a novel Visual Informative Part Attention (VIPA) framework for referring image segmentation. VIPA leverages the informative parts of visual contexts, called a visual expression, which can effectively provide the structural and semantic visual target information to the network. This design reduces high-variance cross-modal projection and enhances semantic consistency in an attention mechanism of the referring image segmentation. We also design a visual expression generator (VEG) module, which retrieves informative visual tokens via local-global linguistic context cues and refines the retrieved tokens for reducing noise information and sharing informative visual attributes. This module allows the visual expression to consider comprehensive contexts and capture semantic visual contexts of informative regions. In this way, our framework enables the network's attention to robustly align with the fine-grained regions of interest. Extensive experiments and visual analysis demonstrate the effectiveness of our approach. Our VIPA outperforms the existing state-of-the-art methods on four public RIS benchmarks.

