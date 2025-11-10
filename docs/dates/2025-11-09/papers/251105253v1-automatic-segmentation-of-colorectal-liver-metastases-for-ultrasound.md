---
layout: default
title: Automatic segmentation of colorectal liver metastases for ultrasound-based navigated resection
---

# Automatic segmentation of colorectal liver metastases for ultrasound-based navigated resection
**arXiv**：[2511.05253v1](https://arxiv.org/abs/2511.05253) · [PDF](https://arxiv.org/pdf/2511.05253.pdf)  
**作者**：Tiziano Natali, Karin A. Olthof, Niels F. M. Kok, Koert F. D. Kuhlmann, Theo J. M. Ruers, Matteo Fusaglia  

**一句话要点**：提出基于裁剪3D U-Net的自动分割方法，以提升结直肠肝转移瘤超声导航切除的精度与效率。

**关键词**：结直肠肝转移瘤分割, 3D U-Net, 术中超声导航, 自动分割, nnU-Net框架, 实时手术指导

## 3 点简述
- 核心问题：术中超声图像对比度低、噪声大，手动分割结直肠肝转移瘤困难，影响手术切缘准确性。
- 方法要点：使用nnU-Net框架训练3D U-Net，比较全体积和裁剪体积模型，集成3D Slicer实现实时导航。
- 实验或效果：裁剪模型DSC中位数0.74，执行时间约1分钟，前瞻测试显示临床可接受的实时性能。

## 摘要（原文）

> Introduction: Accurate intraoperative delineation of colorectal liver
> metastases (CRLM) is crucial for achieving negative resection margins but
> remains challenging using intraoperative ultrasound (iUS) due to low contrast,
> noise, and operator dependency. Automated segmentation could enhance precision
> and efficiency in ultrasound-based navigation workflows.
>   Methods: Eighty-five tracked 3D iUS volumes from 85 CRLM patients were used
> to train and evaluate a 3D U-Net implemented via the nnU-Net framework. Two
> variants were compared: one trained on full iUS volumes and another on cropped
> regions around tumors. Segmentation accuracy was assessed using Dice Similarity
> Coefficient (DSC), Hausdorff Distance (HDist.), and Relative Volume Difference
> (RVD) on retrospective and prospective datasets. The workflow was integrated
> into 3D Slicer for real-time intraoperative use.
>   Results: The cropped-volume model significantly outperformed the full-volume
> model across all metrics (AUC-ROC = 0.898 vs 0.718). It achieved median DSC =
> 0.74, recall = 0.79, and HDist. = 17.1 mm comparable to semi-automatic
> segmentation but with ~4x faster execution (~ 1 min). Prospective
> intraoperative testing confirmed robust and consistent performance, with
> clinically acceptable accuracy for real-time surgical guidance.
>   Conclusion: Automatic 3D segmentation of CRLM in iUS using a cropped 3D U-Net
> provides reliable, near real-time results with minimal operator input. The
> method enables efficient, registration-free ultrasound-based navigation for
> hepatic surgery, approaching expert-level accuracy while substantially reducing
> manual workload and procedure time.

