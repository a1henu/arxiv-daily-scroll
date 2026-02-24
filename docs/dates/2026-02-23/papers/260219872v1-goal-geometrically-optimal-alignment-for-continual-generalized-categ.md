---
layout: default
title: GOAL: Geometrically Optimal Alignment for Continual Generalized Category Discovery
---

# GOAL: Geometrically Optimal Alignment for Continual Generalized Category Discovery
**arXiv**：[2602.19872v1](https://arxiv.org/abs/2602.19872) · [PDF](https://arxiv.org/pdf/2602.19872.pdf)  
**作者**：Jizhou Han, Chenhao Ding, SongLin Dong, Yuhang He, Shaokun Wang, Qiang Wang, Yihong Gong  

**一句话要点**：提出GOAL框架，通过固定ETF分类器解决持续广义类别发现中的遗忘与特征对齐不一致问题。

**关键词**：持续广义类别发现, 等角紧框架分类器, 特征对齐, 遗忘减少, 新类别发现

## 3 点简述
- 核心问题：持续广义类别发现中动态更新分类器导致遗忘和特征对齐不一致。
- 方法要点：引入固定等角紧框架分类器，结合监督对齐和置信度引导对齐，稳定整合新类别。
- 实验或效果：在四个基准测试中优于Happy方法，减少遗忘16.1%，提升新类别发现3.2%。

## 摘要（原文）

> Continual Generalized Category Discovery (C-GCD) requires identifying novel classes from unlabeled data while retaining knowledge of known classes over time. Existing methods typically update classifier weights dynamically, resulting in forgetting and inconsistent feature alignment. We propose GOAL, a unified framework that introduces a fixed Equiangular Tight Frame (ETF) classifier to impose a consistent geometric structure throughout learning. GOAL conducts supervised alignment for labeled samples and confidence-guided alignment for novel samples, enabling stable integration of new classes without disrupting old ones. Experiments on four benchmarks show that GOAL outperforms the prior method Happy, reducing forgetting by 16.1% and boosting novel class discovery by 3.2%, establishing a strong solution for long-horizon continual discovery.

