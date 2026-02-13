---
layout: default
title: SAM3-LiteText: An Anatomical Study of the SAM3 Text Encoder for Efficient Vision-Language Segmentation
---

# SAM3-LiteText: An Anatomical Study of the SAM3 Text Encoder for Efficient Vision-Language Segmentation
**arXiv**：[2602.12173v1](https://arxiv.org/abs/2602.12173) · [PDF](https://arxiv.org/pdf/2602.12173.pdf)  
**作者**：Chengxi Zeng, Yuxuan Jiang, Ge Gao, Shuai Wang, Duolikun Danier, Bin Zhu, Stevan Rudinac, David Bull, Fan Zhang  

**一句话要点**：提出SAM3-LiteText，通过轻量文本编码器解决视觉语言分割中文本编码冗余问题

**关键词**：视觉语言分割, 文本编码优化, 知识蒸馏, 轻量模型, 冗余分析

## 3 点简述
- 分析视觉语言分割中文本提示的冗余性，发现上下文窗口利用不足和词汇稀疏
- 设计轻量文本编码框架，用MobileCLIP学生模型通过知识蒸馏替换原SAM3文本编码器
- 实验显示参数减少达88%，保持分割性能，降低内存开销

## 摘要（原文）

> Vision-language segmentation models such as SAM3 enable flexible, prompt-driven visual grounding, but inherit large, general-purpose text encoders originally designed for open-ended language understanding. In practice, segmentation prompts are short, structured, and semantically constrained, leading to substantial over-provisioning in text encoder capacity and persistent computational and memory overhead. In this paper, we perform a large-scale anatomical analysis of text prompting in vision-language segmentation, covering 404,796 real prompts across multiple benchmarks. Our analysis reveals severe redundancy: most context windows are underutilized, vocabulary usage is highly sparse, and text embeddings lie on low-dimensional manifold despite high-dimensional representations. Motivated by these findings, we propose SAM3-LiteText, a lightweight text encoding framework that replaces the original SAM3 text encoder with a compact MobileCLIP student that is optimized by knowledge distillation. Extensive experiments on image and video segmentation benchmarks show that SAM3-LiteText reduces text encoder parameters by up to 88%, substantially reducing static memory footprint, while maintaining segmentation performance comparable to the original model. Code: https://github.com/SimonZeng7108/efficientsam3/tree/sam3_litetext.

