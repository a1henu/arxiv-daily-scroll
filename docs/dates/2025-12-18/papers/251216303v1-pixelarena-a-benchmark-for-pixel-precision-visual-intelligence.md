---
layout: default
title: PixelArena: A benchmark for Pixel-Precision Visual Intelligence
---

# PixelArena: A benchmark for Pixel-Precision Visual Intelligence
**arXiv**：[2512.16303v1](https://arxiv.org/abs/2512.16303) · [PDF](https://arxiv.org/pdf/2512.16303.pdf)  
**作者**：Feng Liang, Sizhe Cheng, Chenqi Yi  

**一句话要点**：提出PixelArena基准，通过语义分割任务评估多模态大模型的像素级生成能力。

**关键词**：像素级视觉智能, 语义分割基准, 多模态大模型, 图像生成评估, 零样本生成

## 3 点简述
- 核心问题：现有图像生成基准多关注美学，缺乏对细粒度生成能力的客观评估。
- 方法要点：利用语义分割任务，以像素精度检验多模态大模型的生成智能。
- 实验或效果：发现Gemini 3 Pro Image在零样本设置下能高保真生成语义掩码，展现新能力。

## 摘要（原文）

> Multi-modal large language models that have image output are emerging. Many image generation benchmarks focus on aesthetics instead of fine-grained generation capabilities. In PixelArena, we propose using semantic segmentation tasks to objectively examine their fine-grained generative intelligence with pixel precision. We find the latest Gemini 3 Pro Image has emergent image generation capabilities that generate semantic masks with high fidelity under zero-shot settings, showcasing visual intelligence unseen before and true generalization in new image generation tasks. We further investigate its results, compare them qualitatively and quantitatively with those of other models, and present failure cases. The findings not only signal exciting progress in the field but also provide insights into future research related to multimodality, reasoning, interpretability and benchmarking.

