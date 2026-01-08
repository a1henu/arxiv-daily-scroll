---
layout: default
title: FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning
---

# FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning
**arXiv**：[2601.03938v1](https://arxiv.org/abs/2601.03938) · [PDF](https://arxiv.org/pdf/2601.03938.pdf)  
**作者**：Yujie Feng, Hao Wang, Jian Li, Xu Chu, Zhaolu Kang, Yiran Liu, Yasha Wang, Philip S. Yu, Xiao-Ming Wu  

**一句话要点**：提出FOREVER框架，基于遗忘曲线设计记忆回放以缓解大语言模型持续学习中的灾难性遗忘

**关键词**：持续学习, 灾难性遗忘, 记忆回放, 遗忘曲线, 大语言模型, 模型时间

## 3 点简述
- 核心问题：现有记忆回放方法依赖固定步长启发式，与模型实际学习进度不匹配，导致灾难性遗忘
- 方法要点：定义基于优化器更新幅度的模型时间，结合遗忘曲线调度回放时机和强度感知正则化机制
- 实验或效果：在三个持续学习基准和0.6B至13B参数模型上验证，FOREVER能一致缓解灾难性遗忘

## 摘要（原文）

> Continual learning (CL) for large language models (LLMs) aims to enable sequential knowledge acquisition without catastrophic forgetting. Memory replay methods are widely used for their practicality and effectiveness, but most rely on fixed, step-based heuristics that often misalign with the model's actual learning progress, since identical training steps can result in varying degrees of parameter change. Motivated by recent findings that LLM forgetting mirrors the Ebbinghaus human forgetting curve, we propose FOREVER (FORgEtting curVe-inspired mEmory Replay), a novel CL framework that aligns replay schedules with a model-centric notion of time. FOREVER defines model time using the magnitude of optimizer updates, allowing forgetting curve-inspired replay intervals to align with the model's internal evolution rather than raw training steps. Building on this approach, FOREVER incorporates a forgetting curve-based replay scheduler to determine when to replay and an intensity-aware regularization mechanism to adaptively control how to replay. Extensive experiments on three CL benchmarks and models ranging from 0.6B to 13B parameters demonstrate that FOREVER consistently mitigates catastrophic forgetting.

