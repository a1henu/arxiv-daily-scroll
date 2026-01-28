---
layout: default
title: Learning Adaptive Parallel Execution for Efficient Code Localization
---

# Learning Adaptive Parallel Execution for Efficient Code Localization
**arXiv**：[2601.19568v1](https://arxiv.org/abs/2601.19568) · [PDF](https://arxiv.org/pdf/2601.19568.pdf)  
**作者**：Ke Xu, Siyang Xiao, Ming Liang, Yichen Yu, Zhixiang Wang, Jingxuan Xu, Dajun Chen, Wei Jiang, Yong Li  

**一句话要点**：提出FuseSearch以解决代码定位中并行执行效率低下的问题

**关键词**：代码定位, 并行执行优化, 自适应搜索, 强化学习训练, 工具效率

## 3 点简述
- 核心问题：现有并行代码定位工具存在34.9%冗余调用率，抵消了并行化优势
- 方法要点：通过定义工具效率，采用SFT和RL两阶段训练学习自适应并行策略
- 实验或效果：在SWE-bench Verified上实现SOTA性能，加速93.6%，减少67.7%轮次和68.9%令牌

## 摘要（原文）

> Code localization constitutes a key bottleneck in automated software development pipelines. While concurrent tool execution can enhance discovery speed, current agents demonstrate a 34.9\% redundant invocation rate, which negates parallelism benefits. We propose \textbf{FuseSearch}, reformulating parallel code localization as a \textbf{joint quality-efficiency optimization} task. Through defining \textbf{tool efficiency} -- the ratio of unique information gain to invocation count -- we utilize a two-phase SFT and RL training approach for learning adaptive parallel strategies. Different from fixed-breadth approaches, FuseSearch dynamically modulates search breadth according to task context, evolving from exploration phases to refinement stages. Evaluated on SWE-bench Verified, FuseSearch-4B achieves SOTA-level performance (84.7\% file-level and 56.4\% function-level $F_1$ scores) with 93.6\% speedup, utilizing 67.7\% fewer turns and 68.9\% fewer tokens. Results indicate that efficiency-aware training naturally improves quality through eliminating noisy redundant signals, enabling high-performance cost-effective localization agents.

