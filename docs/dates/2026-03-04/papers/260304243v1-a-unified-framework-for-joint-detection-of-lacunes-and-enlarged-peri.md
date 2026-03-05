---
layout: default
title: A Unified Framework for Joint Detection of Lacunes and Enlarged Perivascular Spaces
---

# A Unified Framework for Joint Detection of Lacunes and Enlarged Perivascular Spaces
**arXiv**：[2603.04243v1](https://arxiv.org/abs/2603.04243) · [PDF](https://arxiv.org/pdf/2603.04243.pdf)  
**作者**：Lucas He, Krinos Li, Hanyuan Zhang, Runlong He, Silvia Ingala, Luigi Lorenzini, Marleen de Bruijne, Frederik Barkhof, Rhodri Davies, Carole Sudre  

**一句话要点**：提出形态解耦框架以联合检测脑小血管病标志物，解决特征干扰和类别不平衡问题。

**关键词**：医学影像分析, 脑小血管病检测, 形态解耦框架, 跨任务注意力, 混合监督学习, 解剖推理校准

## 3 点简述
- 核心问题：脑小血管病标志物EPVS和腔隙在医学影像中相似，标准分割网络面临特征干扰和极端类别不平衡。
- 方法要点：采用零初始化门控跨任务注意力，利用密集EPVS上下文指导稀疏腔隙检测，并通过混合监督策略增强生物拓扑一致性。
- 实验或效果：在VALDO 2021数据集上验证，腔隙检测精度达71.1%，F1分数62.6%，优于现有方法，并在外部EPAD队列中展示鲁棒性。

## 摘要（原文）

> Cerebral small vessel disease (CSVD) markers, specifically enlarged perivascular spaces (EPVS) and lacunae, present a unique challenge in medical image analysis due to their radiological mimicry. Standard segmentation networks struggle with feature interference and extreme class imbalance when handling these divergent targets simultaneously. To address these issues, we propose a morphology-decoupled framework where Zero-Initialized Gated Cross-Task Attention exploits dense EPVS context to guide sparse lacune detection. Furthermore, biological and topological consistency are enforced via a mixed-supervision strategy integrating Mutual Exclusion and Centerline Dice losses. Finally, we introduce an Anatomically-Informed Inference Calibration mechanism to dynamically suppress false positives based on tissue semantics. Extensive 5-folds cross-validation on the VALDO 2021 dataset (N=40) demonstrates state-of-the-art performance, notably surpassing task winners in lacunae detection precision (71.1%, p=0.01) and F1-score (62.6%, p=0.03). Furthermore, evaluation on the external EPAD cohort (N=1762) confirms the model's robustness for large-scale population studies. Code will be released upon acceptance.

