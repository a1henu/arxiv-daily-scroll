---
layout: default
title: ReEXplore: Improving MLLMs for Embodied Exploration with Contextualized Retrospective Experience Replay
---

# ReEXplore: Improving MLLMs for Embodied Exploration with Contextualized Retrospective Experience Replay
**arXiv**：[2511.19033v1](https://arxiv.org/abs/2511.19033) · [PDF](https://arxiv.org/pdf/2511.19033.pdf)  
**作者**：Gengyuan Zhang, Mingcong Ding, Jingpei Wu, Ruotong Liao, Volker Tresp  

**一句话要点**：提出ReEXplore框架以改进MLLM在具身探索中的性能

**关键词**：具身探索, 多模态大语言模型, 经验回放, 分层决策, 无训练框架

## 3 点简述
- 核心问题：MLLM在具身探索中依赖过时知识、训练成本高且难以处理复杂动作空间
- 方法要点：采用无训练框架，结合回顾经验回放和分层边界选择
- 实验或效果：在多个基准测试中，性能提升高达3倍，导航效率显著提高

## 摘要（原文）

> Embodied exploration is a target-driven process that requires embodied agents to possess fine-grained perception and knowledge-enhanced decision making. While recent attempts leverage MLLMs for exploration due to their strong perceptual and reasoning abilities, we find that MLLM-based embodied agents remain suboptimal in exploring new environments: (i) they rely on profound but stale pre-trained knowledge, (ii) training-based approaches such as imitation learning or reinforcement learning are expensive for long-horizon tasks with sparse outcome rewards, and (iii) frontier-based exploration yields a large, visually nuanced action space that is difficult for MLLMs to make reliable decisions. We address these challenges with ReEXplore, a training-free framework that performs retrospective experience replay to inject distilled, abstract experience at inference time, and hierarchical frontier selection to decompose frontier ranking into coarse-to-fine decisions. Our approach enables robust, traceable, and efficient exploration. Across multiple embodied exploration benchmarks, ReEXplore yields great improvements over strong MLLM baselines, up to 3x higher performance in both success rate and in navigation efficiency under open-source backbones.

