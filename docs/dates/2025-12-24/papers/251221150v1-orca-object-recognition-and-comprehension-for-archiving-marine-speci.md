---
layout: default
title: ORCA: Object Recognition and Comprehension for Archiving Marine Species
---

# ORCA: Object Recognition and Comprehension for Archiving Marine Species
**arXiv**：[2512.21150v1](https://arxiv.org/abs/2512.21150) · [PDF](https://arxiv.org/pdf/2512.21150.pdf)  
**作者**：Yuk-Kwan Wong, Haixin Liang, Zeyu Ma, Yiwei Chen, Ziqiang Zheng, Rinaldi Gotama, Pascal Sebastian, Lauren D. Sparks, Sai-Kit Yeung  

**一句话要点**：提出ORCA多模态基准以解决海洋物种识别与理解中数据不足和任务定义不清的问题。

**关键词**：海洋视觉理解, 多模态基准, 对象检测, 实例描述, 视觉定位, 物种识别

## 3 点简述
- 核心问题：海洋视觉理解受限于训练数据稀缺和缺乏系统任务定义，阻碍模型应用。
- 方法要点：构建包含14,647图像、42,217边界框和22,321实例描述的多模态数据集，支持检测、描述和视觉定位任务。
- 实验或效果：评估18个先进模型，揭示物种多样性、形态重叠和领域特定需求等挑战，确立综合基准。

## 摘要（原文）

> Marine visual understanding is essential for monitoring and protecting marine ecosystems, enabling automatic and scalable biological surveys. However, progress is hindered by limited training data and the lack of a systematic task formulation that aligns domain-specific marine challenges with well-defined computer vision tasks, thereby limiting effective model application. To address this gap, we present ORCA, a multi-modal benchmark for marine research comprising 14,647 images from 478 species, with 42,217 bounding box annotations and 22,321 expert-verified instance captions. The dataset provides fine-grained visual and textual annotations that capture morphology-oriented attributes across diverse marine species. To catalyze methodological advances, we evaluate 18 state-of-the-art models on three tasks: object detection (closed-set and open-vocabulary), instance captioning, and visual grounding. Results highlight key challenges, including species diversity, morphological overlap, and specialized domain demands, underscoring the difficulty of marine understanding. ORCA thus establishes a comprehensive benchmark to advance research in marine domain. Project Page: http://orca.hkustvgd.com/.

