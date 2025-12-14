---
layout: default
title: AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management
---

# AgentProg: Empowering Long-Horizon GUI Agents with Program-Guided Context Management
**arXiv**：[2512.10371v1](https://arxiv.org/abs/2512.10371) · [PDF](https://arxiv.org/pdf/2512.10371.pdf)  
**作者**：Shizuo Tian, Hao Wen, Yuxuan Chen, Jiacheng Liu, Shanhui Zhao, Guohong Liu, Ju Ren, Yunxin Liu, Yuanchun Li  

**一句话要点**：提出AgentProg，通过程序引导的上下文管理解决长时程GUI代理任务中的上下文开销问题。

**关键词**：GUI代理, 上下文管理, 程序引导, 长时程任务, 信念状态, 移动自动化

## 3 点简述
- 核心问题：长时程GUI代理任务中，依赖不断扩展的交互历史导致上下文开销大，现有压缩技术易丢失关键语义信息。
- 方法要点：将交互历史重构为带变量和控制流的程序，基于程序结构决定信息保留与丢弃，并集成全局信念状态机制处理部分可观测性和环境变化。
- 实验或效果：在AndroidWorld和扩展长时程任务套件上实现最优成功率，保持稳健性能，而基线方法性能严重下降。

## 摘要（原文）

> The rapid development of mobile GUI agents has stimulated growing research interest in long-horizon task automation. However, building agents for these tasks faces a critical bottleneck: the reliance on ever-expanding interaction history incurs substantial context overhead. Existing context management and compression techniques often fail to preserve vital semantic information, leading to degraded task performance. We propose AgentProg, a program-guided approach for agent context management that reframes the interaction history as a program with variables and control flow. By organizing information according to the structure of program, this structure provides a principled mechanism to determine which information should be retained and which can be discarded. We further integrate a global belief state mechanism inspired by Belief MDP framework to handle partial observability and adapt to unexpected environmental changes. Experiments on AndroidWorld and our extended long-horizon task suite demonstrate that AgentProg has achieved the state-of-the-art success rates on these benchmarks. More importantly, it maintains robust performance on long-horizon tasks while baseline methods experience catastrophic degradation. Our system is open-sourced at https://github.com/MobileLLM/AgentProg.

