---
layout: default
title: EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT
---

# EgoThinker: Unveiling Egocentric Reasoning with Spatio-Temporal CoT
**arXiv**：[2510.23569v1](https://arxiv.org/abs/2510.23569) · [PDF](https://arxiv.org/pdf/2510.23569.pdf)  
**作者**：Baoqi Pei, Yifei Huang, Jilan Xu, Yuping He, Guo Chen, Fei Wu, Yu Qiao, Jiangmiao Pang  

**一句话要点**：提出EgoThinker框架，通过时空链式思维监督增强多模态大语言模型在自我中心视频推理中的能力。

**关键词**：自我中心视频推理, 多模态大语言模型, 时空链式思维, 两阶段学习, 细粒度定位, EgoRe-5M数据集

## 3 点简述
- 核心问题：自我中心视频推理需推断隐藏意图和细粒度交互，现有MLLMs缺乏第一人称理解能力。
- 方法要点：构建EgoRe-5M数据集，采用两阶段学习（SFT和RFT）提升时空定位和推理。
- 实验效果：在多个自我中心基准测试中表现优异，细粒度时空定位任务有显著改进。

## 摘要（原文）

> Egocentric video reasoning centers on an unobservable agent behind the camera
> who dynamically shapes the environment, requiring inference of hidden
> intentions and recognition of fine-grained interactions. This core challenge
> limits current multimodal large language models MLLMs, which excel at visible
> event reasoning but lack embodied, first-person understanding. To bridge this
> gap, we introduce EgoThinker, a novel framework that endows MLLMs with robust
> egocentric reasoning capabilities through spatio-temporal chain-of-thought
> supervision and a two-stage learning curriculum. First, we introduce EgoRe-5M,
> a large-scale egocentric QA dataset constructed from 13M diverse egocentric
> video clips. This dataset features multi-minute segments annotated with
> detailed CoT rationales and dense hand-object grounding. Second, we employ SFT
> on EgoRe-5M to instill reasoning skills, followed by reinforcement fine-tuning
> RFT to further enhance spatio-temporal localization. Experimental results show
> that EgoThinker outperforms existing methods across multiple egocentric
> benchmarks, while achieving substantial improvements in fine-grained
> spatio-temporal localization tasks. Full code and data are released at
> https://github.com/InternRobotics/EgoThinker.

