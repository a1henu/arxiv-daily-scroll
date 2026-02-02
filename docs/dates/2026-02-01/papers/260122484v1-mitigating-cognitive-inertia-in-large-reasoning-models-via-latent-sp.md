---
layout: default
title: Mitigating Cognitive Inertia in Large Reasoning Models via Latent Spike Steering
---

# Mitigating Cognitive Inertia in Large Reasoning Models via Latent Spike Steering
**arXiv**：[2601.22484v1](https://arxiv.org/abs/2601.22484) · [PDF](https://arxiv.org/pdf/2601.22484.pdf)  
**作者**：Seojin Lee, ByeongJeong Kim, Hwanhee Lee  

**一句话要点**：提出STARS框架以解决大型推理模型中的认知惯性问题

**关键词**：大型推理模型, 认知惯性, 隐藏状态分析, 实时引导, 无监督优化

## 3 点简述
- 核心问题：大型推理模型存在认知惯性，表现为过度思考或推理僵化，现有方法难以捕捉内部冲突。
- 方法要点：STARS通过监测隐藏状态的L2距离峰值识别认知转折点，并注入语言线索实时引导模型。
- 实验或效果：在多个基准测试中，STARS有效减少冗余循环并提高准确性，无需额外微调。

## 摘要（原文）

> While Large Reasoning Models (LRMs) have achieved remarkable performance by scaling test-time compute, they frequently suffer from Cognitive Inertia, a failure pattern manifesting as either overthinking (inertia of motion) or reasoning rigidity (inertia of direction). Existing detection methods, typically relying on superficial textual heuristics like self-correction tokens, often fail to capture the model's unvoiced internal conflicts. To address this, we propose STARS (Spike-Triggered Adaptive Reasoning Steering), a training-free framework designed to rectify cognitive inertia by monitoring latent dynamics. STARS identifies Cognitive Pivots-critical moments of reasoning transition-by detecting distinct L2 distance spikes in the hidden states. Upon detection, the framework employs geometric trajectory analysis to diagnose the structural nature of the transition and injects state-aware language cues to steer the model in real-time. Our experiments across diverse benchmarks confirm that STARS efficiently curtails redundant loops while improving accuracy through the adaptive correction of erroneous trajectories. STARS offers a robust, unsupervised mechanism to optimize the reasoning process of LRMs without requiring additional fine-tuning.

