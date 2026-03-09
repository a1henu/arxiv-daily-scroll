---
layout: default
title: ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning
---

# ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning
**arXiv**：[2603.05863v1](https://arxiv.org/abs/2603.05863) · [PDF](https://arxiv.org/pdf/2603.05863.pdf)  
**作者**：Juyong Jiang, Jiasi Shen, Sunghun Kim, Kang Min Yoo, Jeonghoon Kim, Sungju Kim  

**一句话要点**：提出ReflexiCoder框架，通过强化学习使大语言模型在推理时自主反思与修正生成代码

**关键词**：代码生成, 强化学习, 自我反思, 自主修正, 推理优化

## 3 点简述
- 核心问题：大语言模型在复杂算法任务中单次生成代码性能受限，现有方法依赖外部反馈或计算成本高
- 方法要点：采用强化学习训练模型内化反思-修正轨迹，实现推理时无需外部反馈的自主调试能力
- 实验或效果：在多个基准测试中达到开源模型新SOTA，推理时计算开销降低约40%

## 摘要（原文）

> While Large Language Models (LLMs) have revolutionized code generation, standard "System 1" approaches, generating solutions in a single forward pass, often hit a performance ceiling when faced with complex algorithmic tasks. Existing iterative refinement strategies attempt to bridge this gap at inference time, yet they predominantly rely on external oracles, execution feedback, or computationally expensive prompt-response cycles. In this work, we propose ReflexiCoder, a novel reinforcement learning (RL) framework that internalizes the structured reasoning trajectory, encompassing initial generation, bug and optimization aware reflection, and self-correction, directly into the model's weights. Unlike prior methods, ReflexiCoder shifts the paradigm from external-dependent refinement to an intrinsic, fully autonomous self-reflection and self-correction capabilities at inference time. We utilize an RL-zero training paradigm with granular reward functions to optimize the entire reflection-correction trajectory, teaching the model how to debug without reliance on ground-truth feedback or execution engines at inference time. Extensive experiments across seven benchmarks demonstrate that our ReflexiCoder-8B establishes a new state-of-the-art (SOTA) among leading open-source models in the 1.5B-14B range, achieving 94.51% (87.20%) on HumanEval (Plus), 81.80% (78.57%) on MBPP (Plus), 35.00% on BigCodeBench, 52.21% on LiveCodeBench, and 37.34% on CodeForces in a single-attempt setting, rivaling or surpassing proprietary models like GPT-5.1. Notably, our framework is significantly more token-efficient than base models, reducing inference-time compute overhead by approximately 40% through disciplined, high-speed reasoning and reflection patterns. Source code is available at https://github.com/juyongjiang/ReflexiCoder.

