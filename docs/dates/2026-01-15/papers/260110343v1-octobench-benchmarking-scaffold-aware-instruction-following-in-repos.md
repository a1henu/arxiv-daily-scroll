---
layout: default
title: OctoBench: Benchmarking Scaffold-Aware Instruction Following in Repository-Grounded Agentic Coding
---

# OctoBench: Benchmarking Scaffold-Aware Instruction Following in Repository-Grounded Agentic Coding
**arXiv**：[2601.10343v1](https://arxiv.org/abs/2601.10343) · [PDF](https://arxiv.org/pdf/2601.10343.pdf)  
**作者**：Deming Ding, Shichun Liu, Enhui Yang, Jiahang Lin, Ziying Chen, Shihan Dou, Honglin Guo, Weiyu Cheng, Pengyu Zhao, Chengjun Xiao, Qunhong Zeng, Qi Zhang, Xuanjing Huang, Qidi Xu, Tao Gui  

**一句话要点**：提出OctoBench基准以评估仓库基础代理编码中脚手架感知指令遵循能力

**关键词**：代理编码, 指令遵循基准, 仓库基础任务, 脚手架感知评估, 自动化评分

## 3 点简述
- 核心问题：现代编码脚手架将LLMs转化为软件代理，但其遵循脚手架指定指令的能力在异构约束下未充分评估
- 方法要点：引入OctoBench，包含34个环境和217个任务，提供自动观察与评分工具包进行细粒度检查
- 实验或效果：在八个代表性模型上实验，揭示任务解决与脚手架感知合规性之间的系统性差距

## 摘要（原文）

> Modern coding scaffolds turn LLMs into capable software agents, but their ability to follow scaffold-specified instructions remains under-examined, especially when constraints are heterogeneous and persist across interactions. To fill this gap, we introduce OctoBench, which benchmarks scaffold-aware instruction following in repository-grounded agentic coding. OctoBench includes 34 environments and 217 tasks instantiated under three scaffold types, and is paired with 7,098 objective checklist items. To disentangle solving the task from following the rules, we provide an automated observation-and-scoring toolkit that captures full trajectories and performs fine-grained checks. Experiments on eight representative models reveal a systematic gap between task-solving and scaffold-aware compliance, underscoring the need for training and evaluation that explicitly targets heterogeneous instruction following. We release the benchmark to support reproducible benchmarking and to accelerate the development of more scaffold-aware coding agents.

