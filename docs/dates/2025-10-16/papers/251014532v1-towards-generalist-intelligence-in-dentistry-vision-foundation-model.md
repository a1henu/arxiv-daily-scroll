---
layout: default
title: Towards Generalist Intelligence in Dentistry: Vision Foundation Models for Oral and Maxillofacial Radiology
---

# Towards Generalist Intelligence in Dentistry: Vision Foundation Models for Oral and Maxillofacial Radiology
**arXiv**：[2510.14532v1](https://arxiv.org/abs/2510.14532) · [PDF](https://arxiv.org/pdf/2510.14532.pdf)  
**作者**：Xinrui Huang, Fan Xiao, Dongming He, Anqi Gao, Dandan Li, Xiaofan Zhang, Shaoting Zhang, Xudong Wang  

**一句话要点**：提出DentVFM视觉基础模型以解决牙科AI泛化不足问题

**关键词**：视觉基础模型, 自监督学习, 牙科放射学, 多模态图像, 泛化能力, 基准测试

## 3 点简述
- 牙科放射图像解读受限于专业医生短缺和AI系统单模态、任务特定设计
- 基于ViT架构开发2D和3D模型，使用自监督学习处理160万张多模态图像
- 在DentBench基准测试中显著优于基线，实现跨模态诊断和高效泛化

## 摘要（原文）

> Oral and maxillofacial radiology plays a vital role in dental healthcare, but
> radiographic image interpretation is limited by a shortage of trained
> professionals. While AI approaches have shown promise, existing dental AI
> systems are restricted by their single-modality focus, task-specific design,
> and reliance on costly labeled data, hindering their generalization across
> diverse clinical scenarios. To address these challenges, we introduce DentVFM,
> the first family of vision foundation models (VFMs) designed for dentistry.
> DentVFM generates task-agnostic visual representations for a wide range of
> dental applications and uses self-supervised learning on DentVista, a large
> curated dental imaging dataset with approximately 1.6 million multi-modal
> radiographic images from various medical centers. DentVFM includes 2D and 3D
> variants based on the Vision Transformer (ViT) architecture. To address gaps in
> dental intelligence assessment and benchmarks, we introduce DentBench, a
> comprehensive benchmark covering eight dental subspecialties, more diseases,
> imaging modalities, and a wide geographical distribution. DentVFM shows
> impressive generalist intelligence, demonstrating robust generalization to
> diverse dental tasks, such as disease diagnosis, treatment analysis, biomarker
> identification, and anatomical landmark detection and segmentation.
> Experimental results indicate DentVFM significantly outperforms supervised,
> self-supervised, and weakly supervised baselines, offering superior
> generalization, label efficiency, and scalability. Additionally, DentVFM
> enables cross-modality diagnostics, providing more reliable results than
> experienced dentists in situations where conventional imaging is unavailable.
> DentVFM sets a new paradigm for dental AI, offering a scalable, adaptable, and
> label-efficient model to improve intelligent dental healthcare and address
> critical gaps in global oral healthcare.

