---
layout: default
title: Safe Multitask Molecular Graph Networks for Vapor Pressure and Odor Threshold Prediction
---

# Safe Multitask Molecular Graph Networks for Vapor Pressure and Odor Threshold Prediction
**arXiv**：[2601.16426v1](https://arxiv.org/abs/2601.16426) · [PDF](https://arxiv.org/pdf/2601.16426.pdf)  
**作者**：Shuang Wu, Meijie Wang, Lun Yu  

**一句话要点**：提出安全多任务分子图网络，用于预测蒸汽压和气味阈值，提升泛化性能。

**关键词**：分子图网络, 多任务学习, 蒸汽压预测, 气味阈值预测, 分布外泛化, A20/E17特征

## 3 点简述
- 研究蒸汽压和气味阈值预测，采用Bemis-Murcko骨架分割评估模型分布外能力。
- 引入A20/E17分子图特征，比较GINE和PNA骨干，PNA在蒸汽压任务中表现更优。
- 提出安全多任务方法，以蒸汽压为主任务，避免损害主任务，同时获得最佳泛化效果。

## 摘要（原文）

> We investigate two important tasks in odor-related property modeling: Vapor Pressure (VP) and Odor Threshold (OP). To evaluate the model's out-of-distribution (OOD) capability, we adopt the Bemis-Murcko scaffold split. In terms of features, we introduce the rich A20/E17 molecular graph features (20-dimensional atom features + 17-dimensional bond features) and systematically compare GINE and PNA backbones. The results show: for VP, PNA with a simple regression head achieves Val MSE $\approx$ 0.21 (normalized space); for the OP single task under the same scaffold split, using A20/E17 with robust training (Huber/winsor) achieves Val MSE $\approx$ 0.60-0.61. For multitask training, we propose a **"safe multitask"** approach: VP as the primary task and OP as the auxiliary task, using delayed activation + gradient clipping + small weight, which avoids harming the primary task and simultaneously yields the best VP generalization performance. This paper provides complete reproducible experiments, ablation studies, and error-similarity analysis while discussing the impact of data noise and method limitations.

