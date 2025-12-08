---
layout: default
title: Distilling Expert Surgical Knowledge: How to train local surgical VLMs for anatomy explanation in Complete Mesocolic Excision
---

# Distilling Expert Surgical Knowledge: How to train local surgical VLMs for anatomy explanation in Complete Mesocolic Excision
**arXiv**：[2512.05740v1](https://arxiv.org/abs/2512.05740) · [PDF](https://arxiv.org/pdf/2512.05740.pdf)  
**作者**：Lennart Maack, Julia-Kristin Graß, Lisa-Marie Toscha, Nathaniel Melling, Alexander Schlaefer  

**一句话要点**：提出隐私保护框架，通过知识蒸馏训练本地可部署视觉语言模型，用于完全结肠系膜切除术中的解剖解释。

**关键词**：视觉语言模型, 知识蒸馏, 手术场景理解, 隐私保护, 监督微调, 直接偏好优化

## 3 点简述
- 当前视觉语言模型在特定手术场景理解如解剖标志识别方面存在不足，且需避免患者数据泄露到外部大型模型。
- 方法包括使用教师大语言模型生成专家监督数据集，仅基于文本上下文和二进制分割掩码，不涉及敏感图像，用于监督微调和直接偏好优化。
- 评估显示，通过生成数据集微调视觉语言模型，显著提升了手术领域知识，验证了数据高效且隐私合规的训练方式。

## 摘要（原文）

> Recently, Vision Large Language Models (VLMs) have demonstrated high potential in computer-aided diagnosis and decision-support. However, current VLMs show deficits in domain specific surgical scene understanding, such as identifying and explaining anatomical landmarks during Complete Mesocolic Excision. Additionally, there is a need for locally deployable models to avoid patient data leakage to large VLMs, hosted outside the clinic. We propose a privacy-preserving framework to distill knowledge from large, general-purpose LLMs into an efficient, local VLM. We generate an expert-supervised dataset by prompting a teacher LLM without sensitive images, using only textual context and binary segmentation masks for spatial information. This dataset is used for Supervised Fine-Tuning (SFT) and subsequent Direct Preference Optimization (DPO) of the locally deployable VLM. Our evaluation confirms that finetuning VLMs with our generated datasets increases surgical domain knowledge compared to its base VLM by a large margin. Overall, this work validates a data-efficient and privacy-conforming way to train a surgical domain optimized, locally deployable VLM for surgical scene understanding.

