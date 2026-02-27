---
layout: default
title: FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning
---

# FactGuard: Agentic Video Misinformation Detection via Reinforcement Learning
**arXiv**：[2602.22963v1](https://arxiv.org/abs/2602.22963) · [PDF](https://arxiv.org/pdf/2602.22963.pdf)  
**作者**：Zehao Li, Hongwei Yu, Hao Jiang, Qiang Sheng, Yilong Xu, Baolong Bi, Yang Li, Zhenlong Yuan, Yujun Cai, Zhaoqi Wang  

**一句话要点**：提出FactGuard框架，通过强化学习优化视频虚假信息检测中的工具调用与决策校准。

**关键词**：视频虚假信息检测, 多模态大语言模型, 强化学习, 工具调用, 迭代推理, 决策校准

## 3 点简述
- 核心问题：MLLMs在视频虚假信息检测中依赖固定深度推理，对内部假设过度信任，证据稀疏时效果受限。
- 方法要点：构建基于MLLMs的迭代推理框架，评估任务模糊性并选择性调用外部工具，采用两阶段训练策略结合监督微调与强化学习。
- 实验或效果：在FakeSV、FakeTT和FakeVV数据集上实现SOTA性能，验证了优秀的鲁棒性和泛化能力。

## 摘要（原文）

> Multimodal large language models (MLLMs) have substantially advanced video misinformation detection through unified multimodal reasoning, but they often rely on fixed-depth inference and place excessive trust in internally generated assumptions, particularly in scenarios where critical evidence is sparse, fragmented, or requires external verification. To address these limitations, we propose FactGuard, an agentic framework for video misinformation detection that formulates verification as an iterative reasoning process built upon MLLMs. FactGuard explicitly assesses task ambiguity and selectively invokes external tools to acquire critical evidence, enabling progressive refinement of reasoning trajectories. To further strengthen this capability, we introduce a two-stage training strategy that combines domain-specific agentic supervised fine-tuning with decision-aware reinforcement learning to optimize tool usage and calibrate risk-sensitive decision making. Extensive experiments on FakeSV, FakeTT, and FakeVV demonstrate FactGuard's state-of-the-art performance and validate its excellent robustness and generalization capacity.

