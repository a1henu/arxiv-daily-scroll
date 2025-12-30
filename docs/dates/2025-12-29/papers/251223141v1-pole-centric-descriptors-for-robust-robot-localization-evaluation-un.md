---
layout: default
title: Pole-centric Descriptors for Robust Robot Localization: Evaluation under Pole-at-Distance (PaD) Observations using the Small Pole Landmark (SPL) Dataset
---

# Pole-centric Descriptors for Robust Robot Localization: Evaluation under Pole-at-Distance (PaD) Observations using the Small Pole Landmark (SPL) Dataset
**arXiv**：[2512.23141v1](https://arxiv.org/abs/2512.23141) · [PDF](https://arxiv.org/pdf/2512.23141.pdf)  
**作者**：Wuhao Xie, Kanji Tanaka  

**一句话要点**：提出基于小杆地标数据集的评估框架，以提升远距离杆状结构在机器人定位中的描述符鲁棒性。

**关键词**：机器人定位, 杆状地标, 描述符鲁棒性, 对比学习, 小杆地标数据集, 远距离观测

## 3 点简述
- 核心问题：远距离杆状结构观测导致机器人定位中地标识别可靠性下降。
- 方法要点：构建自动化跟踪关联的小杆地标数据集，用于系统评估描述符鲁棒性。
- 实验或效果：对比学习在稀疏几何特征空间中表现更优，尤其在5-10米范围内检索性能突出。

## 摘要（原文）

> While pole-like structures are widely recognized as stable geometric anchors for long-term robot localization, their identification reliability degrades significantly under Pole-at-Distance (Pad) observations typical of large-scale urban environments. This paper shifts the focus from descriptor design to a systematic investigation of descriptor robustness. Our primary contribution is the establishment of a specialized evaluation framework centered on the Small Pole Landmark (SPL) dataset. This dataset is constructed via an automated tracking-based association pipeline that captures multi-view, multi-distance observations of the same physical landmarks without manual annotation. Using this framework, we present a comparative analysis of Contrastive Learning (CL) and Supervised Learning (SL) paradigms. Our findings reveal that CL induces a more robust feature space for sparse geometry, achieving superior retrieval performance particularly in the 5--10m range. This work provides an empirical foundation and a scalable methodology for evaluating landmark distinctiveness in challenging real-world scenarios.

