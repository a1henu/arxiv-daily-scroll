---
layout: default
title: MATA: A Trainable Hierarchical Automaton System for Multi-Agent Visual Reasoning
---

# MATA: A Trainable Hierarchical Automaton System for Multi-Agent Visual Reasoning
**arXiv**：[2601.19204v1](https://arxiv.org/abs/2601.19204) · [PDF](https://arxiv.org/pdf/2601.19204.pdf)  
**作者**：Zhixi Cai, Fucai Ke, Kevin Leo, Sukai Huang, Maria Garcia de la Banda, Peter J. Stuckey, Hamid Rezatofighi  

**一句话要点**：提出MATA系统以解决多智能体视觉推理中的协作与竞争决策问题

**关键词**：多智能体系统, 视觉推理, 分层自动机, 可训练超智能体, 透明执行历史, 监督微调数据集

## 3 点简述
- 核心问题：现有视觉语言模型推理隐式且易产生幻觉，组合方法依赖单智能体或手工流程，难以动态决定智能体协作或竞争。
- 方法要点：MATA采用分层有限状态自动机，顶层由可训练超智能体控制状态转移，每个智能体运行基于规则的子自动机，共享内存实现透明执行历史。
- 实验或效果：在多个视觉推理基准测试中，MATA相比单体和组合基线达到最先进结果，代码和数据集已开源。

## 摘要（原文）

> Recent vision-language models have strong perceptual ability but their implicit reasoning is hard to explain and easily generates hallucinations on complex queries. Compositional methods improve interpretability, but most rely on a single agent or hand-crafted pipeline and cannot decide when to collaborate across complementary agents or compete among overlapping ones. We introduce MATA (Multi-Agent hierarchical Trainable Automaton), a multi-agent system presented as a hierarchical finite-state automaton for visual reasoning whose top-level transitions are chosen by a trainable hyper agent. Each agent corresponds to a state in the hyper automaton, and runs a small rule-based sub-automaton for reliable micro-control. All agents read and write a shared memory, yielding transparent execution history. To supervise the hyper agent's transition policy, we build transition-trajectory trees and transform to memory-to-next-state pairs, forming the MATA-SFT-90K dataset for supervised finetuning (SFT). The finetuned LLM as the transition policy understands the query and the capacity of agents, and it can efficiently choose the optimal agent to solve the task. Across multiple visual reasoning benchmarks, MATA achieves the state-of-the-art results compared with monolithic and compositional baselines. The code and dataset are available at https://github.com/ControlNet/MATA.

