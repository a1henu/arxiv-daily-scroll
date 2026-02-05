---
layout: default
title: Training Data Efficiency in Multimodal Process Reward Models
---

# Training Data Efficiency in Multimodal Process Reward Models
**arXiv**：[2602.04145v1](https://arxiv.org/abs/2602.04145) · [PDF](https://arxiv.org/pdf/2602.04145.pdf)  
**作者**：Jinyuan Li, Chengsong Huang, Langlin Huang, Shaoyang Xu, Haolin Liu, Wenxuan Zhang, Jiaxin Huang  

**一句话要点**：提出平衡信息分数以提升多模态过程奖励模型的数据效率

**关键词**：多模态过程奖励模型, 数据效率, 训练数据选择, 视觉推理, 蒙特卡洛标注

## 3 点简述
- 核心问题：MPRM训练依赖大规模蒙特卡洛标注数据，成本高昂且存在冗余
- 方法要点：基于标签混合与可靠性理论，设计BIS优先选择信息丰富的训练样本
- 实验或效果：在10%数据下达到全数据性能，相对随机采样提升4.1%

## 摘要（原文）

> Multimodal Process Reward Models (MPRMs) are central to step-level supervision for visual reasoning in MLLMs. Training MPRMs typically requires large-scale Monte Carlo (MC)-annotated corpora, incurring substantial training cost. This paper studies the data efficiency for MPRM training.Our preliminary experiments reveal that MPRM training quickly saturates under random subsampling of the training data, indicating substantial redundancy within existing MC-annotated corpora.To explain this, we formalize a theoretical framework and reveal that informative gradient updates depend on two factors: label mixtures of positive/negative steps and label reliability (average MC scores of positive steps). Guided by these insights, we propose the Balanced-Information Score (BIS), which prioritizes both mixture and reliability based on existing MC signals at the rollout level, without incurring any additional cost. Across two backbones (InternVL2.5-8B and Qwen2.5-VL-7B) on VisualProcessBench, BIS-selected subsets consistently match and even surpass the full-data performance at small fractions. Notably, the BIS subset reaches full-data performance using only 10% of the training data, improving over random subsampling by a relative 4.1%.

