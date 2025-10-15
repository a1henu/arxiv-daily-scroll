---
layout: default
title: IL3D: A Large-Scale Indoor Layout Dataset for LLM-Driven 3D Scene Generation
---

# IL3D: A Large-Scale Indoor Layout Dataset for LLM-Driven 3D Scene Generation
**arXiv**：[2510.12095v1](https://arxiv.org/abs/2510.12095) · [PDF](https://arxiv.org/pdf/2510.12095.pdf)  
**作者**：Wenxu Zhou, Kaixuan Nie, Hang Du, Dong Yin, Wei Huang, Siqiang Guo, Xiaobo Zhang, Pengbo Hu  

**一句话要点**：提出IL3D数据集以支持LLM驱动的3D室内场景生成

**关键词**：3D场景生成, 室内布局数据集, 大语言模型, 多模态学习, 监督微调

## 3 点简述
- 核心问题：缺乏多样高质量训练数据用于室内布局设计和3D场景生成。
- 方法要点：构建大规模数据集，包含室内布局、3D对象和自然语言注释。
- 实验或效果：监督微调LLM在IL3D上提升泛化能力，优于其他数据集。

## 摘要（原文）

> In this study, we present IL3D, a large-scale dataset meticulously designed
> for large language model (LLM)-driven 3D scene generation, addressing the
> pressing demand for diverse, high-quality training data in indoor layout
> design. Comprising 27,816 indoor layouts across 18 prevalent room types and a
> library of 29,215 high-fidelity 3D object assets, IL3D is enriched with
> instance-level natural language annotations to support robust multimodal
> learning for vision-language tasks. We establish rigorous benchmarks to
> evaluate LLM-driven scene generation. Experimental results show that supervised
> fine-tuning (SFT) of LLMs on IL3D significantly improves generalization and
> surpasses the performance of SFT on other datasets. IL3D offers flexible
> multimodal data export capabilities, including point clouds, 3D bounding boxes,
> multiview images, depth maps, normal maps, and semantic masks, enabling
> seamless adaptation to various visual tasks. As a versatile and robust
> resource, IL3D significantly advances research in 3D scene generation and
> embodied intelligence, by providing high-fidelity scene data to support
> environment perception tasks of embodied agents.

