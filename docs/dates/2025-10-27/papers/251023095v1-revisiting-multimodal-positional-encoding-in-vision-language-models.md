---
layout: default
title: Revisiting Multimodal Positional Encoding in Vision-Language Models
---

# Revisiting Multimodal Positional Encoding in Vision-Language Models
**arXiv**：[2510.23095v1](https://arxiv.org/abs/2510.23095) · [PDF](https://arxiv.org/pdf/2510.23095.pdf)  
**作者**：Jie Huang, Xuejing Liu, Sibo Song, Ruibing Hou, Hong Chang, Junyang Lin, Shuai Bai  

**一句话要点**：提出MHRoPE和MRoPE-I以改进视觉语言模型中的多模态位置编码

**关键词**：多模态位置编码, 旋转位置嵌入, 视觉语言模型, 即插即用方法, 多模态理解

## 3 点简述
- 核心问题：多模态位置编码缺乏系统研究，影响模型布局理解和表示能力
- 方法要点：基于位置设计和频率分配分析，提出无需架构更改的即插即用变体
- 实验或效果：在多个基准测试中显著提升通用和细粒度多模态理解性能

## 摘要（原文）

> Multimodal position encoding is essential for vision-language models, yet
> there has been little systematic investigation into multimodal position
> encoding. We conduct a comprehensive analysis of multimodal Rotary Positional
> Embedding (RoPE) by examining its two core components: position design and
> frequency allocation. Through extensive experiments, we identify three key
> guidelines: positional coherence, full frequency utilization, and preservation
> of textual priors-ensuring unambiguous layout, rich representation, and
> faithful transfer from the pre-trained LLM. Based on these insights, we propose
> Multi-Head RoPE (MHRoPE) and MRoPE-Interleave (MRoPE-I), two simple and
> plug-and-play variants that require no architectural changes. Our methods
> consistently outperform existing approaches across diverse benchmarks, with
> significant improvements in both general and fine-grained multimodal
> understanding. Code will be avaliable at
> https://github.com/JJJYmmm/Multimodal-RoPEs.

