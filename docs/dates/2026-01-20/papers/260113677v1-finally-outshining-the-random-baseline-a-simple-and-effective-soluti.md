---
layout: default
title: Finally Outshining the Random Baseline: A Simple and Effective Solution for Active Learning in 3D Biomedical Imaging
---

# Finally Outshining the Random Baseline: A Simple and Effective Solution for Active Learning in 3D Biomedical Imaging
**arXiv**：[2601.13677v1](https://arxiv.org/abs/2601.13677) · [PDF](https://arxiv.org/pdf/2601.13677.pdf)  
**作者**：Carsten T. Lüth, Jeremias Traub, Kim-Celine Kahl, Till J. Bungert, Lukas Klein, Lars Krämer, Paul F. Jäger, Klaus Maier-Hein, Fabian Isensee  

**一句话要点**：提出ClaSP PE方法以解决3D生物医学图像分割中主动学习性能不足的问题

**关键词**：主动学习, 3D生物医学图像分割, 类分层查询, 功率噪声, 标注效率, 泛化能力

## 3 点简述
- 核心问题：现有主动学习方法在3D生物医学图像分割中无法稳定超越改进的随机采样基线，导致标注成本高
- 方法要点：结合类分层查询和带衰减调度的对数尺度功率噪声，以处理类别不平衡和早期选择冗余
- 实验或效果：在24个实验设置中，ClaSP PE是唯一在分割质量和标注效率上显著优于基线的策略，且能泛化到未知数据集

## 摘要（原文）

> Active learning (AL) has the potential to drastically reduce annotation costs in 3D biomedical image segmentation, where expert labeling of volumetric data is both time-consuming and expensive. Yet, existing AL methods are unable to consistently outperform improved random sampling baselines adapted to 3D data, leaving the field without a reliable solution. We introduce Class-stratified Scheduled Power Predictive Entropy (ClaSP PE), a simple and effective query strategy that addresses two key limitations of standard uncertainty-based AL methods: class imbalance and redundancy in early selections. ClaSP PE combines class-stratified querying to ensure coverage of underrepresented structures and log-scale power noising with a decaying schedule to enforce query diversity in early-stage AL and encourage exploitation later. In our evaluation on 24 experimental settings using four 3D biomedical datasets within the comprehensive nnActive benchmark, ClaSP PE is the only method that generally outperforms improved random baselines in terms of both segmentation quality with statistically significant gains, whilst remaining annotation efficient. Furthermore, we explicitly simulate the real-world application by testing our method on four previously unseen datasets without manual adaptation, where all experiment parameters are set according to predefined guidelines. The results confirm that ClaSP PE robustly generalizes to novel tasks without requiring dataset-specific tuning. Within the nnActive framework, we present compelling evidence that an AL method can consistently outperform random baselines adapted to 3D segmentation, in terms of both performance and annotation efficiency in a realistic, close-to-production scenario. Our open-source implementation and clear deployment guidelines make it readily applicable in practice. Code is at https://github.com/MIC-DKFZ/nnActive.

