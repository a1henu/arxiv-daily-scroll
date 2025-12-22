---
layout: default
title: DAVE: A VLM Vision Encoder for Document Understanding and Web Agents
---

# DAVE: A VLM Vision Encoder for Document Understanding and Web Agents
**arXiv**：[2512.17221v1](https://arxiv.org/abs/2512.17221) · [PDF](https://arxiv.org/pdf/2512.17221.pdf)  
**作者**：Brandon Huang, Hang Hua, Zhuoran Yu, Trevor Darrell, Rogerio Feris, Roei Herzig  

**一句话要点**：提出DAVE视觉编码器，以解决文档理解和网页代理任务中视觉语言模型的结构与空间信息不足问题。

**关键词**：视觉语言模型, 文档理解, 网页代理, 自监督预训练, 模型合并, 集成训练

## 3 点简述
- 核心问题：视觉语言模型的低层特征缺乏文档理解和网页代理所需的结构与空间信息。
- 方法要点：通过自监督和自回归预训练，结合模型合并与集成训练，提升编码器在文档和网页任务中的兼容性与性能。
- 实验或效果：在文档任务、VQA、网页定位和代理基准测试中验证了方法的有效性。

## 摘要（原文）

> While Vision-language models (VLMs) have demonstrated remarkable performance across multi-modal tasks, their choice of vision encoders presents a fundamental weakness: their low-level features lack the robust structural and spatial information essential for document understanding and web agents. To bridge this gap, we introduce DAVE, a vision encoder purpose-built for VLMs and tailored for these tasks. Our training pipeline is designed to leverage abundant unlabeled data to bypass the need for costly large-scale annotations for document and web images. We begin with a self-supervised pretraining stage on unlabeled images, followed by a supervised autoregressive pretraining stage, where the model learns tasks like parsing and localization from limited, high-quality data. Within the supervised stage, we adopt two strategies to improve our encoder's alignment with both general visual knowledge and diverse document and web agentic tasks: (i) We introduce a novel model-merging scheme, combining encoders trained with different text decoders to ensure broad compatibility with different web agentic architectures. (ii) We use ensemble training to fuse features from pretrained generalist encoders (e.g., SigLIP2) with our own document and web-specific representations. Extensive experiments on classic document tasks, VQAs, web localization, and agent-based benchmarks validate the effectiveness of our approach, establishing DAVE as a strong vision encoder for document and web applications.

