---
layout: default
title: Flow-Factory: A Unified Framework for Reinforcement Learning in Flow-Matching Models
---

# Flow-Factory: A Unified Framework for Reinforcement Learning in Flow-Matching Models
**arXiv**：[2602.12529v1](https://arxiv.org/abs/2602.12529) · [PDF](https://arxiv.org/pdf/2602.12529.pdf)  
**作者**：Bowen Ping, Chengyou Jia, Minnan Luo, Hangwei Qian, Ivor Tsang  

**一句话要点**：提出Flow-Factory统一框架，以模块化架构解决流匹配模型强化学习中的代码碎片化问题。

**关键词**：流匹配模型, 强化学习, 模块化框架, 代码库统一, 生产优化, 分布式训练

## 3 点简述
- 核心问题：流匹配模型强化学习存在代码库碎片化、模型特定实现和工程复杂性。
- 方法要点：通过基于注册表的模块化架构，解耦算法、模型和奖励，支持新算法和架构无缝集成。
- 实验或效果：在Flux、Qwen-Image和WAN视频模型上支持GRPO、DiffusionNFT和AWM算法，提供生产级优化和分布式训练。

## 摘要（原文）

> Reinforcement learning has emerged as a promising paradigm for aligning diffusion and flow-matching models with human preferences, yet practitioners face fragmented codebases, model-specific implementations, and engineering complexity. We introduce Flow-Factory, a unified framework that decouples algorithms, models, and rewards through through a modular, registry-based architecture. This design enables seamless integration of new algorithms and architectures, as demonstrated by our support for GRPO, DiffusionNFT, and AWM across Flux, Qwen-Image, and WAN video models. By minimizing implementation overhead, Flow-Factory empowers researchers to rapidly prototype and scale future innovations with ease. Flow-Factory provides production-ready memory optimization, flexible multi-reward training, and seamless distributed training support. The codebase is available at https://github.com/X-GenGroup/Flow-Factory.

