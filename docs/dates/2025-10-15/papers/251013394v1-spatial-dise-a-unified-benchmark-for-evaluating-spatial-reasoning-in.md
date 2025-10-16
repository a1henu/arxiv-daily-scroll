---
layout: default
title: Spatial-DISE: A Unified Benchmark for Evaluating Spatial Reasoning in Vision-Language Models
---

# Spatial-DISE: A Unified Benchmark for Evaluating Spatial Reasoning in Vision-Language Models
**arXiv**：[2510.13394v1](https://arxiv.org/abs/2510.13394) · [PDF](https://arxiv.org/pdf/2510.13394.pdf)  
**作者**：Xinmiao Huang, Qisong He, Zhenglin Huang, Boxuan Wang, Zhuoyun Li, Guangliang Cheng, Yi Dong, Xiaowei Huang  

**一句话要点**：提出Spatial-DISE基准以评估视觉语言模型的空间推理能力

**关键词**：空间推理评估, 视觉语言模型, 基准构建, 数据集生成, 多视图推理, 认知分类法

## 3 点简述
- 现有基准无法充分评估内在动态空间推理等关键能力
- 基于认知分类法构建统一基准，并自动化生成可验证数据集
- 评估28个先进模型，揭示其在多步多视图推理上与人类存在差距

## 摘要（原文）

> Spatial reasoning ability is crucial for Vision Language Models (VLMs) to
> support real-world applications in diverse domains including robotics,
> augmented reality, and autonomous navigation. Unfortunately, existing
> benchmarks are inadequate in assessing spatial reasoning ability, especially
> the \emph{intrinsic-dynamic} spatial reasoning which is a fundamental aspect of
> human spatial cognition. In this paper, we propose a unified benchmark,
> \textbf{Spatial-DISE}, based on a cognitively grounded taxonomy that
> categorizes tasks into four fundamental quadrants:
> \textbf{I}ntrinsic-\textbf{S}tatic, Intrinsic-\textbf{D}ynamic,
> \textbf{E}xtrinsic-Static, and Extrinsic-Dynamic spatial reasoning. Moreover,
> to address the issue of data scarcity, we develop a scalable and automated
> pipeline to generate diverse and verifiable spatial reasoning questions,
> resulting in a new \textbf{Spatial-DISE} dataset that includes Spatial-DISE
> Bench (559 evaluation VQA pairs) and Spatial-DISE-12K (12K+ training VQA
> pairs). Our comprehensive evaluation across 28 state-of-the-art VLMs reveals
> that, current VLMs have a large and consistent gap to human competence,
> especially on multi-step multi-view spatial reasoning. Spatial-DISE offers a
> robust framework, valuable dataset, and clear direction for future research
> toward human-like spatial intelligence. Benchmark, dataset, and code will be
> publicly released.

