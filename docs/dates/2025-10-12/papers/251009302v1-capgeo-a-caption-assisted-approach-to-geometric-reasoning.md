---
layout: default
title: CapGeo: A Caption-Assisted Approach to Geometric Reasoning
---

# CapGeo: A Caption-Assisted Approach to Geometric Reasoning
**arXiv**：[2510.09302v1](https://arxiv.org/abs/2510.09302) · [PDF](https://arxiv.org/pdf/2510.09302.pdf)  
**作者**：Yuying Li, Siyi Qian, Hao Liang, Leqi Zheng, Ruichuan An, Yongzhen Guo, Wentao Zhang  
**一句话要点**：提出CapGeo框架，通过字幕辅助解决多模态大语言模型的几何推理瓶颈
**关键词**：几何推理, 多模态大语言模型, 字幕辅助, CapGeo框架, CapGeo-Bench数据集, 关键点评估指标

## 3 点简述
- 核心问题：多模态大语言模型在几何推理中视觉理解不足，导致性能瓶颈
- 方法要点：将几何图转换为文本字幕，桥接视觉与文本模态以提升推理能力
- 实验或效果：Qwen2.5-VL-72B准确率从8.6%提升至59.0%，显著改进模型性能

## 摘要（原文）

> Geometric reasoning remains a core challenge for Multimodal Large Language
> Models (MLLMs). Even the most advanced closed-source systems, such as GPT-O3
> and Gemini-2.5-Pro, still struggle to solve geometry problems reliably, despite
> exhibiting strong textual reasoning abilities on tasks like the International
> Mathematical Olympiad (IMO). This gap suggests that the bottleneck lies in
> understanding geometric diagrams rather than reasoning itself. Since geometric
> figures can often be faithfully described in concise textual form, converting
> visual content into captions offers a promising direction. Motivated by this
> insight, we introduce CapGeo, a caption-assisted reasoning framework that
> bridges visual and textual modalities. Experiments show substantial
> improvements when models are equipped with captions: Qwen2.5-VL-72B improves
> from 8.6% (vision-only) to 59.0%, while Claude-Opus-4 rises from 44.8% to
> 73.0%. To systematically evaluate and identify high-quality geometric
> captioning models, we further propose CapGeo-Bench, a dataset of 4,641 curated
> figure-caption pairs. Crucially, CapGeo-Bench incorporates a keypoint-based
> evaluation metric that correlates strongly with downstream CapGeo performance,
> enabling reliable assessment of geometric captioning ability. Together, our
> framework and benchmark highlight a new pathway toward advancing geometric
> reasoning in MLLMs.

