---
layout: default
title: Breaking Robustness Barriers in Cognitive Diagnosis: A One-Shot Neural Architecture Search Perspective
---

# Breaking Robustness Barriers in Cognitive Diagnosis: A One-Shot Neural Architecture Search Perspective
**arXiv**：[2601.04918v1](https://arxiv.org/abs/2601.04918) · [PDF](https://arxiv.org/pdf/2601.04918.pdf)  
**作者**：Ziwen Wang, Shangshang Yang, Xiaoshan Yu, Haiping Ma, Xingyi Zhang  

**一句话要点**：提出OSCD方法，通过一次性神经架构搜索提升认知诊断模型的鲁棒性

**关键词**：认知诊断, 神经架构搜索, 多目标优化, 鲁棒性, 智能辅导系统

## 3 点简述
- 核心问题：现有认知诊断模型忽视数据噪声，且架构设计依赖专家经验，限制了实际应用。
- 方法要点：采用进化多目标一次性神经架构搜索，分训练和搜索两阶段，构建搜索空间并优化噪声场景下的架构。
- 实验或效果：在真实教育数据集上验证，OSCD发现的架构在认知诊断任务中表现出有效性和鲁棒性。

## 摘要（原文）

> With the advancement of network technologies, intelligent tutoring systems (ITS) have emerged to deliver increasingly precise and tailored personalized learning services. Cognitive diagnosis (CD) has emerged as a core research task in ITS, aiming to infer learners' mastery of specific knowledge concepts by modeling the mapping between learning behavior data and knowledge states. However, existing research prioritizes model performance enhancement while neglecting the pervasive noise contamination in observed response data, significantly hindering practical deployment. Furthermore, current cognitive diagnosis models (CDMs) rely heavily on researchers' domain expertise for structural design, which fails to exhaustively explore architectural possibilities, thus leaving model architectures' full potential untapped. To address this issue, we propose OSCD, an evolutionary multi-objective One-Shot neural architecture search method for Cognitive Diagnosis, designed to efficiently and robustly improve the model's capability in assessing learner proficiency. Specifically, OSCD operates through two distinct stages: training and searching. During the training stage, we construct a search space encompassing diverse architectural combinations and train a weight-sharing supernet represented via the complete binary tree topology, enabling comprehensive exploration of potential architectures beyond manual design priors. In the searching stage, we formulate the optimal architecture search under heterogeneous noise scenarios as a multi-objective optimization problem (MOP), and develop an optimization framework integrating a Pareto-optimal solution search strategy with cross-scenario performance evaluation for resolution. Extensive experiments on real-world educational datasets validate the effectiveness and robustness of the optimal architectures discovered by our OSCD model for CD tasks.

