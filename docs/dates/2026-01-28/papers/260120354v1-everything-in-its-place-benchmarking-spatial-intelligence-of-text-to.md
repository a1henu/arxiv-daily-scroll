---
layout: default
title: Everything in Its Place: Benchmarking Spatial Intelligence of Text-to-Image Models
---

# Everything in Its Place: Benchmarking Spatial Intelligence of Text-to-Image Models
**arXiv**：[2601.20354v1](https://arxiv.org/abs/2601.20354) · [PDF](https://arxiv.org/pdf/2601.20354.pdf)  
**作者**：Zengbin Wang, Xuecai Hu, Yong Wang, Feng Xiong, Man Zhang, Xiangxiang Chu  

**一句话要点**：提出SpatialGenEval基准以评估文本到图像模型的空间智能，并构建SpatialT2I数据集提升性能。

**关键词**：空间智能评估, 文本到图像模型, 长提示设计, 基准测试, 数据集构建, 微调优化

## 3 点简述
- 当前T2I模型在复杂空间关系处理上存在瓶颈，现有基准因提示设计简短而忽略此问题。
- SpatialGenEval包含1,230个信息密集的长提示，覆盖25个场景和10个空间子域，用于系统评估。
- 基于SpatialT2I数据集微调基础模型，性能提升4.2%至5.7%，空间关系更真实。

## 摘要（原文）

> Text-to-image (T2I) models have achieved remarkable success in generating high-fidelity images, but they often fail in handling complex spatial relationships, e.g., spatial perception, reasoning, or interaction. These critical aspects are largely overlooked by current benchmarks due to their short or information-sparse prompt design. In this paper, we introduce SpatialGenEval, a new benchmark designed to systematically evaluate the spatial intelligence of T2I models, covering two key aspects: (1) SpatialGenEval involves 1,230 long, information-dense prompts across 25 real-world scenes. Each prompt integrates 10 spatial sub-domains and corresponding 10 multi-choice question-answer pairs, ranging from object position and layout to occlusion and causality. Our extensive evaluation of 21 state-of-the-art models reveals that higher-order spatial reasoning remains a primary bottleneck. (2) To demonstrate that the utility of our information-dense design goes beyond simple evaluation, we also construct the SpatialT2I dataset. It contains 15,400 text-image pairs with rewritten prompts to ensure image consistency while preserving information density. Fine-tuned results on current foundation models (i.e., Stable Diffusion-XL, Uniworld-V1, OmniGen2) yield consistent performance gains (+4.2%, +5.7%, +4.4%) and more realistic effects in spatial relations, highlighting a data-centric paradigm to achieve spatial intelligence in T2I models.

