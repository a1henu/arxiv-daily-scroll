---
layout: default
title: Social-R1: Towards Human-like Social Reasoning in LLMs
---

# Social-R1: Towards Human-like Social Reasoning in LLMs
**arXiv**：[2603.09249v1](https://arxiv.org/abs/2603.09249) · [PDF](https://arxiv.org/pdf/2603.09249.pdf)  
**作者**：Jincenzi Wu, Yuxuan Lei, Jianxun Lian, Yitian Huang, Lexin Zhou, Haotian Li, Xing Xie, Helen Meng  

**一句话要点**：提出Social-R1强化学习框架，通过轨迹级对齐提升大语言模型的社会推理能力。

**关键词**：社会推理, 强化学习, 轨迹对齐, 对抗基准, 模型泛化

## 3 点简述
- 核心问题：大语言模型的社会智能不足，依赖表面模式而非深层推理，影响人机协作。
- 方法要点：引入ToMBench-Hard对抗基准，Social-R1框架通过多维奖励监督推理过程，实现结构对齐。
- 实验或效果：4B参数模型超越更大模型，在八个基准上泛化稳健，证明高效社会智能路径。

## 摘要（原文）

> While large language models demonstrate remarkable capabilities across numerous domains, social intelligence - the capacity to perceive social cues, infer mental states, and generate appropriate responses - remains a critical challenge, particularly for enabling effective human-AI collaboration and developing AI that truly serves human needs. Current models often rely on superficial patterns rather than genuine social reasoning. We argue that cultivating human-like social intelligence requires training with challenging cases that resist shortcut solutions. To this end, we introduce ToMBench-Hard, an adversarial benchmark designed to provide hard training examples for social reasoning. Building on this, we propose Social-R1, a reinforcement learning framework that aligns model reasoning with human cognition through multi-dimensional rewards. Unlike outcome-based RL, Social-R1 supervises the entire reasoning process, enforcing structural alignment, logical integrity, and information density. Results show that our approach enables a 4B parameter model to surpass much larger counterparts and generalize robustly across eight diverse benchmarks. These findings demonstrate that challenging training cases with trajectory-level alignment offer a path toward efficient and reliable social intelligence.

