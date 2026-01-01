---
layout: default
title: Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time
---

# Understanding and Steering the Cognitive Behaviors of Reasoning Models at Test-Time
**arXiv**：[2512.24574v1](https://arxiv.org/abs/2512.24574) · [PDF](https://arxiv.org/pdf/2512.24574.pdf)  
**作者**：Zhenyu Zhang, Xiaoxia Wu, Zhongzhu Zhou, Qingyang Wu, Yineng Zhang, Pragaash Ponnusamy, Harikaran Subbaraj, Jue Wang, Shuaiwen Leon Song, Ben Athiwaratkun  

**一句话要点**：提出CREST方法，在推理时通过干预注意力头来提升大语言模型的推理效率与准确性。

**关键词**：推理优化, 注意力头干预, 训练无关方法, 认知行为分析, 大语言模型

## 3 点简述
- 核心问题：大语言模型推理轨迹低效，存在浅层或冗余步骤，导致高延迟和不稳定。
- 方法要点：离线校准识别认知头，推理时旋转隐藏表示以抑制低效行为，无需训练。
- 实验或效果：在多个基准测试中，准确率提升最高17.5%，令牌使用减少37.6%。

## 摘要（原文）

> Large Language Models (LLMs) often rely on long chain-of-thought (CoT) reasoning to solve complex tasks. While effective, these trajectories are frequently inefficient, leading to high latency from excessive token generation, or unstable reasoning that alternates between underthinking (shallow, inconsistent steps) and overthinking (repetitive, verbose reasoning). In this work, we study the structure of reasoning trajectories and uncover specialized attention heads that correlate with distinct cognitive behaviors such as verification and backtracking. By lightly intervening on these heads at inference time, we can steer the model away from inefficient modes. Building on this insight, we propose CREST, a training-free method for Cognitive REasoning Steering at Test-time. CREST has two components: (1) an offline calibration step that identifies cognitive heads and derives head-specific steering vectors, and (2) an inference-time procedure that rotates hidden representations to suppress components along those vectors. CREST adaptively suppresses unproductive reasoning behaviors, yielding both higher accuracy and lower computational cost. Across diverse reasoning benchmarks and models, CREST improves accuracy by up to 17.5% while reducing token usage by 37.6%, offering a simple and effective pathway to faster, more reliable LLM reasoning.

