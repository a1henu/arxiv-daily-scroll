---
layout: default
title: CoRe-BT: A Multimodal Radiology-Pathology-Text Benchmark for Robust Brain Tumor Typing
---

# CoRe-BT: A Multimodal Radiology-Pathology-Text Benchmark for Robust Brain Tumor Typing
**arXiv**：[2603.03618v1](https://arxiv.org/abs/2603.03618) · [PDF](https://arxiv.org/pdf/2603.03618.pdf)  
**作者**：Juampablo E. Heras Rivera, Daniel K. Low, Xavier Xiong, Jacob J. Ruzevick, Daniel D. Child, Wen-wai Yim, Mehmet Kurt, Asma Ben Abacha  

**一句话要点**：提出CoRe-BT多模态基准，用于在模态缺失条件下研究脑肿瘤分型的鲁棒性学习。

**关键词**：脑肿瘤分型, 多模态学习, 模态缺失, 医学影像分析, 基准数据集

## 3 点简述
- 核心问题：脑肿瘤分型需整合MRI、病理图像和报告，但临床数据常不完整。
- 方法要点：构建包含310例患者的多模态数据集，支持缺失模态下的鲁棒学习。
- 实验或效果：评估多模态融合可行性，显示模态互补性，提升分型准确性。

## 摘要（原文）

> Accurate brain tumor typing requires integrating heterogeneous clinical evidence, including magnetic resonance imaging (MRI), histopathology, and pathology reports, which are often incomplete at the time of diagnosis. We introduce CoRe-BT, a cross-modal radiology-pathology-text benchmark for brain tumor typing, designed to study robust multimodal learning under missing modality conditions. The dataset comprises 310 patients with multi-sequence brain MRI (T1, T1c, T2, FLAIR), including 95 cases with paired H&E-stained whole-slide pathology images and pathology reports. All cases are annotated with tumor type and grade, and MRI volumes include expert-annotated tumor masks, enabling both region-aware modeling and auxiliary learning tasks. Tumors are categorized into six clinically relevant classes capturing the heterogeneity of common and rare glioma subtypes. We evaluate tumor typing under variable modality availability by comparing MRI-only models with multimodal approaches that incorporate pathology information when present. Baseline experiments demonstrate the feasibility of multimodal fusion and highlight complementary modality contributions across clinically relevant typing tasks. CoRe-BT provides a grounded testbed for advancing multimodal glioma typing and representation learning in realistic scenarios with incomplete clinical data.

