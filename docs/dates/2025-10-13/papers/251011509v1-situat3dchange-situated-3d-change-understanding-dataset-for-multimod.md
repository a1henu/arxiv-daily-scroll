---
layout: default
title: Situat3DChange: Situated 3D Change Understanding Dataset for Multimodal Large Language Model
---

# Situat3DChange: Situated 3D Change Understanding Dataset for Multimodal Large Language Model
**arXiv**：[2510.11509v1](https://arxiv.org/abs/2510.11509) · [PDF](https://arxiv.org/pdf/2510.11509.pdf)  
**作者**：Ruiping Liu, Junwei Zheng, Yufan Chen, Zirui Wang, Kunyu Peng, Kailun Yang, Jiaming Zhang, Marc Pollefeys, Rainer Stiefelhagen  

**一句话要点**：提出Situat3DChange数据集和SCReasoner方法以解决3D动态场景理解问题

**关键词**：3D变化理解, 多模态大语言模型, 点云比较, 情境感知, 人机协作, 数据集构建

## 3 点简述
- 核心问题：现有3D数据集对动态环境和情境理解不完整，限制人机协作。
- 方法要点：构建大规模数据集，集成多视角观察，并开发高效3D MLLM进行点云比较。
- 实验或效果：评估显示MLLM在动态场景理解有进展，数据集具任务无关有效性。

## 摘要（原文）

> Physical environments and circumstances are fundamentally dynamic, yet
> current 3D datasets and evaluation benchmarks tend to concentrate on either
> dynamic scenarios or dynamic situations in isolation, resulting in incomplete
> comprehension. To overcome these constraints, we introduce Situat3DChange, an
> extensive dataset supporting three situation-aware change understanding tasks
> following the perception-action model: 121K question-answer pairs, 36K change
> descriptions for perception tasks, and 17K rearrangement instructions for the
> action task. To construct this large-scale dataset, Situat3DChange leverages
> 11K human observations of environmental changes to establish shared mental
> models and shared situational awareness for human-AI collaboration. These
> observations, enriched with egocentric and allocentric perspectives as well as
> categorical and coordinate spatial relations, are integrated using an LLM to
> support understanding of situated changes. To address the challenge of
> comparing pairs of point clouds from the same scene with minor changes, we
> propose SCReasoner, an efficient 3D MLLM approach that enables effective point
> cloud comparison with minimal parameter overhead and no additional tokens
> required for the language decoder. Comprehensive evaluation on Situat3DChange
> tasks highlights both the progress and limitations of MLLMs in dynamic scene
> and situation understanding. Additional experiments on data scaling and
> cross-domain transfer demonstrate the task-agnostic effectiveness of using
> Situat3DChange as a training dataset for MLLMs.

