---
layout: default
title: Venus: Benchmarking and Empowering Multimodal Large Language Models for Aesthetic Guidance and Cropping
---

# Venus: Benchmarking and Empowering Multimodal Large Language Models for Aesthetic Guidance and Cropping
**arXiv**：[2602.23980v1](https://arxiv.org/abs/2602.23980) · [PDF](https://arxiv.org/pdf/2602.23980.pdf)  
**作者**：Tianxiang Du, Hulingxiao He, Yuxin Peng  

**一句话要点**：提出Venus框架以增强多模态大语言模型的美学指导与裁剪能力

**关键词**：美学指导, 多模态大语言模型, 美学裁剪, 数据集构建, 两阶段框架, CoT推理

## 3 点简述
- 核心问题：现有MLLMs在美学指导上反馈过于正面，无法识别问题或提供可操作建议
- 方法要点：引入AesGuide数据集，并设计两阶段框架通过渐进式问题和CoT推理提升能力
- 实验或效果：Venus显著改善美学指导，并在美学裁剪任务中达到SOTA性能

## 摘要（原文）

> The widespread use of smartphones has made photography ubiquitous, yet a clear gap remains between ordinary users and professional photographers, who can identify aesthetic issues and provide actionable shooting guidance during capture. We define this capability as aesthetic guidance (AG) -- an essential but largely underexplored domain in computational aesthetics. Existing multimodal large language models (MLLMs) primarily offer overly positive feedback, failing to identify issues or provide actionable guidance. Without AG capability, they cannot effectively identify distracting regions or optimize compositional balance, thus also struggling in aesthetic cropping, which aims to refine photo composition through reframing after capture. To address this, we introduce AesGuide, the first large-scale AG dataset and benchmark with 10,748 photos annotated with aesthetic scores, analyses, and guidance. Building upon it, we propose Venus, a two-stage framework that first empowers MLLMs with AG capability through progressively complex aesthetic questions and then activates their aesthetic cropping power via CoT-based rationales. Extensive experiments show that Venus substantially improves AG capability and achieves state-of-the-art (SOTA) performance in aesthetic cropping, enabling interpretable and interactive aesthetic refinement across both stages of photo creation. Code is available at https://github.com/PKU-ICST-MIPL/Venus_CVPR2026.

