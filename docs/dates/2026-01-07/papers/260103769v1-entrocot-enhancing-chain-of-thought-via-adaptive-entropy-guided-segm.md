---
layout: default
title: EntroCoT: Enhancing Chain-of-Thought via Adaptive Entropy-Guided Segmentation
---

# EntroCoT: Enhancing Chain-of-Thought via Adaptive Entropy-Guided Segmentation
**arXiv**：[2601.03769v1](https://arxiv.org/abs/2601.03769) · [PDF](https://arxiv.org/pdf/2601.03769.pdf)  
**作者**：Zihang Li, Yuhang Wang, Yikun Zong, Wenhan Yu, Xiaokun Yuan, Runhan Jiang, Zirui Liu, Tong Yang, Arthur Jiang  

**一句话要点**：提出EntroCoT框架，通过自适应熵引导分割和蒙特卡洛评估，解决CoT监督数据中推理步骤质量低的问题。

**关键词**：链式思维提示, 推理轨迹分割, 蒙特卡洛评估, 数据质量过滤, 数学推理, 微调优化

## 3 点简述
- 核心问题：现有CoT微调数据存在答案正确但推理步骤错误或冗余的问题。
- 方法要点：基于熵机制分割推理轨迹，蒙特卡洛评估步骤贡献，过滤低质量样本。
- 实验或效果：在数学基准测试中，微调于EntroCoT构建的高质量数据集优于全数据集基线。

## 摘要（原文）

> Chain-of-Thought (CoT) prompting has significantly enhanced the mathematical reasoning capabilities of Large Language Models. We find existing fine-tuning datasets frequently suffer from the "answer right but reasoning wrong" probelm, where correct final answers are derived from hallucinated, redundant, or logically invalid intermediate steps. This paper proposes EntroCoT, a unified framework for automatically identifying and refining low-quality CoT supervision traces. EntroCoT first proposes an entropy-based mechanism to segment the reasoning trace into multiple steps at uncertain junctures, and then introduces a Monte Carlo rollout-based mechanism to evaluate the marginal contribution of each step. By accurately filtering deceptive reasoning samples, EntroCoT constructs a high-quality dataset where every intermediate step in each reasoning trace facilitates the final answer. Extensive experiments on mathematical benchmarks demonstrate that fine-tuning on the subset constructed by EntroCoT consistently outperforms the baseslines of full-dataset supervision.

