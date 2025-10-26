---
layout: default
title: HyperET: Efficient Training in Hyperbolic Space for Multi-modal Large Language Models
---

# HyperET: Efficient Training in Hyperbolic Space for Multi-modal Large Language Models
**arXiv**：[2510.20322v1](https://arxiv.org/abs/2510.20322) · [PDF](https://arxiv.org/pdf/2510.20322.pdf)  
**作者**：Zelin Peng, Zhengqin Xu, Qingyang Liu, Xiaokang Yang, Wei Shen  

**一句话要点**：提出HyperET在双曲空间中高效训练多模态大语言模型，以解决跨模态对齐计算资源高的问题

**关键词**：多模态大语言模型, 双曲空间训练, 跨模态对齐, 高效参数化, 视觉-文本粒度对齐

## 3 点简述
- 核心问题：多模态大语言模型训练计算资源高，视觉编码器缺乏多粒度语言对齐
- 方法要点：利用双曲空间建模层次结构，通过动态半径调整实现任意粒度视觉-文本对齐
- 实验或效果：在多个基准测试中，以少于1%额外参数显著提升现有模型性能

## 摘要（原文）

> Multi-modal large language models (MLLMs) have emerged as a transformative
> approach for aligning visual and textual understanding. They typically require
> extremely high computational resources (e.g., thousands of GPUs) for training
> to achieve cross-modal alignment at multi-granularity levels. We argue that a
> key source of this inefficiency lies in the vision encoders they widely equip
> with, e.g., CLIP and SAM, which lack the alignment with language at
> multi-granularity levels. To address this issue, in this paper, we leverage
> hyperbolic space, which inherently models hierarchical levels and thus provides
> a principled framework for bridging the granularity gap between visual and
> textual modalities at an arbitrary granularity level. Concretely, we propose an
> efficient training paradigm for MLLMs, dubbed as HyperET, which can optimize
> visual representations to align with their textual counterparts at an arbitrary
> granularity level through dynamic hyperbolic radius adjustment in hyperbolic
> space. HyperET employs learnable matrices with M\"{o}bius multiplication
> operations, implemented via three effective configurations: diagonal scaling
> matrices, block-diagonal matrices, and banded matrices, providing a flexible
> yet efficient parametrization strategy. Comprehensive experiments across
> multiple MLLM benchmarks demonstrate that HyperET consistently improves both
> existing pre-training and fine-tuning MLLMs clearly with less than 1\%
> additional parameters.

