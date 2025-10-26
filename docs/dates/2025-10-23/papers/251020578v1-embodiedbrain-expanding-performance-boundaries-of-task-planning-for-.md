---
layout: default
title: EmbodiedBrain: Expanding Performance Boundaries of Task Planning for Embodied Intelligence
---

# EmbodiedBrain: Expanding Performance Boundaries of Task Planning for Embodied Intelligence
**arXiv**：[2510.20578v1](https://arxiv.org/abs/2510.20578) · [PDF](https://arxiv.org/pdf/2510.20578.pdf)  
**作者**：Ding Zou, Feifan Wang, Mengyu Ge, Siyuan Fan, Zongbing Zhang, Wei Chen, Lingfeng Wang, Zhongyou Hu, Wenrui Yan, Zhengwei Gao, Hao Wang, Weizhao Jin, Yu Zhang, Hainan Zhao, Mingliang Zhang, Xianxian Xi, Yaru Zhang, Wenyuan Li, Zhengguang Gao, Yurui Zhu  

**一句话要点**：提出EmbodiedBrain模型以解决具身智能任务规划中的性能与延迟权衡问题

**关键词**：具身智能, 任务规划, 多模态大语言模型, 强化学习优化, 仿真环境, 开源框架

## 3 点简述
- 当前LLMs和MLLMs在具身任务中存在模型设计与代理需求不匹配、实时延迟与性能权衡、评估指标不真实等问题
- 采用代理对齐数据结构和SFT与Step-GRPO训练方法，集成生成奖励模型提升长时任务成功率
- 实验在通用、规划和端到端仿真基准上表现优异，开源数据、模型和评估方法

## 摘要（原文）

> The realization of Artificial General Intelligence (AGI) necessitates
> Embodied AI agents capable of robust spatial perception, effective task
> planning, and adaptive execution in physical environments. However, current
> large language models (LLMs) and multimodal LLMs (MLLMs) for embodied tasks
> suffer from key limitations, including a significant gap between model design
> and agent requirements, an unavoidable trade-off between real-time latency and
> performance, and the use of unauthentic, offline evaluation metrics. To address
> these challenges, we propose EmbodiedBrain, a novel vision-language foundation
> model available in both 7B and 32B parameter sizes. Our framework features an
> agent-aligned data structure and employs a powerful training methodology that
> integrates large-scale Supervised Fine-Tuning (SFT) with Step-Augumented Group
> Relative Policy Optimization (Step-GRPO), which boosts long-horizon task
> success by integrating preceding steps as Guided Precursors. Furthermore, we
> incorporate a comprehensive reward system, including a Generative Reward Model
> (GRM) accelerated at the infrastructure level, to improve training efficiency.
> For enable thorough validation, we establish a three-part evaluation system
> encompassing General, Planning, and End-to-End Simulation Benchmarks,
> highlighted by the proposal and open-sourcing of a novel, challenging
> simulation environment. Experimental results demonstrate that EmbodiedBrain
> achieves superior performance across all metrics, establishing a new
> state-of-the-art for embodied foundation models. Towards paving the way for the
> next generation of generalist embodied agents, we open-source all of our data,
> model weight, and evaluating methods, which are available at
> https://zterobot.github.io/EmbodiedBrain.github.io.

