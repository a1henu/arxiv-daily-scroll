---
layout: default
title: OSCAR: Optimization-Steered Agentic Planning for Composed Image Retrieval
---

# OSCAR: Optimization-Steered Agentic Planning for Composed Image Retrieval
**arXiv**：[2602.08603v1](https://arxiv.org/abs/2602.08603) · [PDF](https://arxiv.org/pdf/2602.08603.pdf)  
**作者**：Teng Wang, Rong Shan, Jianghao Lin, Junjie Wu, Tianyi Xu, Jianping Zhang, Wenteng Chen, Changwang Zhang, Zhaoxiang Wang, Weinan Zhang, Jun Wang  

**一句话要点**：提出OSCAR框架，通过优化引导的智能体规划解决组合图像检索问题。

**关键词**：组合图像检索, 智能体规划, 轨迹优化, 混合整数规划, 视觉语言模型, 离线-在线学习

## 3 点简述
- 组合图像检索需处理异构视觉和文本约束，现有方法存在单模型短视或启发式搜索低效问题。
- OSCAR将智能体检索重构为轨迹优化问题，采用离线-在线范式，离线阶段通过混合整数规划推导最优轨迹。
- 在多个基准测试中，OSCAR优于现有方法，仅用10%训练数据即实现强泛化性能。

## 摘要（原文）

> Composed image retrieval (CIR) requires complex reasoning over heterogeneous visual and textual constraints. Existing approaches largely fall into two paradigms: unified embedding retrieval, which suffers from single-model myopia, and heuristic agentic retrieval, which is limited by suboptimal, trial-and-error orchestration. To this end, we propose OSCAR, an optimization-steered agentic planning framework for composed image retrieval. We are the first to reformulate agentic CIR from a heuristic search process into a principled trajectory optimization problem. Instead of relying on heuristic trial-and-error exploration, OSCAR employs a novel offline-online paradigm. In the offline phase, we model CIR via atomic retrieval selection and composition as a two-stage mixed-integer programming problem, mathematically deriving optimal trajectories that maximize ground-truth coverage for training samples via rigorous boolean set operations. These trajectories are then stored in a golden library to serve as in-context demonstrations for online steering of VLM planner at online inference time. Extensive experiments on three public benchmarks and a private industrial benchmark show that OSCAR consistently outperforms SOTA baselines. Notably, it achieves superior performance using only 10% of training data, demonstrating strong generalization of planning logic rather than dataset-specific memorization.

