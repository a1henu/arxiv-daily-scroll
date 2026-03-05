---
layout: default
title: Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory
---

# Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory
**arXiv**：[2603.04257v1](https://arxiv.org/abs/2603.04257) · [PDF](https://arxiv.org/pdf/2603.04257.pdf)  
**作者**：Zhenting Wang, Huancheng Chen, Jiayun Wang, Wei Wei  

**一句话要点**：提出Memex索引经验记忆机制，通过强化学习优化上下文压缩，解决长视野任务中LLM代理的上下文窗口瓶颈问题。

**关键词**：长视野任务, LLM代理, 索引记忆, 上下文压缩, 强化学习优化, 经验数据库

## 3 点简述
- 核心问题：LLM代理在长视野任务中受限于有限上下文窗口，导致轨迹增长时难以保留工具输出和中间推理，影响决策质量。
- 方法要点：引入Memex机制，维护紧凑工作上下文（结构化摘要和稳定索引），将完整交互存储在外部经验数据库中，通过索引解引用恢复过去证据。
- 实验或效果：在挑战性长视野任务上，Memex代理使用显著更小的工作上下文，提高了任务成功率，相比仅摘要方法损失更少。

## 摘要（原文）

> Large language model (LLM) agents are fundamentally bottlenecked by finite context windows on long-horizon tasks. As trajectories grow, retaining tool outputs and intermediate reasoning in-context quickly becomes infeasible: the working context becomes prohibitively long, eventually exceeds the context budget, and makes distant evidence harder to use even when it is still present. Existing solutions typically shorten context through truncation or running summaries, but these methods are fundamentally lossy because they compress or discard past evidence itself. We introduce Memex, an indexed experience memory mechanism that instead compresses context without discarding evidence. Memex maintains a compact working context consisting of concise structured summaries and stable indices, while storing full-fidelity underlying interactions in an external experience database under those indices. The agent can then decide when to dereference an index and recover the exact past evidence needed for the current subgoal. We optimize both write and read behaviors with our reinforcement learning framework MemexRL, using reward shaping tailored to indexed memory usage under a context budget, so the agent learns what to summarize, what to archive, how to index it, and when to retrieve it. This yields a substantially less lossy form of long-horizon memory than summary-only approaches. We further provide a theoretical analysis showing the potential of the Memex loop to preserve decision quality with bounded dereferencing while keeping effective in-context computation bounded as history grows. Empirically, on challenging long-horizon tasks, Memex agent trained with MemexRL improves task success while using a significantly smaller working context.

