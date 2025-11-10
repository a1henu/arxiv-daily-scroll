---
layout: default
title: PreResQ-R1: Towards Fine-Grained Rank-and-Score Reinforcement Learning for Visual Quality Assessment via Preference-Response Disentangled Policy Optimization
---

# PreResQ-R1: Towards Fine-Grained Rank-and-Score Reinforcement Learning for Visual Quality Assessment via Preference-Response Disentangled Policy Optimization
**arXiv**：[2511.05393v1](https://arxiv.org/abs/2511.05393) · [PDF](https://arxiv.org/pdf/2511.05393.pdf)  
**作者**：Zehui Feng, Tian Qiu, Tong Wu, Junxuan Li, Huayuan Xu, Ting Han  

**一句话要点**：提出PreResQ-R1框架，通过偏好-响应解耦强化学习统一评分与排序，提升视觉质量评估性能。

**关键词**：视觉质量评估, 强化学习, 偏好-响应解耦, 多模态大语言模型, 视频质量评估, 推理优化

## 3 点简述
- 现有视觉质量评估方法依赖监督微调或仅排序目标，导致推理浅层、分数校准差和跨域泛化弱。
- 引入双分支奖励设计，分离样本内响应一致性和样本间偏好对齐，采用GRPO优化推理过程。
- 在少量数据上微调，在多个IQA和VQA基准上实现SOTA，推理轨迹与人类感知对齐。

## 摘要（原文）

> Visual Quality Assessment (QA) seeks to predict human perceptual judgments of
> visual fidelity. While recent multimodal large language models (MLLMs) show
> promise in reasoning about image and video quality, existing approaches mainly
> rely on supervised fine-tuning or rank-only objectives, resulting in shallow
> reasoning, poor score calibration, and limited cross-domain generalization. We
> propose PreResQ-R1, a Preference-Response Disentangled Reinforcement Learning
> framework that unifies absolute score regression and relative ranking
> consistency within a single reasoning-driven optimization scheme. Unlike prior
> QA methods, PreResQ-R1 introduces a dual-branch reward formulation that
> separately models intra-sample response coherence and inter-sample preference
> alignment, optimized via Group Relative Policy Optimization (GRPO). This design
> encourages fine-grained, stable, and interpretable chain-of-thought reasoning
> about perceptual quality. To extend beyond static imagery, we further design a
> global-temporal and local-spatial data flow strategy for Video Quality
> Assessment. Remarkably, with reinforcement fine-tuning on only 6K images and
> 28K videos, PreResQ-R1 achieves state-of-the-art results across 10 IQA and 5
> VQA benchmarks under both SRCC and PLCC metrics, surpassing by margins of 5.30%
> and textbf2.15% in IQA task, respectively. Beyond quantitative gains, it
> produces human-aligned reasoning traces that reveal the perceptual cues
> underlying quality judgments. Code and model are available.

