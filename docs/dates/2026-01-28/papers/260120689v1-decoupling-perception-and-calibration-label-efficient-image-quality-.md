---
layout: default
title: Decoupling Perception and Calibration: Label-Efficient Image Quality Assessment Framework
---

# Decoupling Perception and Calibration: Label-Efficient Image Quality Assessment Framework
**arXiv**：[2601.20689v1](https://arxiv.org/abs/2601.20689) · [PDF](https://arxiv.org/pdf/2601.20689.pdf)  
**作者**：Xinyue Li, Zhichao Zhang, Zhiming Xu, Shubo Xu, Xiongkuo Min, Yitong Chen, Guangtao Zhai  

**一句话要点**：提出LEAF框架以解决多模态大模型在图像质量评估中依赖大量人工标注的问题

**关键词**：图像质量评估, 多模态大模型, 知识蒸馏, 标注效率, 平均意见分数校准, 轻量回归器

## 3 点简述
- 核心问题：多模态大模型在图像质量评估中计算成本高且需大量平均意见分数标注
- 方法要点：通过蒸馏教师模型的感知先验到轻量学生回归器，结合点对和配对监督进行校准
- 实验或效果：在用户生成和AI生成基准上，显著减少标注需求并保持强相关性

## 摘要（原文）

> Recent multimodal large language models (MLLMs) have demonstrated strong capabilities in image quality assessment (IQA) tasks. However, adapting such large-scale models is computationally expensive and still relies on substantial Mean Opinion Score (MOS) annotations. We argue that for MLLM-based IQA, the core bottleneck lies not in the quality perception capacity of MLLMs, but in MOS scale calibration. Therefore, we propose LEAF, a Label-Efficient Image Quality Assessment Framework that distills perceptual quality priors from an MLLM teacher into a lightweight student regressor, enabling MOS calibration with minimal human supervision. Specifically, the teacher conducts dense supervision through point-wise judgments and pair-wise preferences, with an estimate of decision reliability. Guided by these signals, the student learns the teacher's quality perception patterns through joint distillation and is calibrated on a small MOS subset to align with human annotations. Experiments on both user-generated and AI-generated IQA benchmarks demonstrate that our method significantly reduces the need for human annotations while maintaining strong MOS-aligned correlations, making lightweight IQA practical under limited annotation budgets.

