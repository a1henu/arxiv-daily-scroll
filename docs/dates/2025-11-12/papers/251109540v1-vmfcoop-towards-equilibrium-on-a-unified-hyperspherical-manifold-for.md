---
layout: default
title: vMFCoOp: Towards Equilibrium on a Unified Hyperspherical Manifold for Prompting Biomedical VLMs
---

# vMFCoOp: Towards Equilibrium on a Unified Hyperspherical Manifold for Prompting Biomedical VLMs
**arXiv**：[2511.09540v1](https://arxiv.org/abs/2511.09540) · [PDF](https://arxiv.org/pdf/2511.09540.pdf)  
**作者**：Minye Shao, Sihan Guo, Xinrun Li, Xingyu Miao, Haoran Duan, Yang Long  

**一句话要点**：提出vMFCoOp框架以解决生物医学视觉语言模型提示学习中的语义错位问题

**关键词**：提示学习, 超球面流形, 生物医学视觉语言模型, 语义对齐, 少样本分类

## 3 点简述
- 核心问题：LLM与CLIP模型语义错位，欧几里得空间优化难以建模统一表示
- 方法要点：在共享超球面流形上估计vMF分布，通过统一语义锚点对齐语义偏差
- 实验或效果：在14个医学数据集上表现优于现有方法，提升准确性和泛化能力

## 摘要（原文）

> Recent advances in context optimization (CoOp) guided by large language model (LLM)-distilled medical semantic priors offer a scalable alternative to manual prompt engineering and full fine-tuning for adapting biomedical CLIP-based vision-language models (VLMs). However, prompt learning in this context is challenged by semantic misalignment between LLMs and CLIP variants due to divergent training corpora and model architectures; it further lacks scalability across continuously evolving families of foundation models. More critically, pairwise multimodal alignment via conventional Euclidean-space optimization lacks the capacity to model unified representations or apply localized geometric constraints, which tends to amplify modality gaps in complex biomedical imaging and destabilize few-shot adaptation. In this work, we propose vMFCoOp, a framework that inversely estimates von Mises-Fisher (vMF) distributions on a shared Hyperspherical Manifold, aligning semantic biases between arbitrary LLMs and CLIP backbones via Unified Semantic Anchors to achieve robust biomedical prompting and superior few-shot classification. Grounded in three complementary constraints, vMFCoOp demonstrates consistent improvements across 14 medical datasets, 12 medical imaging modalities, and 13 anatomical regions, outperforming state-of-the-art methods in accuracy, generalization, and clinical applicability. This work will be continuously expanded to encompass more downstream applications, and the corresponding resources are intended to be shared through https://github.com/VinyehShaw/UniEqui.

