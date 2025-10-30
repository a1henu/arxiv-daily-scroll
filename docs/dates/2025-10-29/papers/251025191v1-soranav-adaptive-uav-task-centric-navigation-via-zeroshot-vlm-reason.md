---
layout: default
title: SoraNav: Adaptive UAV Task-Centric Navigation via Zeroshot VLM Reasoning
---

# SoraNav: Adaptive UAV Task-Centric Navigation via Zeroshot VLM Reasoning
**arXiv**：[2510.25191v1](https://arxiv.org/abs/2510.25191) · [PDF](https://arxiv.org/pdf/2510.25191.pdf)  
**作者**：Hongyu Song, Rishabh Dev Yadav, Cheng Guo, Wei Pan  

**一句话要点**：提出SoraNav框架，通过零样本VLM推理与几何感知决策，提升UAV在复杂任务中的导航性能。

**关键词**：无人机导航, 视觉语言模型, 零样本推理, 几何感知决策, 混合切换策略, 数字孪生

## 3 点简述
- 核心问题：现有VLN方法难以泛化到UAV的3D空间推理任务，缺乏空间基础。
- 方法要点：集成零样本VLM推理与几何先验，采用混合切换策略优化导航决策。
- 实验效果：在2.5D和3D场景中，成功率和路径长度加权成功率显著提升。

## 摘要（原文）

> Interpreting visual observations and natural language instructions for
> complex task execution remains a key challenge in robotics and AI. Despite
> recent advances, language-driven navigation is still difficult, particularly
> for UAVs in small-scale 3D environments. Existing Vision-Language Navigation
> (VLN) approaches are mostly designed for ground robots and struggle to
> generalize to aerial tasks that require full 3D spatial reasoning. The
> emergence of large Vision-Language Models (VLMs), such as GPT and Claude,
> enables zero-shot semantic reasoning from visual and textual inputs. However,
> these models lack spatial grounding and are not directly applicable to
> navigation. To address these limitations, SoraNav is introduced, an adaptive
> UAV navigation framework that integrates zero-shot VLM reasoning with
> geometry-aware decision-making. Geometric priors are incorporated into image
> annotations to constrain the VLM action space and improve decision quality. A
> hybrid switching strategy leverages navigation history to alternate between VLM
> reasoning and geometry-based exploration, mitigating dead-ends and redundant
> revisits. A PX4-based hardware-software platform, comprising both a digital
> twin and a physical micro-UAV, enables reproducible evaluation. Experimental
> results show that in 2.5D scenarios, our method improves Success Rate (SR) by
> 25.7% and Success weighted by Path Length (SPL) by 17%. In 3D scenarios, it
> improves SR by 29.5% and SPL by 18.5% relative to the baseline.

