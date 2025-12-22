---
layout: default
title: MGRegBench: A Novel Benchmark Dataset with Anatomical Landmarks for Mammography Image Registration
---

# MGRegBench: A Novel Benchmark Dataset with Anatomical Landmarks for Mammography Image Registration
**arXiv**：[2512.17605v1](https://arxiv.org/abs/2512.17605) · [PDF](https://arxiv.org/pdf/2512.17605.pdf)  
**作者**：Svetlana Krasnova, Emiliya Starikova, Ilia Naletov, Andrey Krylov, Dmitry Sorokin  

**一句话要点**：提出MGRegBench基准数据集以解决乳腺X光图像配准缺乏公开数据和标准化评估的问题。

**关键词**：乳腺X光配准, 基准数据集, 图像配准, 深度学习, 医学图像分析, 公开数据

## 3 点简述
- 核心问题：乳腺X光配准因缺乏公开数据集和标准化基准而进展受限，现有研究使用私有数据且评估不一致。
- 方法要点：发布包含5000多对图像、100对带手动解剖标志和分割掩码的公开数据集，支持多种配准方法的公平比较。
- 实验或效果：基准测试了经典、学习基、隐式神经表示和最新深度学习方法，提供代码和数据以促进未来研究。

## 摘要（原文）

> Robust mammography registration is essential for clinical applications like tracking disease progression and monitoring longitudinal changes in breast tissue. However, progress has been limited by the absence of public datasets and standardized benchmarks. Existing studies are often not directly comparable, as they use private data and inconsistent evaluation frameworks. To address this, we present MGRegBench, a public benchmark dataset for mammogram registration. It comprises over 5,000 image pairs, with 100 containing manual anatomical landmarks and segmentation masks for rigorous evaluation. This makes MGRegBench one of the largest public 2D registration datasets with manual annotations. Using this resource, we benchmarked diverse registration methods including classical (ANTs), learning-based (VoxelMorph, TransMorph), implicit neural representation (IDIR), a classic mammography-specific approach, and a recent state-of-the-art deep learning method MammoRegNet. The implementations were adapted to this modality from the authors' implementations or re-implemented from scratch. Our contributions are: (1) the first public dataset of this scale with manual landmarks and masks for mammography registration; (2) the first like-for-like comparison of diverse methods on this modality; and (3) an extensive analysis of deep learning-based registration. We publicly release our code and data to establish a foundational resource for fair comparisons and catalyze future research. The source code and data are at https://github.com/KourtKardash/MGRegBench.

