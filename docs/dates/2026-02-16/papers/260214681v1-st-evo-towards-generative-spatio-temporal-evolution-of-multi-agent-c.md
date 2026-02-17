---
layout: default
title: ST-EVO: Towards Generative Spatio-Temporal Evolution of Multi-Agent Communication Topologies
---

# ST-EVO: Towards Generative Spatio-Temporal Evolution of Multi-Agent Communication Topologies
**arXiv**：[2602.14681v1](https://arxiv.org/abs/2602.14681) · [PDF](https://arxiv.org/pdf/2602.14681.pdf)  
**作者**：Xingjian Wu, Xvyuan Liu, Junkai Lu, Siyuan Wang, Yang Shu, Jilin Hu, Chenjuan Guo, Bin Yang  

**一句话要点**：提出ST-EVO以支持多智能体通信拓扑的生成式时空演化

**关键词**：多智能体系统, 时空演化, 通信拓扑, 流匹配调度, 自反馈学习

## 3 点简述
- 核心问题：现有自演化多智能体系统仅关注空间或时间单维度演化，限制协作能力。
- 方法要点：基于流匹配的调度器实现对话级通信调度，具备不确定性感知和自反馈能力。
- 实验或效果：在九个基准测试中实现约5%至25%的准确率提升，达到先进水平。

## 摘要（原文）

> LLM-powered Multi-Agent Systems (MAS) have emerged as an effective approach towards collaborative intelligence, and have attracted wide research interests. Among them, ``self-evolving'' MAS, treated as a more flexible and powerful technical route, can construct task-adaptive workflows or communication topologies, instead of relying on a predefined static structue template. Current self-evolving MAS mainly focus on Spatial Evolving or Temporal Evolving paradigm, which only considers the single dimension of evolution and does not fully incentivize LLMs' collaborative capability. In this work, we start from a novel Spatio-Temporal perspective by proposing ST-EVO, which supports dialogue-wise communication scheduling with a compact yet powerful flow-matching based Scheduler. To make precise Spatio-Temporal scheduling, ST-EVO can also perceive the uncertainty of MAS, and possesses self-feedback ability to learn from accumulated experience. Extensive experiments on nine benchmarks demonstrate the state-of-the-art performance of ST-EVO, achieving about 5%--25% accuracy improvement.

