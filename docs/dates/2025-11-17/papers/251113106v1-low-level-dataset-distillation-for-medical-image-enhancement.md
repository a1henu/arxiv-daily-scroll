---
layout: default
title: Low-Level Dataset Distillation for Medical Image Enhancement
---

# Low-Level Dataset Distillation for Medical Image Enhancement
**arXiv**：[2511.13106v1](https://arxiv.org/abs/2511.13106) · [PDF](https://arxiv.org/pdf/2511.13106.pdf)  
**作者**：Fengzhi Xu, Ziyuan Yang, Mengyu Sun, Joey Tianyi Zhou, Yi Zhang  

**一句话要点**：提出低层数据集蒸馏方法以解决医学图像增强中的训练成本与隐私问题

**关键词**：医学图像增强, 数据集蒸馏, 低层视觉任务, 隐私保护, 像素级映射

## 3 点简述
- 核心问题：低层任务像素级保真度要求高，数据集蒸馏为欠定问题，难以约束密集映射
- 方法要点：利用解剖相似性构建共享先验，通过SPG模块个性化并注入患者知识
- 实验或效果：蒸馏数据集仅含抽象信息，保护隐私，未知具体性能提升

## 摘要（原文）

> Medical image enhancement is clinically valuable, but existing methods require large-scale datasets to learn complex pixel-level mappings. However, the substantial training and storage costs associated with these datasets hinder their practical deployment. While dataset distillation (DD) can alleviate these burdens, existing methods mainly target high-level tasks, where multiple samples share the same label. This many-to-one mapping allows distilled data to capture shared semantics and achieve information compression. In contrast, low-level tasks involve a many-to-many mapping that requires pixel-level fidelity, making low-level DD an underdetermined problem, as a small distilled dataset cannot fully constrain the dense pixel-level mappings. To address this, we propose the first low-level DD method for medical image enhancement. We first leverage anatomical similarities across patients to construct the shared anatomical prior based on a representative patient, which serves as the initialization for the distilled data of different patients. This prior is then personalized for each patient using a Structure-Preserving Personalized Generation (SPG) module, which integrates patient-specific anatomical information into the distilled dataset while preserving pixel-level fidelity. For different low-level tasks, the distilled data is used to construct task-specific high- and low-quality training pairs. Patient-specific knowledge is injected into the distilled data by aligning the gradients computed from networks trained on the distilled pairs with those from the corresponding patient's raw data. Notably, downstream users cannot access raw patient data. Instead, only a distilled dataset containing abstract training information is shared, which excludes patient-specific details and thus preserves privacy.

