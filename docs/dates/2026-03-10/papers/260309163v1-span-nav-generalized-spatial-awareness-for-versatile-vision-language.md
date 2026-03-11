---
layout: default
title: SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation
---

# SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation
**arXiv**：[2603.09163v1](https://arxiv.org/abs/2603.09163) · [PDF](https://arxiv.org/pdf/2603.09163.pdf)  
**作者**：Jiahang Liu, Tianyu Xu, Jiawei Chen, Lu Yue, Jiazhao Zhang, Zhiyong Wang, Minghan Li, Qisheng Zhao, Anqi Li, Qi Su, Zhizheng Zhang, He Wang  

**一句话要点**：提出SPAN-Nav以增强视觉语言导航中的通用空间感知能力

**关键词**：视觉语言导航, 空间感知, 占用预测, 端到端模型, 多任务协同训练

## 3 点简述
- 核心问题：现有视觉语言导航方法在复杂环境中因空间感知不足导致路径规划不可靠。
- 方法要点：通过占用预测任务提取空间先验，使用单令牌紧凑表示并注入动作推理。
- 实验或效果：在三个基准测试中达到最先进性能，真实世界实验验证了鲁棒泛化性。

## 摘要（原文）

> Recent embodied navigation approaches leveraging Vision-Language Models (VLMs) demonstrate strong generalization in versatile Vision-Language Navigation (VLN). However, reliable path planning in complex environments remains challenging due to insufficient spatial awareness. In this work, we introduce SPAN-Nav, an end-to-end foundation model designed to infuse embodied navigation with universal 3D spatial awareness using RGB video streams. SPAN-Nav extracts spatial priors across diverse scenes through an occupancy prediction task on extensive indoor and outdoor environments. To mitigate the computational burden, we introduce a compact representation for spatial priors, finding that a single token is sufficient to encapsulate the coarse-grained cues essential for navigation tasks. Furthermore, inspired by the Chain-of-Thought (CoT) mechanism, SPAN-Nav utilizes this single spatial token to explicitly inject spatial cues into action reasoning through an end-to end framework. Leveraging multi-task co-training, SPAN-Nav captures task-adaptive cues from generalized spatial priors, enabling robust spatial awareness to generalize even to the task lacking explicit spatial supervision. To support comprehensive spatial learning, we present a massive dataset of 4.2 million occupancy annotations that covers both indoor and outdoor scenes across multi-type navigation tasks. SPAN-Nav achieves state-of-the-art performance across three benchmarks spanning diverse scenarios and varied navigation tasks. Finally, real-world experiments validate the robust generalization and practical reliability of our approach across complex physical scenarios.

