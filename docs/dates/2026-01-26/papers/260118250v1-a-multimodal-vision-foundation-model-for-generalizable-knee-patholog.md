---
layout: default
title: A multimodal vision foundation model for generalizable knee pathology
---

# A multimodal vision foundation model for generalizable knee pathology
**arXiv**：[2601.18250v1](https://arxiv.org/abs/2601.18250) · [PDF](https://arxiv.org/pdf/2601.18250.pdf)  
**作者**：Kang Yu, Dingyu Wang, Zimu Yuan, Nan Zhou, Jiajun Liu, Jiaxin Liu, Shanggui Liu, Yaoyan Zheng, Huishu Yuan, Di Huang, Dong Jiang  

**一句话要点**：提出OrthoFoundation多模态视觉基础模型，以解决肌肉骨骼影像诊断中任务碎片化与泛化性不足的问题。

**关键词**：多模态基础模型, 肌肉骨骼影像, 自监督学习, 医学影像诊断, 泛化性评估

## 3 点简述
- 核心问题：肌肉骨骼疾病诊断依赖任务特定监督学习，缺乏大规模开源数据集，导致模型泛化性差。
- 方法要点：基于Dinov3骨干，使用120万无标注膝部X光和MRI图像，通过自监督对比学习预训练多模态基础模型。
- 实验或效果：在14个下游任务中达到SOTA，仅用50%标注数据匹配监督基线，并展示跨解剖部位泛化能力。

## 摘要（原文）

> Musculoskeletal disorders represent a leading cause of global disability, creating an urgent demand for precise interpretation of medical imaging. Current artificial intelligence (AI) approaches in orthopedics predominantly rely on task-specific, supervised learning paradigms. These methods are inherently fragmented, require extensive annotated datasets, and often lack generalizability across different modalities and clinical scenarios. The development of foundation models in this field has been constrained by the scarcity of large-scale, curated, and open-source musculoskeletal datasets. To address these challenges, we introduce OrthoFoundation, a multimodal vision foundation model optimized for musculoskeletal pathology. We constructed a pre-training dataset of 1.2 million unlabeled knee X-ray and MRI images from internal and public databases. Utilizing a Dinov3 backbone, the model was trained via self-supervised contrastive learning to capture robust radiological representations. OrthoFoundation achieves state-of-the-art (SOTA) performance across 14 downstream tasks. It attained superior accuracy in X-ray osteoarthritis diagnosis and ranked first in MRI structural injury detection. The model demonstrated remarkable label efficiency, matching supervised baselines using only 50% of labeled data. Furthermore, despite being pre-trained on knee images, OrthoFoundation exhibited exceptional cross-anatomy generalization to the hip, shoulder, and ankle. OrthoFoundation represents a significant advancement toward general-purpose AI for musculoskeletal imaging. By learning fundamental, joint-agnostic radiological semantics from large-scale multimodal data, it overcomes the limitations of conventional models, which provides a robust framework for reducing annotation burdens and enhancing diagnostic accuracy in clinical practice.

