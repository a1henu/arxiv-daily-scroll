---
layout: default
title: Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks
---

# Fine-grained Image Aesthetic Assessment: Learning Discriminative Scores from Relative Ranks
**arXiv**：[2603.03907v1](https://arxiv.org/abs/2603.03907) · [PDF](https://arxiv.org/pdf/2603.03907.pdf)  
**作者**：Zhichao Yang, Jianjie Wang, Zhixianhe Zhang, Pangu Xie, Xiangfei Sheng, Pengfei Chen, Leida Li  

**一句话要点**：提出FGAesQ框架以解决细粒度图像美学评估问题，通过相对排名学习判别性分数。

**关键词**：细粒度图像美学评估, 相对排名学习, FGAesthetics数据库, FGAesQ框架, 美学分数判别

## 3 点简述
- 核心问题：现有图像美学评估模型难以区分美学差异细微的图像，限制了在细粒度场景中的应用。
- 方法要点：基于FGAesthetics数据库，设计DiffToken、CTAlign和RankReg模块，从相对排名中学习判别性美学分数。
- 实验或效果：在细粒度评估中表现优异，同时在粗粒度评估中保持竞争力，验证了方法的优越性。

## 摘要（原文）

> Image aesthetic assessment (IAA) has extensive applications in content creation, album management, and recommendation systems, etc. In such applications, it is commonly needed to pick out the most aesthetically pleasing image from a series of images with subtle aesthetic variations, a topic we refer to as fine-grained IAA. Unfortunately, state-of-the-art IAA models are typically designed for coarse-grained evaluation, where images with notable aesthetic differences are evaluated independently on an absolute scale. These models are inherently limited in discriminating fine-grained aesthetic differences. To address the dilemma, we contribute FGAesthetics, a fine-grained IAA database with 32,217 images organized into 10,028 series, which are sourced from diverse categories including Natural, AIGC, and Cropping. Annotations are collected via pairwise comparisons within each series. We also devise Series Refinement and Rank Calibration to ensure the reliability of data and labels. Based on FGAesthetics, we further propose FGAesQ, a novel IAA framework that learns discriminative aesthetic scores from relative ranks through Difference-preserved Tokenization (DiffToken), Comparative Text-assisted Alignment (CTAlign), and Rank-aware Regression (RankReg). FGAesQ enables accurate aesthetic assessment in fine-grained scenarios while still maintains competitive performance in coarse-grained evaluation. Extensive experiments and comparisons demonstrate the superiority of the proposed method.

