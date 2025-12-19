---
layout: default
title: Scaling Laws for Energy Efficiency of Local LLMs
---

# Scaling Laws for Energy Efficiency of Local LLMs
**arXiv**：[2512.16531v1](https://arxiv.org/abs/2512.16531) · [PDF](https://arxiv.org/pdf/2512.16531.pdf)  
**作者**：Ander Alvarez, Alessandro Genuardi, Nilotpal Sinha, Antonio Tiene, Samuel Mugel, Román Orús  

**一句话要点**：提出CPU推理的能效缩放定律与量子压缩方法，优化本地大模型部署。

**关键词**：本地大模型部署, CPU推理缩放定律, 视觉语言模型预处理, 量子压缩技术, 边缘计算能效

## 3 点简述
- 核心问题：CPU推理的能效缩放规律未知，影响本地大模型在边缘设备的部署。
- 方法要点：系统基准测试揭示语言模型线性缩放与视觉语言模型分辨率拐点。
- 实验或效果：量子压缩技术降低计算与能耗达71.9%和62%，保持语义准确性。

## 摘要（原文）

> Deploying local large language models and vision-language models on edge devices requires balancing accuracy with constrained computational and energy budgets. Although graphics processors dominate modern artificial-intelligence deployment, most consumer hardware--including laptops, desktops, industrial controllers, and embedded systems--relies on central processing units. Despite this, the computational laws governing central-processing-unit-only inference for local language and vision-language workloads remain largely unexplored. We systematically benchmark large language and vision-language models on two representative central-processing-unit tiers widely used for local inference: a MacBook Pro M2, reflecting mainstream laptop-class deployment, and a Raspberry Pi 5, representing constrained, low-power embedded settings. Using a unified methodology based on continuous sampling of processor and memory usage together with area-under-curve integration, we characterize how computational load scales with input text length for language models and with image resolution for vision-language models. We uncover two empirical scaling laws: (1) computational cost for language-model inference scales approximately linearly with token length; and (2) vision-language models exhibit a preprocessing-driven "resolution knee", where compute remains constant above an internal resolution clamp and decreases sharply below it. Beyond these laws, we show that quantum-inspired compression reduces processor and memory usage by up to 71.9% and energy consumption by up to 62%, while preserving or improving semantic accuracy. These results provide a systematic quantification of multimodal central-processing-unit-only scaling for local language and vision-language workloads, and they identify model compression and input-resolution preprocessing as effective, low-cost levers for sustainable edge inference.

