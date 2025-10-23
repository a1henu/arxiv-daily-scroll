---
layout: default
title: CARES: Context-Aware Resolution Selector for VLMs
---

# CARES: Context-Aware Resolution Selector for VLMs
**arXiv**：[2510.19496v1](https://arxiv.org/abs/2510.19496) · [PDF](https://arxiv.org/pdf/2510.19496.pdf)  
**作者**：Moshe Kimhi, Nimrod Shabtay, Raja Giryes, Chaim Baskin, Eli Schwartz  

**一句话要点**：提出CARES模块以动态选择图像分辨率，降低视觉语言模型计算开销。

**关键词**：视觉语言模型, 分辨率选择, 计算优化, 轻量预处理, 多模态基准

## 3 点简述
- 视觉语言模型常处理高分辨率图像，导致视觉令牌占比高，增加计算和延迟。
- CARES使用轻量VLM预测最小足够分辨率，训练为离散分类器，推理时支持连续插值。
- 在多个基准测试中，CARES保持任务性能，计算量减少高达80%。

## 摘要（原文）

> Large vision-language models (VLMs) commonly process images at native or high
> resolution to remain effective across tasks. This inflates visual tokens ofter
> to 97-99% of total tokens, resulting in high compute and latency, even when
> low-resolution images would suffice. We introduce \emph{CARES}-a
> \textbf{C}ontext-\textbf{A}ware \textbf{R}esolution \textbf{S}elector, a
> lightweight preprocessing module that, given an image-query pair, predicts the
> \emph{minimal} sufficient input resolution. CARES uses a compact VLM (350M) to
> extract features and predict when a target pretrained VLM's response converges
> to its peak ability to answer correctly. Though trained as a discrete
> classifier over a set of optional resolutions, CARES interpolates continuous
> resolutions at inference for fine-grained control. Across five multimodal
> benchmarks spanning documents and natural images, as well as diverse target
> VLMs, CARES preserves task performance while reducing compute by up to 80%.

