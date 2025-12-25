---
layout: default
title: ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments
---

# ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments
**arXiv**：[2512.20940v1](https://arxiv.org/abs/2512.20940) · [PDF](https://arxiv.org/pdf/2512.20940.pdf)  
**作者**：Shuhao Ye, Sitong Mao, Yuxiang Cui, Xuan Yu, Shichao Zhai, Wen Chen, Shunbo Zhou, Rong Xiong, Yue Wang  

**一句话要点**：提出ETP-R1框架，通过大规模数据与强化微调提升基于图的连续环境视觉语言导航性能。

**关键词**：视觉语言导航, 连续环境, 拓扑规划, 强化微调, 大规模预训练, 图基模型

## 3 点简述
- 核心问题：基于图的方法在连续环境视觉语言导航中利用大规模数据和先进训练范式不足，落后于大型视觉语言模型方法。
- 方法要点：构建高质量大规模预训练数据集，采用三阶段训练范式，首次将闭环在线强化微调应用于基于图的模型。
- 实验或效果：在R2R-CE和RxR-CE基准测试中，所有主要指标均达到新的最先进性能。

## 摘要（原文）

> Vision-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to navigate towards target in continuous environments, following natural language instructions. While current graph-based methods offer an efficient, structured approach by abstracting the environment into a topological map and simplifying the action space to waypoint selection, they lag behind methods based on Large Vision-Language Models (LVLMs) in leveraging large-scale data and advanced training paradigms. In this paper, we try to bridge this gap by introducing ETP-R1, a framework that applies the paradigm of scaling up data and Reinforcement Fine-Tuning (RFT) to a graph-based VLN-CE model. To build a strong foundation, we first construct a high-quality, large-scale pretraining dataset using the Gemini API. This dataset consists of diverse, low-hallucination instructions for topological trajectories, providing rich supervision for our graph-based policy to map language to topological paths. This foundation is further strengthened by unifying data from both R2R and RxR tasks for joint pretraining. Building on this, we introduce a three-stage training paradigm, which culminates in the first application of closed-loop, online RFT to a graph-based VLN-CE model, powered by the Group Relative Policy Optimization (GRPO) algorithm. Extensive experiments demonstrate that our approach is highly effective, establishing new state-of-the-art performance across all major metrics on both the R2R-CE and RxR-CE benchmarks. Our code is available at https://github.com/Cepillar/ETP-R1.

