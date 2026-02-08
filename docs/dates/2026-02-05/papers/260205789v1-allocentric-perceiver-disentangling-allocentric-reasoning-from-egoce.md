---
layout: default
title: Allocentric Perceiver: Disentangling Allocentric Reasoning from Egocentric Visual Priors via Frame Instantiation
---

# Allocentric Perceiver: Disentangling Allocentric Reasoning from Egocentric Visual Priors via Frame Instantiation
**arXiv**：[2602.05789v1](https://arxiv.org/abs/2602.05789) · [PDF](https://arxiv.org/pdf/2602.05789.pdf)  
**作者**：Hengyi Wang, Ruiqiang Zhang, Chang Liu, Guanjie Wang, Zehua Ma, Han Fang, Weiming Zhang  

**一句话要点**：提出Allocentric Perceiver，通过帧实例化从以自我为中心的视觉先验中解耦以他者为中心的空间推理

**关键词**：以他者为中心推理, 视觉语言模型, 空间推理, 3D重建, 帧实例化, 几何表示

## 3 点简述
- 核心问题：视觉语言模型在以他者为中心的空间查询中表现脆弱，需显式视角转换
- 方法要点：利用现成几何专家恢复3D状态，实例化查询条件化的以他者为中心参考帧
- 实验或效果：在空间推理基准上实现约10%提升，超越微调模型和先进模型

## 摘要（原文）

> With the rising need for spatially grounded tasks such as Vision-Language Navigation/Action, allocentric perception capabilities in Vision-Language Models (VLMs) are receiving growing focus. However, VLMs remain brittle on allocentric spatial queries that require explicit perspective shifts, where the answer depends on reasoning in a target-centric frame rather than the observed camera view. Thus, we introduce Allocentric Perceiver, a training-free strategy that recovers metric 3D states from one or more images with off-the-shelf geometric experts, and then instantiates a query-conditioned allocentric reference frame aligned with the instruction's semantic intent. By deterministically transforming reconstructed geometry into the target frame and prompting the backbone VLM with structured, geometry-grounded representations, Allocentric Perceriver offloads mental rotation from implicit reasoning to explicit computation. We evaluate Allocentric Perciver across multiple backbone families on spatial reasoning benchmarks, observing consistent and substantial gains ($\sim$10%) on allocentric tasks while maintaining strong egocentric performance, and surpassing both spatial-perception-finetuned models and state-of-the-art open-source and proprietary models.

