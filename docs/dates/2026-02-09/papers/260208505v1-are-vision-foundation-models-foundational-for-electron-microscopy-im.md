---
layout: default
title: Are Vision Foundation Models Foundational for Electron Microscopy Image Segmentation?
---

# Are Vision Foundation Models Foundational for Electron Microscopy Image Segmentation?
**arXiv**：[2602.08505v1](https://arxiv.org/abs/2602.08505) · [PDF](https://arxiv.org/pdf/2602.08505.pdf)  
**作者**：Caterina Fuster-Barceló, Virginie Uhlmann  

**一句话要点**：评估视觉基础模型在电子显微镜图像分割中的跨域适应性与局限性

**关键词**：视觉基础模型, 电子显微镜图像分割, 参数高效微调, 域不匹配, 线粒体分割, 跨域适应

## 3 点简述
- 研究视觉基础模型在异质电子显微镜数据集上的跨域分割性能，聚焦线粒体分割问题
- 采用冻结主干与LoRA参数高效微调两种适应策略，评估DINOv2、DINOv3和OpenCLIP模型
- 实验显示单域训练效果良好，但多域训练性能显著下降，揭示数据集间存在持久域不匹配

## 摘要（原文）

> Although vision foundation models (VFMs) are increasingly reused for biomedical image analysis, it remains unclear whether the latent representations they provide are general enough to support effective transfer and reuse across heterogeneous microscopy image datasets. Here, we study this question for the problem of mitochondria segmentation in electron microscopy (EM) images, using two popular public EM datasets (Lucchi++ and VNC) and three recent representative VFMs (DINOv2, DINOv3, and OpenCLIP). We evaluate two practical model adaptation regimes: a frozen-backbone setting in which only a lightweight segmentation head is trained on top of the VFM, and parameter-efficient fine-tuning (PEFT) via Low-Rank Adaptation (LoRA) in which the VFM is fine-tuned in a targeted manner to a specific dataset. Across all backbones, we observe that training on a single EM dataset yields good segmentation performance (quantified as foreground Intersection-over-Union), and that LoRA consistently improves in-domain performance. In contrast, training on multiple EM datasets leads to severe performance degradation for all models considered, with only marginal gains from PEFT. Exploration of the latent representation space through various techniques (PCA, Fréchet Dinov2 distance, and linear probes) reveals a pronounced and persistent domain mismatch between the two considered EM datasets in spite of their visual similarity, which is consistent with the observed failure of paired training. These results suggest that, while VFMs can deliver competitive results for EM segmentation within a single domain under lightweight adaptation, current PEFT strategies are insufficient to obtain a single robust model across heterogeneous EM datasets without additional domain-alignment mechanisms.

