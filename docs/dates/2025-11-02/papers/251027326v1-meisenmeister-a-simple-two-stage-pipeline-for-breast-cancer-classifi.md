---
layout: default
title: MeisenMeister: A Simple Two Stage Pipeline for Breast Cancer Classification on MRI
---

# MeisenMeister: A Simple Two Stage Pipeline for Breast Cancer Classification on MRI
**arXiv**：[2510.27326v1](https://arxiv.org/abs/2510.27326) · [PDF](https://arxiv.org/pdf/2510.27326.pdf)  
**作者**：Benjamin Hamm, Yannick Kirchhoff, Maximilian Rokuss, Klaus Maier-Hein  

**一句话要点**：提出MeisenMeister两阶段管道以改进乳腺癌MRI分类

**关键词**：乳腺癌分类, MRI分析, 两阶段管道, 稳健分类方法, 公开实现

## 3 点简述
- 核心问题：乳腺癌MRI检测因高质量分割标签稀缺而具挑战性
- 方法要点：采用基于分类的两阶段管道，强调稳健性和临床相关性
- 实验或效果：通过迭代开发优化性能，公开实现代码供验证

## 摘要（原文）

> The ODELIA Breast MRI Challenge 2025 addresses a critical issue in breast
> cancer screening: improving early detection through more efficient and accurate
> interpretation of breast MRI scans. Even though methods for general-purpose
> whole-body lesion segmentation as well as multi-time-point analysis exist,
> breast cancer detection remains highly challenging, largely due to the limited
> availability of high-quality segmentation labels. Therefore, developing robust
> classification-based approaches is crucial for the future of early breast
> cancer detection, particularly in applications such as large-scale screening.
> In this write-up, we provide a comprehensive overview of our approach to the
> challenge. We begin by detailing the underlying concept and foundational
> assumptions that guided our work. We then describe the iterative development
> process, highlighting the key stages of experimentation, evaluation, and
> refinement that shaped the evolution of our solution. Finally, we present the
> reasoning and evidence that informed the design choices behind our final
> submission, with a focus on performance, robustness, and clinical relevance. We
> release our full implementation publicly at
> https://github.com/MIC-DKFZ/MeisenMeister

