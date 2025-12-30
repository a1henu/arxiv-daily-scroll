---
layout: default
title: Agentic Physical AI toward a Domain-Specific Foundation Model for Nuclear Reactor Control
---

# Agentic Physical AI toward a Domain-Specific Foundation Model for Nuclear Reactor Control
**arXiv**：[2512.23292v1](https://arxiv.org/abs/2512.23292) · [PDF](https://arxiv.org/pdf/2512.23292.pdf)  
**作者**：Yoonpyo Lee, Kazuma Kobayashi, Sai Puppala, Sajedul Talukder, Seid Koric, Souvik Chakraborty, Syed Bahauddin Alam  

**一句话要点**：提出基于物理验证的Agentic Physical AI，构建核反应堆控制领域专用基础模型。

**关键词**：Agentic Physical AI, 领域专用基础模型, 核反应堆控制, 物理验证, 方差崩溃, 紧凑语言模型

## 3 点简述
- 通用基础模型在物理系统控制中因结构限制导致输入不忠实，准确率仅50-53%。
- 采用紧凑语言模型，通过物理验证驱动策略优化，而非感知推理。
- 训练360M参数模型，数据集从10^3扩展到10^5，实现方差崩溃和稳定执行。

## 摘要（原文）

> The prevailing paradigm in AI for physical systems, scaling general-purpose foundation models toward universal multimodal reasoning, confronts a fundamental barrier at the control interface. Recent benchmarks show that even frontier vision-language models achieve only 50-53% accuracy on basic quantitative physics tasks, behaving as approximate guessers that preserve semantic plausibility while violating physical constraints. This input unfaithfulness is not a scaling deficiency but a structural limitation. Perception-centric architectures optimize parameter-space imitation, whereas safety-critical control demands outcome-space guarantees over executed actions. Here, we present a fundamentally different pathway toward domain-specific foundation models by introducing compact language models operating as Agentic Physical AI, in which policy optimization is driven by physics-based validation rather than perceptual inference. We train a 360-million-parameter model on synthetic reactor control scenarios, scaling the dataset from 10^3 to 10^5 examples. This induces a sharp phase transition absent in general-purpose models. Small-scale systems exhibit high-variance imitation with catastrophic tail risk, while large-scale models undergo variance collapse exceeding 500x reduction, stabilizing execution-level behavior. Despite balanced exposure to four actuation families, the model autonomously rejects approximately 70% of the training distribution and concentrates 95% of runtime execution on a single-bank strategy. Learned representations transfer across distinct physics and continuous input modalities without architectural modification.

