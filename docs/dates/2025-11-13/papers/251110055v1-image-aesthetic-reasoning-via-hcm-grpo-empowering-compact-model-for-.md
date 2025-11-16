---
layout: default
title: Image Aesthetic Reasoning via HCM-GRPO: Empowering Compact Model for Superior Performance
---

# Image Aesthetic Reasoning via HCM-GRPO: Empowering Compact Model for Superior Performance
**arXiv**：[2511.10055v1](https://arxiv.org/abs/2511.10055) · [PDF](https://arxiv.org/pdf/2511.10055.pdf)  
**作者**：Zhiyuan Hu, Zheng Sun, Yi Wei, Long Yu  

**一句话要点**：提出HCM-GRPO方法以提升图像美学推理性能

**关键词**：图像美学推理, 多模态大语言模型, 强化学习优化, 数据集构建, 链式思维数据

## 3 点简述
- 核心问题：MLLMs在图像美学推理中表现差，缺乏数据和推理能力
- 方法要点：引入HCM策略和DPA奖励，增强GRPO框架
- 实验或效果：小模型超越开源和闭源大模型，性能显著提升

## 摘要（原文）

> The performance of image generation has been significantly improved in recent years. However, the study of image screening is rare and its performance with Multimodal Large Language Models (MLLMs) is unsatisfactory due to the lack of data and the weak image aesthetic reasoning ability in MLLMs. In this work, we propose a complete solution to address these problems in terms of data and methodology. For data, we collect a comprehensive image screening dataset with over 128k samples, about 640k images. Each sample consists of an original image, four generated images. The dataset evaluates the image aesthetic reasoning ability under four aspects: appearance deformation, physical shadow, placement layout, and extension rationality. Regarding data annotation, we investigate multiple approaches, including purely manual, fully automated, and answer-driven annotations, to acquire high-quality chains of thought (CoT) data in the most cost-effective manner. Methodologically, we introduce a Hard Cases Mining (HCM) strategy with a Dynamic Proportional Accuracy (DPA) reward into the Group Relative Policy Optimization (GRPO) framework, called HCM-GRPO. This enhanced method demonstrates superior image aesthetic reasoning capabilities compared to the original GRPO. Our experimental results reveal that even state-of-the-art closed-source MLLMs, such as GPT4o and Qwen-VL-Max, exhibit performance akin to random guessing in image aesthetic reasoning. In contrast, by leveraging the HCM-GRPO, we are able to surpass the scores of both large-scale open-source and leading closed-source models with a much smaller model.

