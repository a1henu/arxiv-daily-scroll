---
layout: default
title: UrbanAlign: Post-hoc Semantic Calibration for VLM-Human Preference Alignment
---

# UrbanAlign: Post-hoc Semantic Calibration for VLM-Human Preference Alignment
**arXiv**：[2602.19442v1](https://arxiv.org/abs/2602.19442) · [PDF](https://arxiv.org/pdf/2602.19442.pdf)  
**作者**：Yecheng Zhang, Rong Zhao, Zhizhou Sha, Yong Li, Lei Wang, Ce Hou, Wen Ji, Hao Huang, Yunshan Wan, Jian Yu, Junhao Xia, Yuru Zhang, Chunlei Shi  

**一句话要点**：提出UrbanAlign框架，通过训练后语义校准实现VLM与人类偏好在城市感知任务中的对齐。

**关键词**：视觉语言模型对齐, 后处理校准, 城市感知, 概念瓶颈, 多智能体评分, 几何校准

## 3 点简述
- 核心问题：VLM在主观感知任务中输出与人类偏好存在差距，需无训练对齐。
- 方法要点：采用概念挖掘、多智能体结构化评分和几何校准的三阶段后处理流程。
- 实验或效果：在Place Pulse 2.0上准确率达72.2%，优于监督基线，保持维度级可解释性。

## 摘要（原文）

> Aligning vision-language model (VLM) outputs with human preferences in domain-specific tasks typically requires fine-tuning or reinforcement learning, both of which demand labelled data and GPU compute. We show that for subjective perception tasks, this alignment can be achieved without any model training: VLMs are already strong concept extractors but poor decision calibrators, and the gap can be closed externally. We propose a training-free post-hoc concept-bottleneck pipeline consisting of three tightly coupled stages: concept mining, multi-agent structured scoring, and geometric calibration, unified by an end-to-end dimension optimization loop. Interpretable evaluation dimensions are mined from a handful of human annotations; an Observer-Debater-Judge chain extracts robust continuous concept scores from a frozen VLM; and locally-weighted ridge regression on a hybrid visual-semantic manifold calibrates these scores against human ratings. Applied to urban perception as UrbanAlign, the framework achieves 72.2% accuracy ($κ=0.45$) on Place Pulse 2.0 across six categories, outperforming the best supervised baseline by +15.1 pp and uncalibrated VLM scoring by +16.3 pp, with full dimension-level interpretability and zero model-weight modification.

