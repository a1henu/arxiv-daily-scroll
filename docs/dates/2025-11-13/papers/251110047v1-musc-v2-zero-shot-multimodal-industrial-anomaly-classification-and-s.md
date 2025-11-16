---
layout: default
title: MuSc-V2: Zero-Shot Multimodal Industrial Anomaly Classification and Segmentation with Mutual Scoring of Unlabeled Samples
---

# MuSc-V2: Zero-Shot Multimodal Industrial Anomaly Classification and Segmentation with Mutual Scoring of Unlabeled Samples
**arXiv**：[2511.10047v1](https://arxiv.org/abs/2511.10047) · [PDF](https://arxiv.org/pdf/2511.10047.pdf)  
**作者**：Xurui Li, Feng Xue, Yu Zhou  

**一句话要点**：提出MuSc-V2框架，通过样本互评分实现零样本工业异常分类与分割

**关键词**：零样本学习, 异常检测, 多模态融合, 工业视觉, 互评分机制, 3D表示学习

## 3 点简述
- 核心问题：零样本异常分类与分割中，正常图像块相似而异常块孤立，现有方法未充分利用此特性
- 方法要点：结合2D/3D模态，使用互评分机制和跨模态增强，提升特征判别力
- 实验或效果：在MVTec 3D-AD和Eyecandies数据集上AP分别提升23.7%和19.3%，超越零样本基准

## 摘要（原文）

> Zero-shot anomaly classification (AC) and segmentation (AS) methods aim to identify and outline defects without using any labeled samples. In this paper, we reveal a key property that is overlooked by existing methods: normal image patches across industrial products typically find many other similar patches, not only in 2D appearance but also in 3D shapes, while anomalies remain diverse and isolated. To explicitly leverage this discriminative property, we propose a Mutual Scoring framework (MuSc-V2) for zero-shot AC/AS, which flexibly supports single 2D/3D or multimodality. Specifically, our method begins by improving 3D representation through Iterative Point Grouping (IPG), which reduces false positives from discontinuous surfaces. Then we use Similarity Neighborhood Aggregation with Multi-Degrees (SNAMD) to fuse 2D/3D neighborhood cues into more discriminative multi-scale patch features for mutual scoring. The core comprises a Mutual Scoring Mechanism (MSM) that lets samples within each modality to assign score to each other, and Cross-modal Anomaly Enhancement (CAE) that fuses 2D and 3D scores to recover modality-specific missing anomalies. Finally, Re-scoring with Constrained Neighborhood (RsCon) suppresses false classification based on similarity to more representative samples. Our framework flexibly works on both the full dataset and smaller subsets with consistently robust performance, ensuring seamless adaptability across diverse product lines. In aid of the novel framework, MuSc-V2 achieves significant performance improvements: a $\textbf{+23.7\%}$ AP gain on the MVTec 3D-AD dataset and a $\textbf{+19.3\%}$ boost on the Eyecandies dataset, surpassing previous zero-shot benchmarks and even outperforming most few-shot methods. The code will be available at The code will be available at \href{https://github.com/HUST-SLOW/MuSc-V2}{https://github.com/HUST-SLOW/MuSc-V2}.

