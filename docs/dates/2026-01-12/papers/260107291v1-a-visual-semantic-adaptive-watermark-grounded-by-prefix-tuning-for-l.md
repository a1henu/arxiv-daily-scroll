---
layout: default
title: A Visual Semantic Adaptive Watermark grounded by Prefix-Tuning for Large Vision-Language Model
---

# A Visual Semantic Adaptive Watermark grounded by Prefix-Tuning for Large Vision-Language Model
**arXiv**：[2601.07291v1](https://arxiv.org/abs/2601.07291) · [PDF](https://arxiv.org/pdf/2601.07291.pdf)  
**作者**：Qi Zheng, Shuliang Liu, Yu Huang, Sihang Jia, Jungang Li, Lyuhao Chen, Junhao Chen, Hanqian Li, Aiwei Liu, Yibo Yan, Xuming Hu  

**一句话要点**：提出视觉语义自适应水印VISA-Mark，以解决大视觉语言模型中视觉无关水印破坏视觉保真度的问题。

**关键词**：大视觉语言模型, 视觉语义水印, 前缀调谐, 视觉保真度, 自适应扰动, 攻击鲁棒性

## 3 点简述
- 核心问题：现有水印方法引入视觉无关标记或导致高推理延迟，破坏视觉保真度。
- 方法要点：使用前缀调谐器提取视觉证据权重，自适应扰动视觉支持标记，严格保持视觉保真度。
- 实验或效果：在视觉一致性上提升7.8%，检测准确率达96.88% AUC，攻击鲁棒性达99.3%，不牺牲推理效率。

## 摘要（原文）

> Watermarking has emerged as a pivotal solution for content traceability and intellectual property protection in Large Vision-Language Models (LVLMs). However, vision-agnostic watermarks introduce visually irrelevant tokens and disrupt visual grounding by enforcing indiscriminate pseudo-random biases, while some semantic-aware methods incur prohibitive inference latency due to rejection sampling. In this paper, we propose the VIsual Semantic Adaptive Watermark (VISA-Mark), a novel framework that embeds detectable signals while strictly preserving visual fidelity. Our approach employs a lightweight, efficiently trained prefix-tuner to extract dynamic Visual-Evidence Weights, which quantify the evidentiary support for candidate tokens based on the visual input. These weights guide an adaptive vocabulary partitioning and logits perturbation mechanism, concentrating watermark strength specifically on visually-supported tokens. By actively aligning the watermark with visual evidence, VISA-Mark effectively maintains visual fidelity. Empirical results confirm that VISA-Mark outperforms conventional methods with a 7.8% improvement in visual consistency (Chair-I) and superior semantic fidelity. The framework maintains highly competitive detection accuracy (96.88% AUC) and robust attack resilience (99.3%) without sacrificing inference efficiency, effectively establishing a new standard for reliability-preserving multimodal watermarking.

