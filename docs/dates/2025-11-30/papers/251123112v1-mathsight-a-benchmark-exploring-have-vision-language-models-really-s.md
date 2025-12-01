---
layout: default
title: MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?
---

# MathSight: A Benchmark Exploring Have Vision-Language Models Really Seen in University-Level Mathematical Reasoning?
**arXiv**：[2511.23112v1](https://arxiv.org/abs/2511.23112) · [PDF](https://arxiv.org/pdf/2511.23112.pdf)  
**作者**：Yuandong Wang, Yao Cui, Yuxin Zhao, Zhen Yang, Yangfu Zhu, Zhenzhou Shao  

**一句话要点**：提出MathSight基准以量化视觉语言模型在大学数学推理中视觉输入的真实贡献

**关键词**：视觉语言模型, 数学推理基准, 多模态评估, 视觉贡献量化, 大学级数学

## 3 点简述
- 核心问题：现有基准未分离视觉模态作用，视觉信息贡献度不明确
- 方法要点：设计多视觉变体（原始、手绘、照片）和纯文本条件进行控制比较
- 实验或效果：实验显示视觉贡献随问题难度增加而减少，Qwen3-VL无图像输入超越多模态变体

## 摘要（原文）

> Recent advances in Vision-Language Models (VLMs) have achieved impressive progress in multimodal mathematical reasoning. Yet, how much visual information truly contributes to reasoning remains unclear. Existing benchmarks report strong overall performance but seldom isolate the role of the image modality, leaving open whether VLMs genuinely leverage visual understanding or merely depend on linguistic priors. To address this, we present MathSight, a university-level multimodal mathematical reasoning benchmark designed to disentangle and quantify the effect of visual input. Each problem includes multiple visual variants -- original, hand-drawn, photo-captured -- and a text-only condition for controlled comparison. Experiments on state-of-the-art VLMs reveal a consistent trend: the contribution of visual information diminishes with increasing problem difficulty. Remarkably, Qwen3-VL without any image input surpasses both its multimodal variants and GPT-5, underscoring the need for benchmarks like MathSight to advance genuine vision-grounded reasoning in future models.

