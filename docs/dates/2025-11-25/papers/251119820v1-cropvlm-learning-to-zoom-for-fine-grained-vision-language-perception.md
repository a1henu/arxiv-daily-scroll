---
layout: default
title: CropVLM: Learning to Zoom for Fine-Grained Vision-Language Perception
---

# CropVLM: Learning to Zoom for Fine-Grained Vision-Language Perception
**arXiv**：[2511.19820v1](https://arxiv.org/abs/2511.19820) · [PDF](https://arxiv.org/pdf/2511.19820.pdf)  
**作者**：Miguel Carvalho, Helder Dias, Bruno Martins  

**一句话要点**：提出CropVLM以增强视觉语言模型在细粒度图像理解中的性能

**关键词**：视觉语言模型, 细粒度图像理解, 强化学习, 动态放大, 跨域性能提升, 无监督训练

## 3 点简述
- 视觉语言模型在细粒度图像任务中因感知限制和视觉碎片化而表现不佳
- 使用强化学习训练模型动态放大图像区域，无需人工标注或昂贵合成评估
- 在不修改目标模型下显著提升跨域高分辨率图像理解任务性能

## 摘要（原文）

> Vision-Language Models (VLMs) often struggle with tasks that require fine-grained image understanding, such as scene-text recognition or document analysis, due to perception limitations and visual fragmentation. To address these challenges, we introduce CropVLM as an external low-cost method for boosting performance, enabling VLMs to dynamically ''zoom in'' on relevant image regions, enhancing their ability to capture fine details. CropVLM is trained using reinforcement learning, without using human-labeled bounding boxes as a supervision signal, and without expensive synthetic evaluations. The model is trained once and can be paired with both open-source and proprietary VLMs to improve their performance. Our approach delivers significant improvements on tasks that require high-resolution image understanding, notably for benchmarks that are out-of-domain for the target VLM, without modifying or fine-tuning the VLM, thus avoiding catastrophic forgetting.

