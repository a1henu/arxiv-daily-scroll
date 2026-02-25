---
layout: default
title: OrthoDiffusion: A Generalizable Multi-Task Diffusion Foundation Model for Musculoskeletal MRI Interpretation
---

# OrthoDiffusion: A Generalizable Multi-Task Diffusion Foundation Model for Musculoskeletal MRI Interpretation
**arXiv**：[2602.20752v1](https://arxiv.org/abs/2602.20752) · [PDF](https://arxiv.org/pdf/2602.20752.pdf)  
**作者**：Tian Lan, Lei Xu, Zimu Yuan, Shanggui Liu, Jiajun Liu, Jiaxin Liu, Weilai Xiang, Hongyu Yang, Dong Jiang, Jianxin Yin, Dingyu Wang  

**一句话要点**：提出OrthoDiffusion扩散基础模型以解决肌肉骨骼MRI多任务解释的泛化挑战

**关键词**：扩散模型, 肌肉骨骼MRI, 多任务学习, 自监督预训练, 解剖分割, 多标签诊断

## 3 点简述
- 核心问题：肌肉骨骼MRI解释复杂，需多平面识别异常，专家依赖高且易变。
- 方法要点：基于三个方向特定3D扩散模型，自监督预训练，集成视图特征支持分割与诊断。
- 实验或效果：在膝关节分割与异常检测中表现优异，跨中心泛化强，标签稀缺时精度高，可迁移至其他关节。

## 摘要（原文）

> Musculoskeletal disorders represent a significant global health burden and are a leading cause of disability worldwide. While MRI is essential for accurate diagnosis, its interpretation remains exceptionally challenging. Radiologists must identify multiple potential abnormalities within complex anatomical structures across different imaging planes, a process that requires significant expertise and is prone to variability. We developed OrthoDiffusion, a unified diffusion-based foundation model designed for multi-task musculoskeletal MRI interpretation. The framework utilizes three orientation-specific 3D diffusion models, pre-trained in a self-supervised manner on 15,948 unlabeled knee MRI scans, to learn robust anatomical features from sagittal, coronal, and axial views. These view-specific representations are integrated to support diverse clinical tasks, including anatomical segmentation and multi-label diagnosis. Our evaluation demonstrates that OrthoDiffusion achieves excellent performance in the segmentation of 11 knee structures and the detection of 8 knee abnormalities. The model exhibited remarkable robustness across different clinical centers and MRI field strengths, consistently outperforming traditional supervised models. Notably, in settings where labeled data was scarce, OrthoDiffusion maintained high diagnostic precision using only 10\% of training labels. Furthermore, the anatomical representations learned from knee imaging proved highly transferable to other joints, achieving strong diagnostic performance across 11 diseases of the ankle and shoulder. These findings suggest that diffusion-based foundation models can serve as a unified platform for multi-disease diagnosis and anatomical segmentation, potentially improving the efficiency and accuracy of musculoskeletal MRI interpretation in real-world clinical workflows.

