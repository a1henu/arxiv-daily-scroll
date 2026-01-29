---
layout: default
title: DeepSeek-OCR 2: Visual Causal Flow
---

# DeepSeek-OCR 2: Visual Causal Flow
**arXiv**：[2601.20552v1](https://arxiv.org/abs/2601.20552) · [PDF](https://arxiv.org/pdf/2601.20552.pdf)  
**作者**：Haoran Wei, Yaofeng Sun, Yukun Li  

**一句话要点**：提出DeepSeek-OCR 2，通过动态重排视觉令牌以改进复杂布局图像理解。

**关键词**：视觉语言模型, 因果推理, 动态令牌重排, 图像语义理解, 编码器设计

## 3 点简述
- 核心问题：传统视觉语言模型处理视觉令牌时采用固定扫描顺序，与人类灵活语义感知不符。
- 方法要点：设计DeepEncoder V2，赋予编码器因果推理能力，实现基于语义的动态令牌重排。
- 实验或效果：探索通过级联1D因果推理结构实现2D图像理解，代码和模型权重已公开。

## 摘要（原文）

> We present DeepSeek-OCR 2 to investigate the feasibility of a novel encoder-DeepEncoder V2-capable of dynamically reordering visual tokens upon image semantics. Conventional vision-language models (VLMs) invariably process visual tokens in a rigid raster-scan order (top-left to bottom-right) with fixed positional encoding when fed into LLMs. However, this contradicts human visual perception, which follows flexible yet semantically coherent scanning patterns driven by inherent logical structures. Particularly for images with complex layouts, human vision exhibits causally-informed sequential processing. Inspired by this cognitive mechanism, DeepEncoder V2 is designed to endow the encoder with causal reasoning capabilities, enabling it to intelligently reorder visual tokens prior to LLM-based content interpretation. This work explores a novel paradigm: whether 2D image understanding can be effectively achieved through two-cascaded 1D causal reasoning structures, thereby offering a new architectural approach with the potential to achieve genuine 2D reasoning. Codes and model weights are publicly accessible at http://github.com/deepseek-ai/DeepSeek-OCR-2.

