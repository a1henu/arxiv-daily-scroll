---
layout: default
title: Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing
---

# Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing
**arXiv**：[2510.19808v1](https://arxiv.org/abs/2510.19808) · [PDF](https://arxiv.org/pdf/2510.19808.pdf)  
**作者**：Yusu Qian, Eli Bocek-Rivele, Liangchen Song, Jialing Tong, Yinfei Yang, Jiasen Lu, Wenze Hu, Zhe Gan  

**一句话要点**：提出Pico-Banana-400K数据集以解决文本引导图像编辑中大规模高质量数据缺失问题

**关键词**：文本引导图像编辑, 大规模数据集, 多模态模型, 图像编辑分类, 指令忠实度, 多轮编辑

## 3 点简述
- 核心问题：文本引导图像编辑研究因缺乏大规模、高质量、开放的真实图像数据集而受限
- 方法要点：利用Nano-Banana从OpenImages生成编辑对，通过细粒度分类和多模态模型评分确保质量与多样性
- 实验或效果：数据集包含40万图像，支持多轮编辑、偏好对齐和指令重写等复杂场景研究

## 摘要（原文）

> Recent advances in multimodal models have demonstrated remarkable text-guided
> image editing capabilities, with systems like GPT-4o and Nano-Banana setting
> new benchmarks. However, the research community's progress remains constrained
> by the absence of large-scale, high-quality, and openly accessible datasets
> built from real images. We introduce Pico-Banana-400K, a comprehensive
> 400K-image dataset for instruction-based image editing. Our dataset is
> constructed by leveraging Nano-Banana to generate diverse edit pairs from real
> photographs in the OpenImages collection. What distinguishes Pico-Banana-400K
> from previous synthetic datasets is our systematic approach to quality and
> diversity. We employ a fine-grained image editing taxonomy to ensure
> comprehensive coverage of edit types while maintaining precise content
> preservation and instruction faithfulness through MLLM-based quality scoring
> and careful curation. Beyond single turn editing, Pico-Banana-400K enables
> research into complex editing scenarios. The dataset includes three specialized
> subsets: (1) a 72K-example multi-turn collection for studying sequential
> editing, reasoning, and planning across consecutive modifications; (2) a
> 56K-example preference subset for alignment research and reward model training;
> and (3) paired long-short editing instructions for developing instruction
> rewriting and summarization capabilities. By providing this large-scale,
> high-quality, and task-rich resource, Pico-Banana-400K establishes a robust
> foundation for training and benchmarking the next generation of text-guided
> image editing models.

