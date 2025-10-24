---
layout: default
title: Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation
---

# Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation
**arXiv**：[2510.20812v1](https://arxiv.org/abs/2510.20812) · [PDF](https://arxiv.org/pdf/2510.20812.pdf)  
**作者**：Yuhan Liu, Lianhui Qin, Shengjie Wang  

**一句话要点**：提出Speculative Verdict框架以解决信息密集型图像中的视觉推理问题

**关键词**：视觉语言模型, 信息密集型图像, 推理路径合成, 计算效率优化, 无需训练框架, 多专家系统

## 3 点简述
- 核心问题：大型视觉语言模型在密集文本与图形元素交织的图像中推理困难，难以精确定位和整合证据。
- 方法要点：结合多个轻量级草稿专家生成多样化推理路径，由大型裁决模型合成最终答案，无需训练。
- 实验或效果：在InfographicVQA等基准上实现性能提升，兼具错误纠正和计算效率。

## 摘要（原文）

> Large Vision-Language Models (VLMs) have achieved remarkable progress in
> multimodal understanding, yet they struggle when reasoning over
> information-intensive images that densely interleave textual annotations with
> fine-grained graphical elements. The main challenges lie in precisely
> localizing critical cues in dense layouts and multi-hop reasoning to integrate
> dispersed evidence. We propose Speculative Verdict (SV), a training-free
> framework inspired by speculative decoding that combines multiple lightweight
> draft experts with a large verdict model. In the draft stage, small VLMs act as
> draft experts to generate reasoning paths that provide diverse localization
> candidates; in the verdict stage, a strong VLM synthesizes these paths to
> produce the final answer, minimizing computational cost while recovering
> correct answers. To further improve efficiency and accuracy, SV introduces a
> consensus expert selection mechanism that forwards only high-agreement
> reasoning paths to the verdict. Empirically, SV achieves consistent gains on
> challenging information-intensive and high-resolution visual question answering
> benchmarks, including InfographicVQA, ChartMuseum, ChartQAPro, and HR-Bench 4K.
> By synthesizing correct insights from multiple partially accurate reasoning
> paths, SV achieves both error correction and cost-efficiency compared to large
> proprietary models or training pipelines. Code is available at
> https://github.com/Tinaliu0123/speculative-verdict

