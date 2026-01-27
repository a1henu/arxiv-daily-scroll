---
layout: default
title: DisasterInsight: A Multimodal Benchmark for Function-Aware and Grounded Disaster Assessment
---

# DisasterInsight: A Multimodal Benchmark for Function-Aware and Grounded Disaster Assessment
**arXiv**：[2601.18493v1](https://arxiv.org/abs/2601.18493) · [PDF](https://arxiv.org/pdf/2601.18493.pdf)  
**作者**：Sara Tehrani, Yonghao Xu, Leif Haglund, Amanda Berg, Michael Felsberg  

**一句话要点**：提出DisasterInsight基准以评估灾难分析中的视觉语言模型功能理解与指令鲁棒性

**关键词**：灾难评估, 视觉语言模型, 遥感图像, 指令微调, 多模态基准

## 3 点简述
- 现有遥感基准忽视功能理解和指令鲁棒性，限制灾难响应应用
- 基于xBD数据集构建约112K实例，支持建筑功能分类、损伤评估等多任务评估
- 提出DI-Chat模型，通过LoRA微调在损伤分类和报告生成上显著提升性能

## 摘要（原文）

> Timely interpretation of satellite imagery is critical for disaster response, yet existing vision-language benchmarks for remote sensing largely focus on coarse labels and image-level recognition, overlooking the functional understanding and instruction robustness required in real humanitarian workflows. We introduce DisasterInsight, a multimodal benchmark designed to evaluate vision-language models (VLMs) on realistic disaster analysis tasks. DisasterInsight restructures the xBD dataset into approximately 112K building-centered instances and supports instruction-diverse evaluation across multiple tasks, including building-function classification, damage-level and disaster-type classification, counting, and structured report generation aligned with humanitarian assessment guidelines.
>   To establish domain-adapted baselines, we propose DI-Chat, obtained by fine-tuning existing VLM backbones on disaster-specific instruction data using parameter-efficient Low-Rank Adaptation (LoRA). Extensive experiments on state-of-the-art generic and remote-sensing VLMs reveal substantial performance gaps across tasks, particularly in damage understanding and structured report generation. DI-Chat achieves significant improvements on damage-level and disaster-type classification as well as report generation quality, while building-function classification remains challenging for all evaluated models. DisasterInsight provides a unified benchmark for studying grounded multimodal reasoning in disaster imagery.

