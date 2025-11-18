---
layout: default
title: Adaptive Multi-Scale Integration Unlocks Robust Cell Annotation in Histopathology Images
---

# Adaptive Multi-Scale Integration Unlocks Robust Cell Annotation in Histopathology Images
**arXiv**：[2511.13586v1](https://arxiv.org/abs/2511.13586) · [PDF](https://arxiv.org/pdf/2511.13586.pdf)  
**作者**：Yinuo Xu, Yan Cui, Mingyao Li, Zhi Huang  

**一句话要点**：提出NuClass框架以解决组织病理图像中细胞注释的鲁棒性问题

**关键词**：细胞注释, 多尺度集成, 不确定性引导, 组织病理图像, 空间转录组学

## 3 点简述
- 核心问题：现有模型难以整合细胞核形态与组织上下文，且细粒度标注稀缺。
- 方法要点：通过多尺度集成和不确定性引导，自适应融合局部与全局特征。
- 实验或效果：在三个独立队列中，最佳类别F1达96%，优于基线方法。

## 摘要（原文）

> Identifying cell types and subtypes from routine histopathology images is essential for improving the computational understanding of human disease. Existing tile-based models can capture detailed nuclear morphology but often fail to incorporate the broader tissue context that influences a cell's function and identity. In addition, available human annotations are typically coarse-grained and unevenly distributed across studies, making fine-grained subtype-level supervision difficult to obtain.
>   To address these limitations, we introduce NuClass, a pathologist workflow inspired framework for cell-wise multi-scale integration of nuclear morphology and microenvironmental context. NuClass includes two main components: Path local, which focuses on nuclear morphology from 224-by-224 pixel crops, and Path global, which models the surrounding 1024-by-1024 pixel neighborhood. A learnable gating module adaptively balances local detail and contextual cues. To encourage complementary learning, we incorporate an uncertainty-guided objective that directs the global path to prioritize regions where the local path is uncertain. We also provide calibrated confidence estimates and Grad-CAM visualizations to enhance interpretability.
>   To overcome the lack of high-quality annotations, we construct a marker-guided dataset from Xenium spatial transcriptomics assays, yielding single-cell resolution labels for more than two million cells across eight organs and 16 classes. Evaluated on three fully held-out cohorts, NuClass achieves up to 96 percent F1 for its best-performing class, outperforming strong baselines. Our results show that multi-scale, uncertainty-aware fusion can bridge the gap between slide-level pathological foundation models and reliable, cell-level phenotype prediction.

