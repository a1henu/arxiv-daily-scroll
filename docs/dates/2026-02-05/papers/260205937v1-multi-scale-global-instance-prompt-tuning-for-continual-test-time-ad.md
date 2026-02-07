---
layout: default
title: Multi-Scale Global-Instance Prompt Tuning for Continual Test-time Adaptation in Medical Image Segmentation
---

# Multi-Scale Global-Instance Prompt Tuning for Continual Test-time Adaptation in Medical Image Segmentation
**arXiv**：[2602.05937v1](https://arxiv.org/abs/2602.05937) · [PDF](https://arxiv.org/pdf/2602.05937.pdf)  
**作者**：Lingrui Li, Yanfeng Zhou, Nan Pu, Xin Chen, Zhun Zhong  

**一句话要点**：提出多尺度全局-实例提示调优方法，以增强医学图像分割中的持续测试时适应能力。

**关键词**：持续测试时适应, 医学图像分割, 提示调优, 多尺度学习, 全局-实例知识集成

## 3 点简述
- 核心问题：医学图像分布偏移导致预训练模型在多域部署中性能下降，现有持续测试时适应方法易受错误累积和灾难性遗忘影响。
- 方法要点：设计自适应尺度实例提示和多尺度全局级提示，通过加权集成捕获全局与实例级知识，提升适应鲁棒性。
- 实验或效果：在医学图像分割基准测试中优于现有方法，实现持续变化目标域的稳健适应。

## 摘要（原文）

> Distribution shift is a common challenge in medical images obtained from different clinical centers, significantly hindering the deployment of pre-trained semantic segmentation models in real-world applications across multiple domains. Continual Test-Time Adaptation(CTTA) has emerged as a promising approach to address cross-domain shifts during continually evolving target domains. Most existing CTTA methods rely on incrementally updating model parameters, which inevitably suffer from error accumulation and catastrophic forgetting, especially in long-term adaptation. Recent prompt-tuning-based works have shown potential to mitigate the two issues above by updating only visual prompts. While these approaches have demonstrated promising performance, several limitations remain:1)lacking multi-scale prompt diversity, 2)inadequate incorporation of instance-specific knowledge, and 3)risk of privacy leakage. To overcome these limitations, we propose Multi-scale Global-Instance Prompt Tuning(MGIPT), to enhance scale diversity of prompts and capture both global- and instance-level knowledge for robust CTTA. Specifically, MGIPT consists of an Adaptive-scale Instance Prompt(AIP) and a Multi-scale Global-level Prompt(MGP). AIP dynamically learns lightweight and instance-specific prompts to mitigate error accumulation with adaptive optimal-scale selection mechanism. MGP captures domain-level knowledge across different scales to ensure robust adaptation with anti-forgetting capabilities. These complementary components are combined through a weighted ensemble approach, enabling effective dual-level adaptation that integrates both global and local information. Extensive experiments on medical image segmentation benchmarks demonstrate that our MGIPT outperforms state-of-the-art methods, achieving robust adaptation across continually changing target domains.

