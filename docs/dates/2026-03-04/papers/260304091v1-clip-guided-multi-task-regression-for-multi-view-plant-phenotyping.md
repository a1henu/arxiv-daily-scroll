---
layout: default
title: CLIP-Guided Multi-Task Regression for Multi-View Plant Phenotyping
---

# CLIP-Guided Multi-Task Regression for Multi-View Plant Phenotyping
**arXiv**：[2603.04091v1](https://arxiv.org/abs/2603.04091) · [PDF](https://arxiv.org/pdf/2603.04091.pdf)  
**作者**：Simon Warmers, Muhammad Zawish, Fayaz Ali Dharejo, Steven Davy, Radu Timofte  

**一句话要点**：提出基于CLIP的多任务回归框架，以解决多视角植物表型分析中的视角冗余和外观变化问题。

**关键词**：多视角植物表型分析, CLIP嵌入, 多任务回归, 角度不变表示, 轻量文本先验, 鲁棒预测

## 3 点简述
- 核心问题：多视角植物图像存在视角冗余和视角依赖的外观变化，影响生长动态建模的鲁棒性。
- 方法要点：利用CLIP嵌入构建单模型，聚合旋转视角为角度不变表示，并结合轻量文本先验编码视角级别。
- 实验或效果：在GroMo25基准上，年龄和叶片数MAE分别降低49.5%和44.2%，简化流程并提升对缺失视角的鲁棒性。

## 摘要（原文）

> Modeling plant growth dynamics plays a central role in modern agricultural research. However, learning robust predictors from multi-view plant imagery remains challenging due to strong viewpoint redundancy and viewpoint-dependent appearance changes. We propose a level-aware vision language framework that jointly predicts plant age and leaf count using a single multi-task model built on CLIP embeddings. Our method aggregates rotational views into angle-invariant representations and conditions visual features on lightweight text priors encoding viewpoint level for stable prediction under incomplete or unordered inputs. On the GroMo25 benchmark, our approach reduces mean age MAE from 7.74 to 3.91 and mean leaf-count MAE from 5.52 to 3.08 compared to the GroMo baseline, corresponding to improvements of 49.5% and 44.2%, respectively. The unified formulation simplifies the pipeline by replacing the conventional dual-model setup while improving robustness to missing views. The models and code is available at: https://github.com/SimonWarmers/CLIP-MVP

