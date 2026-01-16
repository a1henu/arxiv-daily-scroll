---
layout: default
title: Unleashing the Capabilities of Large Vision-Language Models for Intelligent Perception of Roadside Infrastructure
---

# Unleashing the Capabilities of Large Vision-Language Models for Intelligent Perception of Roadside Infrastructure
**arXiv**：[2601.10551v1](https://arxiv.org/abs/2601.10551) · [PDF](https://arxiv.org/pdf/2601.10551.pdf)  
**作者**：Luxuan Fu, Chong Liu, Bisheng Yang, Zhen Dong  

**一句话要点**：提出领域适应框架，将大视觉语言模型转化为智能路边基础设施分析代理。

**关键词**：大视觉语言模型, 领域适应, 检索增强生成, 路边基础设施感知, 开放词汇检测, 知识增强推理

## 3 点简述
- 核心问题：通用大视觉语言模型在路边基础设施细粒度属性和工程标准识别上表现不佳。
- 方法要点：结合开放词汇微调、LoRA适应和双模态检索增强生成，提升模型专业性和准确性。
- 实验效果：在新数据集上实现58.9 mAP检测性能和95.5%属性识别准确率。

## 摘要（原文）

> Automated perception of urban roadside infrastructure is crucial for smart city management, yet general-purpose models often struggle to capture the necessary fine-grained attributes and domain rules. While Large Vision Language Models (VLMs) excel at open-world recognition, they often struggle to accurately interpret complex facility states in compliance with engineering standards, leading to unreliable performance in real-world applications. To address this, we propose a domain-adapted framework that transforms VLMs into specialized agents for intelligent infrastructure analysis. Our approach integrates a data-efficient fine-tuning strategy with a knowledge-grounded reasoning mechanism. Specifically, we leverage open-vocabulary fine-tuning on Grounding DINO to robustly localize diverse assets with minimal supervision, followed by LoRA-based adaptation on Qwen-VL for deep semantic attribute reasoning. To mitigate hallucinations and enforce professional compliance, we introduce a dual-modality Retrieval-Augmented Generation (RAG) module that dynamically retrieves authoritative industry standards and visual exemplars during inference. Evaluated on a comprehensive new dataset of urban roadside scenes, our framework achieves a detection performance of 58.9 mAP and an attribute recognition accuracy of 95.5%, demonstrating a robust solution for intelligent infrastructure monitoring.

