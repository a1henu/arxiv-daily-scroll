---
layout: default
title: Task-Adaptive Low-Dose CT Reconstruction
---

# Task-Adaptive Low-Dose CT Reconstruction
**arXiv**：[2511.07094v1](https://arxiv.org/abs/2511.07094) · [PDF](https://arxiv.org/pdf/2511.07094.pdf)  
**作者**：Necati Sefercioglu, Mehmet Ozan Unal, Metin Ertas, Isa Yildirim  

**一句话要点**：提出任务自适应低剂量CT重建框架，以提升诊断任务中的解剖细节保留

**关键词**：低剂量CT重建, 任务自适应优化, 正则化方法, 医学图像分割, 深度学习框架

## 3 点简述
- 核心问题：现有深度学习方法在低剂量CT重建中虽指标高，但诊断关键细节丢失
- 方法要点：使用预训练任务网络作为正则化项，指导重建训练，避免联合训练风险
- 实验或效果：在肝脏肿瘤分割任务中，Dice分数达0.707，优于传统和联合训练方法

## 摘要（原文）

> Deep learning-based low-dose computed tomography reconstruction methods
> already achieve high performance on standard image quality metrics like peak
> signal-to-noise ratio and structural similarity index measure. Yet, they
> frequently fail to preserve the critical anatomical details needed for
> diagnostic tasks. This fundamental limitation hinders their clinical
> applicability despite their high metric scores. We propose a novel
> task-adaptive reconstruction framework that addresses this gap by incorporating
> a frozen pre-trained task network as a regularization term in the
> reconstruction loss function. Unlike existing joint-training approaches that
> simultaneously optimize both reconstruction and task networks, and risk
> diverging from satisfactory reconstructions, our method leverages a pre-trained
> task model to guide reconstruction training while still maintaining diagnostic
> quality. We validate our framework on a liver and liver tumor segmentation
> task. Our task-adaptive models achieve Dice scores up to 0.707, approaching the
> performance of full-dose scans (0.874), and substantially outperforming
> joint-training approaches (0.331) and traditional reconstruction methods
> (0.626). Critically, our framework can be integrated into any existing deep
> learning-based reconstruction model through simple loss function modification,
> enabling widespread adoption for task-adaptive optimization in clinical
> practice. Our codes are available at:
> https://github.com/itu-biai/task_adaptive_ct

