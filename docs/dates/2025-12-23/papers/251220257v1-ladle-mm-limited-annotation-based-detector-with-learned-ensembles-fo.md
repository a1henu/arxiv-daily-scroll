---
layout: default
title: LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation
---

# LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation
**arXiv**：[2512.20257v1](https://arxiv.org/abs/2512.20257) · [PDF](https://arxiv.org/pdf/2512.20257.pdf)  
**作者**：Daniele Cardullo, Simone Teglia, Irene Amerini  

**一句话要点**：提出LADLE-MM，一种基于有限标注和模型集成的方法，用于检测多模态虚假信息。

**关键词**：多模态虚假信息检测, 有限标注学习, 模型集成, BLIP嵌入, 开放集泛化

## 3 点简述
- 核心问题：多模态虚假信息检测常依赖大量标注数据或复杂架构，资源消耗大。
- 方法要点：采用双单模态分支加多模态分支，结合BLIP嵌入作为固定参考空间，减少可训练参数。
- 实验或效果：在DGM4和VERITE数据集上表现竞争性，优于现有方法，尤其在无基础标注时。

## 摘要（原文）

> With the rise of easily accessible tools for generating and manipulating multimedia content, realistic synthetic alterations to digital media have become a widespread threat, often involving manipulations across multiple modalities simultaneously. Recently, such techniques have been increasingly employed to distort narratives of important events and to spread misinformation on social media, prompting the development of misinformation detectors. In the context of misinformation conveyed through image-text pairs, several detection methods have been proposed. However, these approaches typically rely on computationally intensive architectures or require large amounts of annotated data. In this work we introduce LADLE-MM: Limited Annotation based Detector with Learned Ensembles for Multimodal Misinformation, a model-soup initialized multimodal misinformation detector designed to operate under a limited annotation setup and constrained training resources. LADLE-MM is composed of two unimodal branches and a third multimodal one that enhances image and text representations with additional multimodal embeddings extracted from BLIP, serving as fixed reference space. Despite using 60.3% fewer trainable parameters than previous state-of-the-art models, LADLE-MM achieves competitive performance on both binary and multi-label classification tasks on the DGM4 benchmark, outperforming existing methods when trained without grounding annotations. Moreover, when evaluated on the VERITE dataset, LADLE-MM outperforms current state-of-the-art approaches that utilize more complex architectures involving Large Vision-Language-Models, demonstrating the effective generalization ability in an open-set setting and strong robustness to unimodal bias.

