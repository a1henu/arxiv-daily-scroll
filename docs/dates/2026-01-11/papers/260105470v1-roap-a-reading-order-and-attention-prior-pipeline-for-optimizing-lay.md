---
layout: default
title: ROAP: A Reading-Order and Attention-Prior Pipeline for Optimizing Layout Transformers in Key Information Extraction
---

# ROAP: A Reading-Order and Attention-Prior Pipeline for Optimizing Layout Transformers in Key Information Extraction
**arXiv**：[2601.05470v1](https://arxiv.org/abs/2601.05470) · [PDF](https://arxiv.org/pdf/2601.05470.pdf)  
**作者**：Tingwei Xie, Jinxin He, Yonghong Song  

**一句话要点**：提出ROAP管道以优化布局Transformer在关键信息提取中的注意力分布

**关键词**：关键信息提取, 布局Transformer, 阅读顺序建模, 注意力优化, 视觉丰富文档理解, 多模态干扰抑制

## 3 点简述
- 核心问题：多模态Transformer在视觉丰富文档理解中缺乏显式阅读顺序建模和视觉噪声干扰文本语义注意力
- 方法要点：通过AXG-Tree提取阅读序列，结合RO-RPB和TT-Prior优化注意力机制，不改变预训练骨干
- 实验或效果：在FUNSD和CORD基准上提升LayoutLMv3和GeoLayoutLM性能，证实阅读逻辑建模和模态干扰调节的重要性

## 摘要（原文）

> The efficacy of Multimodal Transformers in visually-rich document understanding (VrDU) is critically constrained by two inherent limitations: the lack of explicit modeling for logical reading order and the interference of visual tokens that dilutes attention on textual semantics.
>   To address these challenges, this paper presents ROAP, a lightweight and architecture-agnostic pipeline designed to optimize attention distributions in Layout Transformers without altering their pre-trained backbones.
>   The proposed pipeline first employs an Adaptive-XY-Gap (AXG-Tree) to robustly extract hierarchical reading sequences from complex layouts. These sequences are then integrated into the attention mechanism via a Reading-Order-Aware Relative Position Bias (RO-RPB). Furthermore, a Textual-Token Sub-block Attention Prior (TT-Prior) is introduced to adaptively suppress visual noise and enhance fine-grained text-text interactions.
>   Extensive experiments on the FUNSD and CORD benchmarks demonstrate that ROAP consistently improves the performance of representative backbones, including LayoutLMv3 and GeoLayoutLM.
>   These findings confirm that explicitly modeling reading logic and regulating modality interference are critical for robust document understanding, offering a scalable solution for complex layout analysis. The implementation code will be released at https://github.com/KevinYuLei/ROAP.

