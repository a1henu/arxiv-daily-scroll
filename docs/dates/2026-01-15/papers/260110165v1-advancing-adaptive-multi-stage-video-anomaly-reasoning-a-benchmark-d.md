---
layout: default
title: Advancing Adaptive Multi-Stage Video Anomaly Reasoning: A Benchmark Dataset and Method
---

# Advancing Adaptive Multi-Stage Video Anomaly Reasoning: A Benchmark Dataset and Method
**arXiv**：[2601.10165v1](https://arxiv.org/abs/2601.10165) · [PDF](https://arxiv.org/pdf/2601.10165.pdf)  
**作者**：Chao Huang, Benfeng Wang, Wei Wang, Jie Wen, Li Shen, Wenqi Ren, Yong Xu, Xiaochun Cao  

**一句话要点**：提出视频异常推理任务与数据集，以增强多模态大语言模型在视频异常分析中的结构化推理能力。

**关键词**：视频异常推理, 多模态大语言模型, 结构化推理, 弱监督学习, 数据集构建, 风险感知决策

## 3 点简述
- 现有方法在视频异常检测与理解中缺乏显式推理过程，本文定义视频异常推理任务，要求模型进行多阶段推理。
- 构建包含8,641个视频和50,000+样本的数据集，基于PerCoAct-CoT链式思维标注，支持系统评估。
- 提出Vad-R1-Plus模型和优化方法，实验显示在视频异常推理任务上优于基线模型。

## 摘要（原文）

> Recent progress in reasoning capabilities of Multimodal Large Language Models(MLLMs) has highlighted their potential for performing complex video understanding tasks. However, in the domain of Video Anomaly Detection and Understanding (VAD&U), existing MLLM-based methods are largely limited to anomaly localization or post-hoc description, lacking explicit reasoning processes, risk awareness, and decision-oriented interpretation. To address this gap, we define a new task termed Video Anomaly Reasoning (VAR), which elevates video anomaly analysis from descriptive understanding to structured, multi-stage reasoning. VAR explicitly requires models to perform progressive reasoning over anomalous events before answering anomaly-related questions, encompassing visual perception, causal interpretation, and risk-aware decision making. To support this task, we present a new dataset with 8,641 videos, where each video is annotated with diverse question types corresponding to different reasoning depths, totaling more than 50,000 samples, making it one of the largest datasets for video anomaly. The annotations are based on a structured Perception-Cognition-Action Chain-of-Thought (PerCoAct-CoT), which formalizes domain-specific reasoning priors for video anomaly understanding. This design enables systematic evaluation of multi-stage and adaptive anomaly reasoning. In addition, we propose Anomaly-Aware Group Relative Policy Optimization to further enhance reasoning reliability under weak supervision. Building upon the proposed task and dataset, we develop an end-to-end MLLM-based VAR model termed Vad-R1-Plus, which supports adaptive hierarchical reasoning and risk-aware decision making. Extensive experiments demonstrate that the proposed benchmark and method effectively advance the reasoning capabilities of MLLMs on VAR tasks, outperforming both open-source and proprietary baselines.

