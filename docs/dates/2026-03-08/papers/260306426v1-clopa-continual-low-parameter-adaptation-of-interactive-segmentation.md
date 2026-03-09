---
layout: default
title: CLoPA: Continual Low Parameter Adaptation of Interactive Segmentation for Medical Image Annotation
---

# CLoPA: Continual Low Parameter Adaptation of Interactive Segmentation for Medical Image Annotation
**arXiv**：[2603.06426v1](https://arxiv.org/abs/2603.06426) · [PDF](https://arxiv.org/pdf/2603.06426.pdf)  
**作者**：Parhom Esmaeili, Chayanin Tangwiriyasakul, Eli Gibson, Sebastien Ourselin, M. Jorge Cardoso  

**一句话要点**：提出CLoPA以通过持续低参数适应提升医学图像交互分割的标注性能

**关键词**：交互式分割, 持续学习, 医学图像标注, 参数微调, 任务适应

## 3 点简述
- 现有零样本模型在多样化医学图像任务中性能不稳定，难以达到专家水平
- CLoPA基于标注缓存持续微调少量参数，无需新增参数或改变推理流程
- 在八个医学分割任务中快速提升至专家级性能，多数增益在单次训练后实现

## 摘要（原文）

> Interactive segmentation enables clinicians to guide annotation, but existing zero-shot models like nnInteractive fail to consistently reach expert-level performance across diverse medical imaging tasks. Because annotation campaigns produce a growing stream of task-specific labelled data, online adaptation of the segmentation model is a natural complement to zero-shot inference. We propose CLoPA, a continual adaptation strategy that tunes a small fraction of nnInteractive's parameters on the annotation cache, triggered by lightweight episode scheduling. CLoPA requires no new parameters or changes to the inference pipeline, and operates entirely within the existing annotation workflow. Across eight Medical Segmentation Decathlon tasks spanning diverse anatomical targets and imaging characteristics, CLoPA rapidly elevates performance to expert-level, even for tasks where nnInteractive previously failed, with the majority of gains realised after a single training episode. We show that the benefits of tuning different parameter groups depends on task characteristics and data regimes. Also, that for targets with complex geometries (e.g., hepatic vessels), instance normalisation and low-level feature tuning saturates, suggesting a need for deeper feature-representation alignment in the most challenging scenarios.

