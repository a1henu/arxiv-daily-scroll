---
layout: default
title: AI End-to-End Radiation Treatment Planning Under One Second
---

# AI End-to-End Radiation Treatment Planning Under One Second
**arXiv**：[2603.06338v1](https://arxiv.org/abs/2603.06338) · [PDF](https://arxiv.org/pdf/2603.06338.pdf)  
**作者**：Simon Arberet, Riqiang Gao, Martin Kraus, Florin C. Ghesu, Wilko Verbakel, Mamadou Diallo, Anthony Magliari, Venkatesan Karuppusamy, Sushil Beriwal, REQUITE Consortium, Ali Kamen, Dorin Comaniciu  

**一句话要点**：提出AIRT端到端深度学习框架，实现一秒内从CT图像生成可交付前列腺放疗计划

**关键词**：放疗计划自动化, 端到端深度学习, 前列腺癌治疗, 快速计划生成, 剂量优化

## 3 点简述
- 核心问题：现有自动化放疗计划生成耗时数分钟，依赖多次剂量评估与修正，影响临床效率。
- 方法要点：AIRT采用端到端深度学习，结合可微分剂量反馈、对抗性通量图塑形和数据增强，直接从CT图像和结构轮廓推断可交付计划。
- 实验或效果：在单Nvidia A100 GPU上，AIRT生成单弧VMAT前列腺计划时间低于一秒，基于超万例数据训练，在目标覆盖和器官保护指标上非劣于RapidPlan Eclipse。

## 摘要（原文）

> Artificial intelligence-based radiation therapy (RT) planning has the potential to reduce planning time and inter-planner variability, improving efficiency and consistency in clinical workflows. Most existing automated approaches rely on multiple dose evaluations and corrections, resulting in plan generation times of several minutes. We introduce AIRT (Artificial Intelligence-based Radiotherapy), an end-to-end deep-learning framework that directly infers deliverable treatment plans from CT images and structure contours. AIRT generates single-arc VMAT prostate plans, from imaging and anatomical inputs to leaf sequencing, in under one second on a single Nvidia A100 GPU. The framework includes a differentiable dose feedback, an adversarial fluence map shaping, and a plan generation augmentation to improve plan quality and robustness. The model was trained on more than 10,000 intact prostate cases. Non-inferiority to RapidPlan Eclipse was demonstrated across target coverage and OAR sparing metrics. Target homogeneity (HI = 0.10 $\pm$ 0.01) and OAR sparing were similar to reference plans when evaluated using AcurosXB. These results represent a significant step toward ultra-fast standardized RT planning and a streamlined clinical workflow.

