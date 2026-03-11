---
layout: default
title: RA-SSU: Towards Fine-Grained Audio-Visual Learning with Region-Aware Sound Source Understanding
---

# RA-SSU: Towards Fine-Grained Audio-Visual Learning with Region-Aware Sound Source Understanding
**arXiv**：[2603.09809v1](https://arxiv.org/abs/2603.09809) · [PDF](https://arxiv.org/pdf/2603.09809.pdf)  
**作者**：Muyi Sun, Yixuan Wang, Hong Wang, Chen Su, Man Zhang, Xingqun Qi, Qi Li, Zhenan Sun  

**一句话要点**：提出RA-SSU任务与SSUFormer模型，实现细粒度音频-视觉学习中的区域感知声源理解。

**关键词**：细粒度音频-视觉学习, 区域感知声源理解, 声源分割, 多模态学习, 数据集构建, Transformer模型

## 3 点简述
- 定义细粒度音频-视觉学习任务RA-SSU，旨在实现区域感知、帧级别的高质量声源理解。
- 构建f-Music和f-Lifescene数据集，提供带注释的声源掩码和逐帧文本描述，支持任务评估。
- 提出SSUFormer基准模型，结合MCM和MoHE模块，在声源分割和描述任务中达到SOTA性能。

## 摘要（原文）

> Audio-Visual Learning (AVL) is one fundamental task of multi-modality learning and embodied intelligence, displaying the vital role in scene understanding and interaction. However, previous researchers mostly focus on exploring downstream tasks from a coarse-grained perspective (e.g., audio-visual correspondence, sound source localization, and audio-visual event localization). Considering providing more specific scene perception details, we newly define a fine-grained Audio-Visual Learning task, termed Region-Aware Sound Source Understanding (RA-SSU), which aims to achieve region-aware, frame-level, and high-quality sound source understanding. To support this goal, we innovatively construct two corresponding datasets, i.e. fine-grained Music (f-Music) and fine-grained Lifescene (f-Lifescene), each containing annotated sound source masks and frame-by-frame textual descriptions. The f-Music dataset includes 3,976 samples across 22 scene types related to specific application scenarios, focusing on music scenes with complex instrument mixing. The f-Lifescene dataset contains 6,156 samples across 61 types representing diverse sounding objects in life scenarios. Moreover, we propose SSUFormer, a Sound-Source Understanding TransFormer benchmark that facilitates both the sound source segmentation and sound region description with a multi-modal input and multi-modal output architecture. Specifically, we design two modules for this framework, Mask Collaboration Module (MCM) and Mixture of Hierarchical-prompted Experts (MoHE), to respectively enhance the accuracy and enrich the elaboration of the sound source description. Extensive experiments are conducted on our two datasets to verify the feasibility of the task, evaluate the availability of the datasets, and demonstrate the superiority of the SSUFormer, which achieves SOTA performance on the Sound Source Understanding benchmark.

