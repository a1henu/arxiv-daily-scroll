---
layout: default
title: A data- and compute-efficient chest X-ray foundation model beyond aggressive scaling
---

# A data- and compute-efficient chest X-ray foundation model beyond aggressive scaling
**arXiv**：[2602.22843v1](https://arxiv.org/abs/2602.22843) · [PDF](https://arxiv.org/pdf/2602.22843.pdf)  
**作者**：Chong Wang, Yabin Zhang, Yunhe Gao, Maya Varma, Clemence Mottez, Faidra Patsatzi, Jiaming Liu, Jin Long, Jean-Benoit Delbrouck, Sergios Gatidis, Akshay S. Chaudhari, Curtis P. Langlotz  

**一句话要点**：提出CheXficient胸片基础模型，通过主动数据筛选实现高效预训练，替代盲目扩大数据集。

**关键词**：医学影像基础模型, 数据筛选, 计算效率, 胸片分析, 多任务评估, 长尾学习

## 3 点简述
- 核心问题：大规模医学影像数据集存在冗余和类别不平衡，导致计算效率低和表示学习偏差。
- 方法要点：在预训练中主动筛选信息丰富的训练样本，仅使用22.7%的数据和27.3%的计算资源。
- 实验或效果：在20个基准测试中表现可比或优于全数据模型，提升长尾或罕见条件的泛化能力。

## 摘要（原文）

> Foundation models for medical imaging are typically pretrained on increasingly large datasets, following a "scale-at-all-costs" paradigm. However, this strategy faces two critical challenges: large-scale medical datasets often contain substantial redundancy and severe class imbalance that bias representation learning toward over-represented patterns, and indiscriminate training regardless of heterogeneity in data quality incurs considerable computational inefficiency. Here we demonstrate that active, principled data curation during pretraining can serve as a viable, cost-effective alternative to brute-force dataset enlargement. We introduce CheXficient, a chest X-ray (CXR) foundation model that selectively prioritizes informative training samples. CheXficient is pretrained on only 22.7% of 1,235,004 paired CXR images and reports while consuming under 27.3% of the total compute budget, yet achieving comparable or superior performance to its full-data counterpart and other large-scale pretrained models. We assess CheXficient across 20 individual benchmarks spanning 5 task types, including non-adapted off-the-shelf evaluations (zero-shot findings classification and crossmodal retrieval) and adapted downstream tasks (disease prediction, semantic segmentation, and radiology report generation). Further analyses show that CheXficient systematically prioritizes under-represented training samples, improving generalizability on long-tailed or rare conditions. Overall, our work offers practical insights into the data and computation demands for efficient pretraining and downstream adaptation of medical vision-language foundation models.

