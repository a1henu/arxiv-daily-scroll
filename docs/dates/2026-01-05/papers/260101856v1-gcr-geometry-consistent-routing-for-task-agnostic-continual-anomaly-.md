---
layout: default
title: GCR: Geometry-Consistent Routing for Task-Agnostic Continual Anomaly Detection
---

# GCR: Geometry-Consistent Routing for Task-Agnostic Continual Anomaly Detection
**arXiv**：[2601.01856v1](https://arxiv.org/abs/2601.01856) · [PDF](https://arxiv.org/pdf/2601.01856.pdf)  
**作者**：Joongwon Chae, Lihui Luo, Yang Liu, Runming Wang, Dongmei Yu, Zeming Liang, Xi Yuan, Dayan Zhang, Zhenglin Chen, Peiwu Qin, Ilmoon Chae  

**一句话要点**：提出几何一致性路由框架，以稳定任务无关的持续异常检测

**关键词**：异常检测, 持续学习, 几何一致性路由, 任务无关检测, 原型匹配, 工业视觉

## 3 点简述
- 核心问题：任务无关持续异常检测中，跨专家路由规则因分数分布差异而不稳定
- 方法要点：在共享冻结嵌入空间中，通过最小化最近原型距离实现几何一致性路由
- 实验效果：在MVTec AD和VisA数据集上显著提升路由稳定性，实现近零遗忘

## 摘要（原文）

> Feature-based anomaly detection is widely adopted in industrial inspection due to the strong representational power of large pre-trained vision encoders. While most existing methods focus on improving within-category anomaly scoring, practical deployments increasingly require task-agnostic operation under continual category expansion, where the category identity is unknown at test time. In this setting, overall performance is often dominated by expert selection, namely routing an input to an appropriate normality model before any head-specific scoring is applied. However, routing rules that compare head-specific anomaly scores across independently constructed heads are unreliable in practice, as score distributions can differ substantially across categories in scale and tail behavior.
>   We propose GCR, a lightweight mixture-of-experts framework for stabilizing task-agnostic continual anomaly detection through geometry-consistent routing. GCR routes each test image directly in a shared frozen patch-embedding space by minimizing an accumulated nearest-prototype distance to category-specific prototype banks, and then computes anomaly maps only within the routed expert using a standard prototype-based scoring rule. By separating cross-head decision making from within-head anomaly scoring, GCR avoids cross-head score comparability issues without requiring end-to-end representation learning.
>   Experiments on MVTec AD and VisA show that geometry-consistent routing substantially improves routing stability and mitigates continual performance collapse, achieving near-zero forgetting while maintaining competitive detection and localization performance. These results indicate that many failures previously attributed to representation forgetting can instead be explained by decision-rule instability in cross-head routing. Code is available at https://github.com/jw-chae/GCR

