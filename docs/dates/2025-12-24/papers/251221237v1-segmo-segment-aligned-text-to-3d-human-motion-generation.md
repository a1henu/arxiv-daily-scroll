---
layout: default
title: SegMo: Segment-aligned Text to 3D Human Motion Generation
---

# SegMo: Segment-aligned Text to 3D Human Motion Generation
**arXiv**：[2512.21237v1](https://arxiv.org/abs/2512.21237) · [PDF](https://arxiv.org/pdf/2512.21237.pdf)  
**作者**：Bowen Dang, Lin Wu, Xiaohang Yang, Zheng Yuan, Zhixiang Chen  

**一句话要点**：提出SegMo框架，通过细粒度文本-动作对齐解决文本生成3D人体动作问题。

**关键词**：文本到动作生成, 细粒度对齐, 对比学习, 3D人体动作, 语义片段, 动作检索

## 3 点简述
- 核心问题：现有方法在序列级别对齐文本与动作，忽略模态内部语义结构，导致对齐粗糙。
- 方法要点：将文本和动作分解为语义连贯的片段，通过对比学习实现细粒度对齐，包含文本与动作片段提取模块。
- 实验或效果：在HumanML3D数据集上TOP 1分数提升至0.553，并可应用于动作定位和动作-文本检索任务。

## 摘要（原文）

> Generating 3D human motions from textual descriptions is an important research problem with broad applications in video games, virtual reality, and augmented reality. Recent methods align the textual description with human motion at the sequence level, neglecting the internal semantic structure of modalities. However, both motion descriptions and motion sequences can be naturally decomposed into smaller and semantically coherent segments, which can serve as atomic alignment units to achieve finer-grained correspondence. Motivated by this, we propose SegMo, a novel Segment-aligned text-conditioned human Motion generation framework to achieve fine-grained text-motion alignment. Our framework consists of three modules: (1) Text Segment Extraction, which decomposes complex textual descriptions into temporally ordered phrases, each representing a simple atomic action; (2) Motion Segment Extraction, which partitions complete motion sequences into corresponding motion segments; and (3) Fine-grained Text-Motion Alignment, which aligns text and motion segments with contrastive learning. Extensive experiments demonstrate that SegMo improves the strong baseline on two widely used datasets, achieving an improved TOP 1 score of 0.553 on the HumanML3D test set. Moreover, thanks to the learned shared embedding space for text and motion segments, SegMo can also be applied to retrieval-style tasks such as motion grounding and motion-to-text retrieval.

