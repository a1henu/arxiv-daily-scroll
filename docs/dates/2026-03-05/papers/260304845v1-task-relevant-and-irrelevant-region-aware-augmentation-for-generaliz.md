---
layout: default
title: Task-Relevant and Irrelevant Region-Aware Augmentation for Generalizable Vision-Based Imitation Learning in Agricultural Manipulation
---

# Task-Relevant and Irrelevant Region-Aware Augmentation for Generalizable Vision-Based Imitation Learning in Agricultural Manipulation
**arXiv**：[2603.04845v1](https://arxiv.org/abs/2603.04845) · [PDF](https://arxiv.org/pdf/2603.04845.pdf)  
**作者**：Shun Hattori, Hikaru Sasaki, Takumi Hachimine, Yusuke Mizutani, Takamitsu Matsubara  

**一句话要点**：提出DRAIL区域感知增强框架，以提升农业机器人视觉模仿学习的泛化能力

**关键词**：视觉模仿学习, 农业机器人, 数据增强, 泛化能力, 区域感知, 扩散策略

## 3 点简述
- 核心问题：农业视觉模仿学习因数据稀缺和作物外观、背景变化导致泛化受限
- 方法要点：DRAIL分离任务相关与无关区域，分别进行知识驱动增强和随机化处理
- 实验或效果：在蔬菜收获和生菜采摘任务中，DRAIL在未见视觉条件下提升成功率

## 摘要（原文）

> Vision-based imitation learning has shown promise for robotic manipulation; however, its generalization remains limited in practical agricultural tasks. This limitation stems from scarce demonstration data and substantial visual domain gaps caused by i) crop-specific appearance diversity and ii) background variations. To address this limitation, we propose Dual-Region Augmentation for Imitation Learning (DRAIL), a region-aware augmentation framework designed for generalizable vision-based imitation learning in agricultural manipulation. DRAIL explicitly separates visual observations into task-relevant and task-irrelevant regions. The task-relevant region is augmented in a domain-knowledge-driven manner to preserve essential visual characteristics, while the task-irrelevant region is aggressively randomized to suppress spurious background correlations. By jointly handling both sources of visual variation, DRAIL promotes learning policies that rely on task-essential features rather than incidental visual cues. We evaluate DRAIL on diffusion policy-based visuomotor controllers through robot experiments on artificial vegetable harvesting and real lettuce defective leaf picking preparation tasks. The results show consistent improvements in success rates under unseen visual conditions compared to baseline methods. Further attention analysis and representation generalization metrics indicate that the learned policies rely more on task-essential visual features, resulting in enhanced robustness and generalization.

