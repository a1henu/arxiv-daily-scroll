---
layout: default
title: EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis
---

# EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis
**arXiv**：[2601.05808v1](https://arxiv.org/abs/2601.05808) · [PDF](https://arxiv.org/pdf/2601.05808.pdf)  
**作者**：Xiaoshuai Song, Haofei Chang, Guanting Dong, Yutao Zhu, Zhicheng Dou, Ji-Rong Wen  

**一句话要点**：提出EnvScaler框架，通过程序合成扩展工具交互环境以训练LLM代理。

**关键词**：工具交互环境, 程序合成, LLM代理训练, 环境扩展, 监督微调, 强化学习

## 3 点简述
- 核心问题：LLM代理训练缺乏可扩展、多样化的工具交互环境，现有方法受限或不可靠。
- 方法要点：EnvScaler包括SkelBuilder构建环境骨架和ScenGenerator生成任务场景与验证函数。
- 实验或效果：合成191个环境和约7K场景，应用于Qwen3系列模型，在基准测试中显著提升LLM在复杂环境中的任务解决能力。

## 摘要（原文）

> Large language models (LLMs) are expected to be trained to act as agents in various real-world environments, but this process relies on rich and varied tool-interaction sandboxes. However, access to real systems is often restricted; LLM-simulated environments are prone to hallucinations and inconsistencies; and manually built sandboxes are hard to scale. In this paper, we propose EnvScaler, an automated framework for scalable tool-interaction environments via programmatic synthesis. EnvScaler comprises two components. First, SkelBuilder constructs diverse environment skeletons through topic mining, logic modeling, and quality evaluation. Then, ScenGenerator generates multiple task scenarios and rule-based trajectory validation functions for each environment. With EnvScaler, we synthesize 191 environments and about 7K scenarios, and apply them to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) for Qwen3 series models. Results on three benchmarks show that EnvScaler significantly improves LLMs' ability to solve tasks in complex environments involving multi-turn, multi-tool interactions. We release our code and data at https://github.com/RUC-NLPIR/EnvScaler.

