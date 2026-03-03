---
layout: default
title: Robust White Blood Cell Classification with Stain-Normalized Decoupled Learning and Ensembling
---

# Robust White Blood Cell Classification with Stain-Normalized Decoupled Learning and Ensembling
**arXiv**：[2603.01976v1](https://arxiv.org/abs/2603.01976) · [PDF](https://arxiv.org/pdf/2603.01976.pdf)  
**作者**：Luu Le, Hoang-Loc Cao, Ha-Hieu Pham, Thanh-Huy Nguyen, Ulas Bagci  

**一句话要点**：提出染色归一化解耦学习与集成方法，以解决白细胞分类中的染色变异和类别不平衡问题。

**关键词**：白细胞分类, 染色归一化, 解耦学习, 类别不平衡, 集成方法, 测试时增强

## 3 点简述
- 核心问题：白细胞分类面临染色和扫描条件导致的显著外观变异，以及常见细胞类型主导、罕见类别不足的严重类别不平衡。
- 方法要点：采用染色归一化解耦训练框架，先通过实例平衡采样学习可迁移表示，再用类别感知采样和混合损失重新平衡分类器。
- 实验或效果：在WBCBench 2026挑战赛中取得领先排名，通过测试时增强集成多种训练骨干网络增强鲁棒性。

## 摘要（原文）

> White blood cell (WBC) classification is fundamental for hematology applications such as infection assessment, leukemia screening, and treatment monitoring. However, real-world WBC datasets present substantial appearance variations caused by staining and scanning conditions, as well as severe class imbalance in which common cell types dominate while rare but clinically important categories are underrepresented. To address these challenges, we propose a stain-normalized, decoupled training framework that first learns transferable representations using instance-balanced sampling, and then rebalances the classifier with class-aware sampling and a hybrid loss combining effective-number weighting and focal modulation. In inference stage, we further enhance robustness by ensembling various trained backbones with test-time augmentation. Our approach achieved the top rank on the leaderboard of the WBCBench 2026: Robust White Blood Cell Classification Challenge at ISBI 2026.

