---
layout: default
title: UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning
---

# UI-Ins: Enhancing GUI Grounding with Multi-Perspective Instruction-as-Reasoning
**arXiv**：[2510.20286v1](https://arxiv.org/abs/2510.20286) · [PDF](https://arxiv.org/pdf/2510.20286.pdf)  
**作者**：Liangyu Chen, Hanzhang Zhou, Chenglin Cai, Jianan Zhang, Panrong Tong, Quyu Kong, Xu Zhang, Chen Liu, Yuqi Liu, Wenxuan Wang, Yue Wang, Qin Jin, Steven Hoi  

**一句话要点**：提出UI-Ins方法以增强GUI grounding，通过多视角指令推理提升性能。

**关键词**：GUI grounding, 指令推理, 强化学习, 多视角学习, UI代理

## 3 点简述
- 核心问题：现有GUI grounding方法忽视指令多样性和质量，导致性能受限。
- 方法要点：采用指令即推理范式，结合SFT和RL训练，优化推理路径选择。
- 实验效果：在多个基准测试中达到SOTA，UI-Ins-32B在UI-I2E-Bench准确率达87.3%。

## 摘要（原文）

> GUI grounding, which maps natural-language instructions to actionable UI
> elements, is a core capability of GUI agents. Prior works largely treats
> instructions as a static proxy for user intent, overlooking the impact of
> instruction diversity and quality on grounding performance. Through a careful
> investigation of existing grounding datasets, we find a 23.3% flaw rate in
> their instructions and show that inference-time exploitation of instruction
> diversity yields up to a substantial 76% relative performance improvement. In
> this paper, we introduce the Instruction-as-Reasoning paradigm, treating
> instructions as dynamic analytical pathways that offer distinct perspectives
> and enabling the model to select the most effective pathway during reasoning.
> To achieve this, we propose a two-stage training framework: supervised
> fine-tuning (SFT) on synthesized, diverse instructions to instill
> multi-perspective reasoning, followed by reinforcement learning (RL) to
> optimize pathway selection and composition. Our resulting models, UI-Ins-7B and
> UI-Ins-32B, achieve state-of-the-art results on five challenging grounding
> benchmarks and exhibit emergent reasoning, selectively composing and
> synthesizing novel instruction pathways at inference. In particular, UI-Ins-32B
> attains the best grounding accuracy, scoring 87.3% on UI-I2E-Bench, 57.0% on
> ScreenSpot-Pro, and 84.9% on MMBench-GUI L2. Furthermore, our model
> demonstrates strong agentic potential, achieving a 74.1% success rate on
> AndroidWorld using UI-Ins-7B as the executor. Our in-depth analysis reveals
> additional insights such as how reasoning can be formulated to enhance rather
> than hinder grounding performance, and how our method mitigates policy collapse
> in the SFT+RL framework. All code and model checkpoints will be publicly
> released in https://github.com/alibaba/UI-Ins.

