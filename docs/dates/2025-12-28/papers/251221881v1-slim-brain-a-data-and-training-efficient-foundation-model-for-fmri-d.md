---
layout: default
title: SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis
---

# SLIM-Brain: A Data- and Training-Efficient Foundation Model for fMRI Data Analysis
**arXiv**：[2512.21881v1](https://arxiv.org/abs/2512.21881) · [PDF](https://arxiv.org/pdf/2512.21881.pdf)  
**作者**：Mo Wang, Junfeng Xia, Wenhao Ye, Enyu Liu, Kaining Peng, Jianfeng Feng, Quanying Liu, Hongkai Wen  

**一句话要点**：提出SLIM-Brain以解决fMRI分析中数据与训练效率的双重瓶颈

**关键词**：fMRI分析, 基础模型, 数据效率, 训练效率, 4D编码器, 自适应设计

## 3 点简述
- 当前fMRI基础模型面临数据维度高与训练资源消耗大的问题，图谱方法丢失细节，无图谱方法计算成本高。
- SLIM-Brain采用两阶段自适应设计：轻量时间提取器筛选关键窗口，4D分层编码器仅从选定窗口学习细粒度表示。
- 在七个公共基准测试中实现最优性能，预训练仅需4千会话，GPU内存使用减少约70%。

## 摘要（原文）

> Foundation models are emerging as a powerful paradigm for fMRI analysis, but current approaches face a dual bottleneck of data- and training-efficiency. Atlas-based methods aggregate voxel signals into fixed regions of interest, reducing data dimensionality but discarding fine-grained spatial details, and requiring extremely large cohorts to train effectively as general-purpose foundation models. Atlas-free methods, on the other hand, operate directly on voxel-level information - preserving spatial fidelity but are prohibitively memory- and compute-intensive, making large-scale pre-training infeasible. We introduce SLIM-Brain (Sample-efficient, Low-memory fMRI Foundation Model for Human Brain), a new atlas-free foundation model that simultaneously improves both data- and training-efficiency. SLIM-Brain adopts a two-stage adaptive design: (i) a lightweight temporal extractor captures global context across full sequences and ranks data windows by saliency, and (ii) a 4D hierarchical encoder (Hiera-JEPA) learns fine-grained voxel-level representations only from the top-$k$ selected windows, while deleting about 70% masked patches. Extensive experiments across seven public benchmarks show that SLIM-Brain establishes new state-of-the-art performance on diverse tasks, while requiring only 4 thousand pre-training sessions and approximately 30% of GPU memory comparing to traditional voxel-level methods.

