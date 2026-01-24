---
layout: default
title: TeNet: Text-to-Network for Compact Policy Synthesis
---

# TeNet: Text-to-Network for Compact Policy Synthesis
**arXiv**：[2601.15912v1](https://arxiv.org/abs/2601.15912) · [PDF](https://arxiv.org/pdf/2601.15912.pdf)  
**作者**：Ariyan Bighashdel, Kevin Sebastian Luck  

**一句话要点**：提出TeNet框架，通过文本条件化超网络从自然语言生成紧凑机器人策略，以解决实时控制中的部署难题。

**关键词**：文本到网络, 超网络, 机器人策略合成, 实时控制, 自然语言指令, 紧凑模型

## 3 点简述
- 核心问题：机器人基于自然语言指令的控制常依赖笨重模型或手工接口，难以实时部署。
- 方法要点：使用预训练LLM文本嵌入条件化超网络，一次性生成可执行策略，实现轻量高效控制。
- 实验或效果：在MuJoCo和Meta-World基准测试中，策略尺寸显著小于基线，支持多任务和元学习，性能强劲。

## 摘要（原文）

> Robots that follow natural-language instructions often either plan at a high level using hand-designed interfaces or rely on large end-to-end models that are difficult to deploy for real-time control. We propose TeNet (Text-to-Network), a framework for instantiating compact, task-specific robot policies directly from natural language descriptions. TeNet conditions a hypernetwork on text embeddings produced by a pretrained large language model (LLM) to generate a fully executable policy, which then operates solely on low-dimensional state inputs at high control frequencies. By using the language only once at the policy instantiation time, TeNet inherits the general knowledge and paraphrasing robustness of pretrained LLMs while remaining lightweight and efficient at execution time. To improve generalization, we optionally ground language in behavior during training by aligning text embeddings with demonstrated actions, while requiring no demonstrations at inference time. Experiments on MuJoCo and Meta-World benchmarks show that TeNet produces policies that are orders of magnitude smaller than sequence-based baselines, while achieving strong performance in both multi-task and meta-learning settings and supporting high-frequency control. These results show that text-conditioned hypernetworks offer a practical way to build compact, language-driven controllers for ressource-constrained robot control tasks with real-time requirements.

