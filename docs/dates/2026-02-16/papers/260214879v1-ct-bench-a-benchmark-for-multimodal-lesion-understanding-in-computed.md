---
layout: default
title: CT-Bench: A Benchmark for Multimodal Lesion Understanding in Computed Tomography
---

# CT-Bench: A Benchmark for Multimodal Lesion Understanding in Computed Tomography
**arXiv**：[2602.14879v1](https://arxiv.org/abs/2602.14879) · [PDF](https://arxiv.org/pdf/2602.14879.pdf)  
**作者**：Qingqing Zhu, Qiao Jin, Tejas S. Mathai, Yin Fang, Zhizheng Wang, Yifan Yang, Maame Sarfo-Gyamfi, Benjamin Hou, Ran Gu, Praveen T. S. Balamuralikrishna, Kenneth C. Wang, Ronald M. Summers, Zhiyong Lu  

**一句话要点**：提出CT-Bench基准数据集以解决CT影像中病灶理解的多模态任务评估问题。

**关键词**：CT影像分析, 病灶理解, 多模态基准, 视觉问答, 医学人工智能, 数据集构建

## 3 点简述
- 核心问题：公开CT数据集缺乏病灶级标注，限制AI在病灶自动勾画和报告生成方面的进展。
- 方法要点：构建包含病灶图像与元数据集及多任务视觉问答基准的综合数据集，涵盖病灶定位、描述、大小估计和属性分类。
- 实验或效果：评估多种先进多模态模型，通过微调在病灶分析任务上实现显著性能提升，验证临床实用性。

## 摘要（原文）

> Artificial intelligence (AI) can automatically delineate lesions on computed tomography (CT) and generate radiology report content, yet progress is limited by the scarcity of publicly available CT datasets with lesion-level annotations. To bridge this gap, we introduce CT-Bench, a first-of-its-kind benchmark dataset comprising two components: a Lesion Image and Metadata Set containing 20,335 lesions from 7,795 CT studies with bounding boxes, descriptions, and size information, and a multitask visual question answering benchmark with 2,850 QA pairs covering lesion localization, description, size estimation, and attribute categorization. Hard negative examples are included to reflect real-world diagnostic challenges. We evaluate multiple state-of-the-art multimodal models, including vision-language and medical CLIP variants, by comparing their performance to radiologist assessments, demonstrating the value of CT-Bench as a comprehensive benchmark for lesion analysis. Moreover, fine-tuning models on the Lesion Image and Metadata Set yields significant performance gains across both components, underscoring the clinical utility of CT-Bench.

