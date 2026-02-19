---
layout: default
title: Visual Self-Refine: A Pixel-Guided Paradigm for Accurate Chart Parsing
---

# Visual Self-Refine: A Pixel-Guided Paradigm for Accurate Chart Parsing
**arXiv**：[2602.16455v1](https://arxiv.org/abs/2602.16455) · [PDF](https://arxiv.org/pdf/2602.16455.pdf)  
**作者**：Jinsong Li, Xiaoyi Dong, Yuhang Zang, Yuhang Cao, Jiaqi Wang, Dahua Lin  

**一句话要点**：提出Visual Self-Refine范式，通过像素级定位反馈提升图表解析准确性

**关键词**：图表解析, 视觉反馈, 像素级定位, 自校正, 视觉语言模型, 基准构建

## 3 点简述
- 现有大视觉语言模型在视觉密集图表解析中易出现数据遗漏、错位和幻觉等问题
- VSR范式让模型生成像素级定位输出，可视化后反馈自检以纠正视觉感知错误
- 在ChartP-Bench基准上验证了ChartVSR模型的有效性，并推广VSR为通用视觉反馈机制

## 摘要（原文）

> While Large Vision-Language Models (LVLMs) have demonstrated remarkable capabilities for reasoning and self-correction at the textual level, these strengths provide minimal benefits for complex tasks centered on visual perception, such as Chart Parsing. Existing models often struggle with visually dense charts, leading to errors like data omission, misalignment, and hallucination. Inspired by the human strategy of using a finger as a ``visual anchor'' to ensure accuracy when reading complex charts, we propose a new paradigm named Visual Self-Refine (VSR). The core idea of VSR is to enable a model to generate pixel-level localization outputs, visualize them, and then feed these visualizations back to itself, allowing it to intuitively inspect and correct its own potential visual perception errors. We instantiate the VSR paradigm in the domain of Chart Parsing by proposing ChartVSR. This model decomposes the parsing process into two stages: a Refine Stage, where it iteratively uses visual feedback to ensure the accuracy of all data points' Pixel-level Localizations, and a Decode Stage, where it uses these verified localizations as precise visual anchors to parse the final structured data. To address the limitations of existing benchmarks, we also construct ChartP-Bench, a new and highly challenging benchmark for chart parsing. Our work also highlights VSR as a general-purpose visual feedback mechanism, offering a promising new direction for enhancing accuracy on a wide range of vision-centric tasks.

