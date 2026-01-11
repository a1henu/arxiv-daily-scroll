---
layout: default
title: GeM-VG: Towards Generalized Multi-image Visual Grounding with Multimodal Large Language Models
---

# GeM-VG: Towards Generalized Multi-image Visual Grounding with Multimodal Large Language Models
**arXiv**：[2601.04777v1](https://arxiv.org/abs/2601.04777) · [PDF](https://arxiv.org/pdf/2601.04777.pdf)  
**作者**：Shurong Zheng, Yousong Zhu, Hongyin Zhao, Fan Yang, Yufei Zhan, Ming Tang, Jinqiao Wang  

**一句话要点**：提出GeM-VG以解决多图像视觉定位任务中缺乏统一建模的问题

**关键词**：多模态大语言模型, 多图像视觉定位, 广义任务建模, 混合强化微调, 链式思维推理, 数据集构建

## 3 点简述
- 核心问题：现有多图像视觉定位方法受限于单目标定位和任务类型有限，缺乏对广义任务的统一建模。
- 方法要点：提出GeM-VG模型，基于任务分类引入MG-Data-240K数据集，并采用混合强化微调策略结合链式思维推理和直接回答。
- 实验或效果：在MIG-Bench和MC-Bench上分别超越先前领先MLLMs 2.0%和9.7%，单图像定位在ODINW上提升9.1%。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated impressive progress in single-image grounding and general multi-image understanding. Recently, some methods begin to address multi-image grounding. However, they are constrained by single-target localization and limited types of practical tasks, due to the lack of unified modeling for generalized grounding tasks. Therefore, we propose GeM-VG, an MLLM capable of Generalized Multi-image Visual Grounding. To support this, we systematically categorize and organize existing multi-image grounding tasks according to their reliance of cross-image cues and reasoning, and introduce the MG-Data-240K dataset, addressing the limitations of existing datasets regarding target quantity and image relation. To tackle the challenges of robustly handling diverse multi-image grounding tasks, we further propose a hybrid reinforcement finetuning strategy that integrates chain-of-thought (CoT) reasoning and direct answering, considering their complementary strengths. This strategy adopts an R1-like algorithm guided by a carefully designed rule-based reward, effectively enhancing the model's overall perception and reasoning capabilities. Extensive experiments demonstrate the superior generalized grounding capabilities of our model. For multi-image grounding, it outperforms the previous leading MLLMs by 2.0% and 9.7% on MIG-Bench and MC-Bench, respectively. In single-image grounding, it achieves a 9.1% improvement over the base model on ODINW. Furthermore, our model retains strong capabilities in general multi-image understanding.

