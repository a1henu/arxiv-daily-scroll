---
layout: default
title: From Observations to Events: Event-Aware World Model for Reinforcement Learning
---

# From Observations to Events: Event-Aware World Model for Reinforcement Learning
**arXiv**：[2601.19336v1](https://arxiv.org/abs/2601.19336) · [PDF](https://arxiv.org/pdf/2601.19336.pdf)  
**作者**：Zhao-Han Peng, Shaohui Li, Zhi Li, Shulan Ruan, Yu Liu, You He  

**一句话要点**：提出事件感知世界模型以提升强化学习在结构相似场景中的泛化能力

**关键词**：事件感知表示, 世界模型, 强化学习, 泛化能力, 事件分割

## 3 点简述
- 现有基于模型的强化学习方法在纹理或颜色变化等伪变化下泛化能力不足
- EAWM通过自动事件生成器和通用事件分割器学习事件感知表示，无需人工标注
- 在多个基准测试中性能提升10%-45%，达到新的最先进水平

## 摘要（原文）

> While model-based reinforcement learning (MBRL) improves sample efficiency by learning world models from raw observations, existing methods struggle to generalize across structurally similar scenes and remain vulnerable to spurious variations such as textures or color shifts. From a cognitive science perspective, humans segment continuous sensory streams into discrete events and rely on these key events for decision-making. Motivated by this principle, we propose the Event-Aware World Model (EAWM), a general framework that learns event-aware representations to streamline policy learning without requiring handcrafted labels. EAWM employs an automated event generator to derive events from raw observations and introduces a Generic Event Segmentor (GES) to identify event boundaries, which mark the start and end time of event segments. Through event prediction, the representation space is shaped to capture meaningful spatio-temporal transitions. Beyond this, we present a unified formulation of seemingly distinct world model architectures and show the broad applicability of our methods. Experiments on Atari 100K, Craftax 1M, and DeepMind Control 500K, DMC-GB2 500K demonstrate that EAWM consistently boosts the performance of strong MBRL baselines by 10%-45%, setting new state-of-the-art results across benchmarks. Our code is released at https://github.com/MarquisDarwin/EAWM.

