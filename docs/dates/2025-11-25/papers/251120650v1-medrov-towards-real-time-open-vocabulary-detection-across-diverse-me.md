---
layout: default
title: MedROV: Towards Real-Time Open-Vocabulary Detection Across Diverse Medical Imaging Modalities
---

# MedROV: Towards Real-Time Open-Vocabulary Detection Across Diverse Medical Imaging Modalities
**arXiv**：[2511.20650v1](https://arxiv.org/abs/2511.20650) · [PDF](https://arxiv.org/pdf/2511.20650.pdf)  
**作者**：Tooba Tehreem Sheikh, Jean Lahoud, Rao Muhammad Anwer, Fahad Shahbaz Khan, Salman Khan, Hisham Cholakkal  

**一句话要点**：提出MedROV实时开放词汇检测模型，解决医学影像中未知结构检测问题

**关键词**：开放词汇检测, 医学影像, 实时检测, 对比学习, 多模态数据集, 伪标签策略

## 3 点简述
- 医学影像检测受限于封闭集范式，无法识别新标签对象
- 构建大规模数据集Omnis，采用伪标签策略和对比学习增强泛化
- 实验显示mAP50提升40，运行速度70 FPS，超越现有方法

## 摘要（原文）

> Traditional object detection models in medical imaging operate within a closed-set paradigm, limiting their ability to detect objects of novel labels. Open-vocabulary object detection (OVOD) addresses this limitation but remains underexplored in medical imaging due to dataset scarcity and weak text-image alignment. To bridge this gap, we introduce MedROV, the first Real-time Open Vocabulary detection model for medical imaging. To enable open-vocabulary learning, we curate a large-scale dataset, Omnis, with 600K detection samples across nine imaging modalities and introduce a pseudo-labeling strategy to handle missing annotations from multi-source datasets. Additionally, we enhance generalization by incorporating knowledge from a large pre-trained foundation model. By leveraging contrastive learning and cross-modal representations, MedROV effectively detects both known and novel structures. Experimental results demonstrate that MedROV outperforms the previous state-of-the-art foundation model for medical image detection with an average absolute improvement of 40 mAP50, and surpasses closed-set detectors by more than 3 mAP50, while running at 70 FPS, setting a new benchmark in medical detection. Our source code, dataset, and trained model are available at https://github.com/toobatehreem/MedROV.

