---
layout: default
title: HDINO: A Concise and Efficient Open-Vocabulary Detector
---

# HDINO: A Concise and Efficient Open-Vocabulary Detector
**arXiv**：[2603.02924v1](https://arxiv.org/abs/2603.02924) · [PDF](https://arxiv.org/pdf/2603.02924.pdf)  
**作者**：Hao Zhang, Yiqun Wang, Qinran Lin, Runze Fan, Yong Li  

**一句话要点**：提出HDINO，一种简洁高效的开集目标检测器，减少对精细标注数据和复杂跨模态特征的依赖。

**关键词**：开集目标检测, 语义对齐, 两阶段训练, 轻量级特征融合, Transformer模型

## 3 点简述
- 核心问题：现有开集目标检测方法依赖精细标注数据和资源密集型跨模态特征提取，导致效率低下。
- 方法要点：采用两阶段训练策略，包括一阶段的一对多语义对齐机制和难度加权分类损失，以及二阶段的轻量级特征融合模块。
- 实验或效果：在Swin Transformer-T设置下，HDINO-T在COCO上达到49.2 mAP，超越Grounding DINO-T和T-Rex2，微调后性能进一步提升。

## 摘要（原文）

> Despite the growing interest in open-vocabulary object detection in recent years, most existing methods rely heavily on manually curated fine-grained training datasets as well as resource-intensive layer-wise cross-modal feature extraction. In this paper, we propose HDINO, a concise yet efficient open-vocabulary object detector that eliminates the dependence on these components. Specifically, we propose a two-stage training strategy built upon the transformer-based DINO model. In the first stage, noisy samples are treated as additional positive object instances to construct a One-to-Many Semantic Alignment Mechanism(O2M) between the visual and textual modalities, thereby facilitating semantic alignment. A Difficulty Weighted Classification Loss (DWCL) is also designed based on initial detection difficulty to mine hard examples and further improve model performance. In the second stage, a lightweight feature fusion module is applied to the aligned representations to enhance sensitivity to linguistic semantics. Under the Swin Transformer-T setting, HDINO-T achieves \textbf{49.2} mAP on COCO using 2.2M training images from two publicly available detection datasets, without any manual data curation and the use of grounding data, surpassing Grounding DINO-T and T-Rex2 by \textbf{0.8} mAP and \textbf{2.8} mAP, respectively, which are trained on 5.4M and 6.5M images. After fine-tuning on COCO, HDINO-T and HDINO-L further achieve \textbf{56.4} mAP and \textbf{59.2} mAP, highlighting the effectiveness and scalability of our approach. Code and models are available at https://github.com/HaoZ416/HDINO.

