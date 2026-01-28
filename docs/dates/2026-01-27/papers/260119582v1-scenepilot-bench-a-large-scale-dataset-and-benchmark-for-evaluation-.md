---
layout: default
title: ScenePilot-Bench: A Large-Scale Dataset and Benchmark for Evaluation of Vision-Language Models in Autonomous Driving
---

# ScenePilot-Bench: A Large-Scale Dataset and Benchmark for Evaluation of Vision-Language Models in Autonomous Driving
**arXiv**：[2601.19582v1](https://arxiv.org/abs/2601.19582) · [PDF](https://arxiv.org/pdf/2601.19582.pdf)  
**作者**：Yujin Wang, Yutong Zheng, Wenxian Fan, Tianyi Wang, Hongqing Chu, Daxin Tian, Bingzhao Gao, Jianqiang Wang, Hong Chen  

**一句话要点**：提出ScenePilot-Bench基准以评估自动驾驶场景中的视觉语言模型

**关键词**：自动驾驶基准, 视觉语言模型评估, 多粒度标注, 安全感知指标, 跨区域泛化

## 3 点简述
- 核心问题：自动驾驶中视觉语言模型评估缺乏大规模、多粒度基准
- 方法要点：基于ScenePilot-4K数据集构建四轴评估套件，涵盖场景理解、空间感知、运动规划和GPT-Score
- 实验或效果：基准测试代表性模型，分析性能边界并识别驾驶导向推理的差距

## 摘要（原文）

> In this paper, we introduce ScenePilot-Bench, a large-scale first-person driving benchmark designed to evaluate vision-language models (VLMs) in autonomous driving scenarios. ScenePilot-Bench is built upon ScenePilot-4K, a diverse dataset comprising 3,847 hours of driving videos, annotated with multi-granularity information including scene descriptions, risk assessments, key participant identification, ego trajectories, and camera parameters. The benchmark features a four-axis evaluation suite that assesses VLM capabilities in scene understanding, spatial perception, motion planning, and GPT-Score, with safety-aware metrics and cross-region generalization settings. We benchmark representative VLMs on ScenePilot-Bench, providing empirical analyses that clarify current performance boundaries and identify gaps for driving-oriented reasoning. ScenePilot-Bench offers a comprehensive framework for evaluating and advancing VLMs in safety-critical autonomous driving contexts.

