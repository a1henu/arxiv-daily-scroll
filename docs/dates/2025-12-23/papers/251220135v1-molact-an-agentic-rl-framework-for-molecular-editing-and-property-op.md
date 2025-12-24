---
layout: default
title: MolAct: An Agentic RL Framework for Molecular Editing and Property Optimization
---

# MolAct: An Agentic RL Framework for Molecular Editing and Property Optimization
**arXiv**：[2512.20135v1](https://arxiv.org/abs/2512.20135) · [PDF](https://arxiv.org/pdf/2512.20135.pdf)  
**作者**：Zhuo Yang, Yeyun chen, Jiaqing Xie, Ben Gao, Shuaike Shen, Wanhao Liu, Liujia Yang, Beilun Wang, Tianfan Fu, Yuqiang Li  

**一句话要点**：提出MolAct框架，将分子编辑与优化建模为多步工具增强的Agentic强化学习问题。

**关键词**：分子编辑, 强化学习, Agentic框架, 工具增强, 属性优化

## 3 点简述
- 核心问题：分子编辑与优化需多步迭代，保持化学有效性和结构相似性。
- 方法要点：采用两阶段训练，先学习编辑能力，再重用行为进行属性优化。
- 实验效果：MolEditAgent在编辑任务中超越基线，MolOptAgent在LogP优化上优于Claude 3.7。

## 摘要（原文）

> Molecular editing and optimization are multi-step problems that require iteratively improving properties while keeping molecules chemically valid and structurally similar. We frame both tasks as sequential, tool-guided decisions and introduce MolAct, an agentic reinforcement learning framework that employs a two-stage training paradigm: first building editing capability, then optimizing properties while reusing the learned editing behaviors. To the best of our knowledge, this is the first work to formalize molecular design as an Agentic Reinforcement Learning problem, where an LLM agent learns to interleave reasoning, tool-use, and molecular optimization. The framework enables agents to interact in multiple turns, invoking chemical tools for validity checking, property assessment, and similarity control, and leverages their feedback to refine subsequent edits. We instantiate the MolAct framework to train two model families: MolEditAgent for molecular editing tasks and MolOptAgent for molecular optimization tasks. In molecular editing, MolEditAgent-7B delivers 100, 95, and 98 valid add, delete, and substitute edits, outperforming strong closed "thinking" baselines such as DeepSeek-R1; MolEditAgent-3B approaches the performance of much larger open "thinking" models like Qwen3-32B-think. In molecular optimization, MolOptAgent-7B (trained on MolEditAgent-7B) surpasses the best closed "thinking" baseline (e.g., Claude 3.7) on LogP and remains competitive on solubility, while maintaining balanced performance across other objectives. These results highlight that treating molecular design as a multi-step, tool-augmented process is key to reliable and interpretable improvements.

