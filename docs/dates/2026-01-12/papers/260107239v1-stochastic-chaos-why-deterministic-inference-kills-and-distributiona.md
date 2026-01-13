---
layout: default
title: Stochastic CHAOS: Why Deterministic Inference Kills, and Distributional Variability Is the Heartbeat of Artifical Cognition
---

# Stochastic CHAOS: Why Deterministic Inference Kills, and Distributional Variability Is the Heartbeat of Artifical Cognition
**arXiv**：[2601.07239v1](https://arxiv.org/abs/2601.07239) · [PDF](https://arxiv.org/pdf/2601.07239.pdf)  
**作者**：Tanmay Joshi, Shourya Aggarwal, Anusa Saha, Aadi Pandey, Shreyash Dhoot, Vighnesh Rai, Raxit Goswami, Aman Chadha, Vinija Jain, Amitava Das  

**一句话要点**：提出Stochastic CHAOS方法，强调分布变异性对LLM认知的重要性，以解决确定性推理的局限性。

**关键词**：大语言模型推理, 不确定性建模, 分布变异性, 确定性推理, 安全对齐, 涌现能力

## 3 点简述
- 核心问题：确定性推理抑制LLM的不确定性建模、涌现能力和安全对齐，导致评估偏差。
- 方法要点：倡导Stochastic CHAOS，将分布变异性视为可测量和控制的信号，而非消除。
- 实验或效果：实证显示确定性推理低估能力与脆弱性，隐藏失败概率和安全风险，多路径推理退化。

## 摘要（原文）

> Deterministic inference is a comforting ideal in classical software: the same program on the same input should always produce the same output. As large language models move into real-world deployment, this ideal has been imported wholesale into inference stacks. Recent work from the Thinking Machines Lab has presented a detailed analysis of nondeterminism in LLM inference, showing how batch-invariant kernels and deterministic attention can enforce bitwise-identical outputs, positioning deterministic inference as a prerequisite for reproducibility and enterprise reliability.
>   In this paper, we take the opposite stance. We argue that, for LLMs, deterministic inference kills. It kills the ability to model uncertainty, suppresses emergent abilities, collapses reasoning into a single brittle path, and weakens safety alignment by hiding tail risks. LLMs implement conditional distributions over outputs, not fixed functions. Collapsing these distributions to a single canonical completion may appear reassuring, but it systematically conceals properties central to artificial cognition. We instead advocate Stochastic CHAOS, treating distributional variability as a signal to be measured and controlled.
>   Empirically, we show that deterministic inference is systematically misleading. Single-sample deterministic evaluation underestimates both capability and fragility, masking failure probability under paraphrases and noise. Phase-like transitions associated with emergent abilities disappear under greedy decoding. Multi-path reasoning degrades when forced onto deterministic backbones, reducing accuracy and diagnostic insight. Finally, deterministic evaluation underestimates safety risk by hiding rare but dangerous behaviors that appear only under multi-sample evaluation.

