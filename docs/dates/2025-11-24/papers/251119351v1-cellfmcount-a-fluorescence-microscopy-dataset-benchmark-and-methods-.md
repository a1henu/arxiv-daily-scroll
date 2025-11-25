---
layout: default
title: CellFMCount: A Fluorescence Microscopy Dataset, Benchmark, and Methods for Cell Counting
---

# CellFMCount: A Fluorescence Microscopy Dataset, Benchmark, and Methods for Cell Counting
**arXiv**：[2511.19351v1](https://arxiv.org/abs/2511.19351) · [PDF](https://arxiv.org/pdf/2511.19351.pdf)  
**作者**：Abdurahman Ali Mohammed, Catherine Fonder, Ying Wei, Wallapak Tavanapong, Donald S Sakaguchi, Qi Li, Surya K. Mallapragada  

**一句话要点**：提出CellFMCount数据集与SAM-Counter方法以解决荧光显微镜细胞计数难题

**关键词**：细胞计数, 荧光显微镜数据集, 密度图方法, SAM模型适配, 基准测试

## 3 点简述
- 细胞计数在生物医学中关键但手动计数费时易错，需自动化方法
- 引入大规模数据集和基准测试，并适配SAM模型用于细胞计数
- SAM-Counter方法在测试集上MAE为22.12，优于现有方法

## 摘要（原文）

> Accurate cell counting is essential in various biomedical research and clinical applications, including cancer diagnosis, stem cell research, and immunology. Manual counting is labor-intensive and error-prone, motivating automation through deep learning techniques. However, training reliable deep learning models requires large amounts of high-quality annotated data, which is difficult and time-consuming to produce manually. Consequently, existing cell-counting datasets are often limited, frequently containing fewer than $500$ images. In this work, we introduce a large-scale annotated dataset comprising $3{,}023$ images from immunocytochemistry experiments related to cellular differentiation, containing over $430{,}000$ manually annotated cell locations. The dataset presents significant challenges: high cell density, overlapping and morphologically diverse cells, a long-tailed distribution of cell count per image, and variation in staining protocols. We benchmark three categories of existing methods: regression-based, crowd-counting, and cell-counting techniques on a test set with cell counts ranging from $10$ to $2{,}126$ cells per image. We also evaluate how the Segment Anything Model (SAM) can be adapted for microscopy cell counting using only dot-annotated datasets. As a case study, we implement a density-map-based adaptation of SAM (SAM-Counter) and report a mean absolute error (MAE) of $22.12$, which outperforms existing approaches (second-best MAE of $27.46$). Our results underscore the value of the dataset and the benchmarking framework for driving progress in automated cell counting and provide a robust foundation for future research and development.

