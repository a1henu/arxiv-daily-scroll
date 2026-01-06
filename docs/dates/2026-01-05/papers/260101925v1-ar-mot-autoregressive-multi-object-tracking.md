---
layout: default
title: AR-MOT: Autoregressive Multi-object Tracking
---

# AR-MOT: Autoregressive Multi-object Tracking
**arXiv**：[2601.01925v1](https://arxiv.org/abs/2601.01925) · [PDF](https://arxiv.org/pdf/2601.01925.pdf)  
**作者**：Lianjie Jia, Yuhan Wu, Binghao Ran, Yifan Wang, Lijun Wang, Huchuan Lu  

**一句话要点**：提出AR-MOT，一种基于大语言模型的自回归多目标跟踪范式，以解决现有方法架构僵化、难以适应多模态和指令驱动任务的问题。

**关键词**：多目标跟踪, 自回归模型, 大语言模型, 序列生成, 区域感知对齐, 时序记忆融合

## 3 点简述
- 核心问题：现有多目标跟踪方法架构固定，依赖特定输出头，难以扩展至多模态或指令驱动场景。
- 方法要点：将跟踪任务建模为序列生成，引入对象分词器、区域感知对齐模块和时序记忆融合模块，无需任务特定头。
- 实验或效果：在MOT17和DanceTrack数据集上验证，性能与先进方法相当，支持灵活扩展。

## 摘要（原文）

> As multi-object tracking (MOT) tasks continue to evolve toward more general and multi-modal scenarios, the rigid and task-specific architectures of existing MOT methods increasingly hinder their applicability across diverse tasks and limit flexibility in adapting to new tracking formulations. Most approaches rely on fixed output heads and bespoke tracking pipelines, making them difficult to extend to more complex or instruction-driven tasks. To address these limitations, we propose AR-MOT, a novel autoregressive paradigm that formulates MOT as a sequence generation task within a large language model (LLM) framework. This design enables the model to output structured results through flexible sequence construction, without requiring any task-specific heads. To enhance region-level visual perception, we introduce an Object Tokenizer based on a pretrained detector. To mitigate the misalignment between global and regional features, we propose a Region-Aware Alignment (RAA) module, and to support long-term tracking, we design a Temporal Memory Fusion (TMF) module that caches historical object tokens. AR-MOT offers strong potential for extensibility, as new modalities or instructions can be integrated by simply modifying the output sequence format without altering the model architecture. Extensive experiments on MOT17 and DanceTrack validate the feasibility of our approach, achieving performance comparable to state-of-the-art methods while laying the foundation for more general and flexible MOT systems.

