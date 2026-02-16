---
layout: default
title: 3DLAND: 3D Lesion Abdominal Anomaly Localization Dataset
---

# 3DLAND: 3D Lesion Abdominal Anomaly Localization Dataset
**arXiv**：[2602.12820v1](https://arxiv.org/abs/2602.12820) · [PDF](https://arxiv.org/pdf/2602.12820.pdf)  
**作者**：Mehran Advand, Zahra Dehghanian, Navid Faraji, Reza Barati, Seyed Amir Ahmad Safavi-Naini, Hamid R. Rabiee  

**一句话要点**：提出3DLAND数据集以解决腹部CT三维标注不足问题，支持多器官病变定位与AI评估。

**关键词**：三维医学影像, 腹部病变定位, 多器官分割, 数据集构建, 异常检测, 迁移学习

## 3 点简述
- 现有腹部CT数据集缺乏三维标注和多器官覆盖，阻碍AI模型学习与应用。
- 通过自动化空间推理、提示优化2D分割和记忆引导3D传播构建大规模三维病变数据集。
- 数据集包含6000+CT体积和20000+三维标注，经专家验证表面骰子分数超0.75，支持异常检测和跨器官迁移学习。

## 摘要（原文）

> Existing medical imaging datasets for abdominal CT often lack three-dimensional annotations, multi-organ coverage, or precise lesion-to-organ associations, hindering robust representation learning and clinical applications. To address this gap, we introduce 3DLAND, a large-scale benchmark dataset comprising over 6,000 contrast-enhanced CT volumes with over 20,000 high-fidelity 3D lesion annotations linked to seven abdominal organs: liver, kidneys, pancreas, spleen, stomach, and gallbladder. Our streamlined three-phase pipeline integrates automated spatial reasoning, prompt-optimized 2D segmentation, and memory-guided 3D propagation, validated by expert radiologists with surface dice scores exceeding 0.75. By providing diverse lesion types and patient demographics, 3DLAND enables scalable evaluation of anomaly detection, localization, and cross-organ transfer learning for medical AI. Our dataset establishes a new benchmark for evaluating organ-aware 3D segmentation models, paving the way for advancements in healthcare-oriented AI. To facilitate reproducibility and further research, the 3DLAND dataset and implementation code are publicly available at https://mehrn79.github.io/3DLAND.

