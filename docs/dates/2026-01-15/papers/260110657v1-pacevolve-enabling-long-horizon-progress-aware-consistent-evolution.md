---
layout: default
title: PACEvolve: Enabling Long-Horizon Progress-Aware Consistent Evolution
---

# PACEvolve: Enabling Long-Horizon Progress-Aware Consistent Evolution
**arXiv**：[2601.10657v1](https://arxiv.org/abs/2601.10657) · [PDF](https://arxiv.org/pdf/2601.10657.pdf)  
**作者**：Minghao Yan, Bo Peng, Benjamin Coleman, Ziqi Chen, Zhouhang Xie, Zhankui He, Noveen Sachdeva, Isabella Ye, Weili Wang, Chi Wang, Ed H. Chi, Wang-Cheng Kang, Derek Zhiyuan Cheng, Beidou Wang  

**一句话要点**：提出PACEvolve框架以解决LLM进化搜索中的系统性失败模式，实现长视野一致进化。

**关键词**：进化搜索, 上下文管理, 动量回溯, 自适应采样, 长视野优化, LLM应用

## 3 点简述
- 核心问题：LLM进化搜索存在上下文污染、模式崩溃和弱协作三种失败模式，缺乏系统管理。
- 方法要点：结合分层上下文管理、动量回溯和自适应采样策略，动态协调搜索过程。
- 实验或效果：在LLM-SR和KernelBench上达到SOTA，并在Modded NanoGPT上发现超越记录的解决方案。

## 摘要（原文）

> Large Language Models (LLMs) have emerged as powerful operators for evolutionary search, yet the design of efficient search scaffolds remains ad hoc. While promising, current LLM-in-the-loop systems lack a systematic approach to managing the evolutionary process. We identify three distinct failure modes: Context Pollution, where experiment history biases future candidate generation; Mode Collapse, where agents stagnate in local minima due to poor exploration-exploitation balance; and Weak Collaboration, where rigid crossover strategies fail to leverage parallel search trajectories effectively. We introduce Progress-Aware Consistent Evolution (PACEvolve), a framework designed to robustly govern the agent's context and search dynamics, to address these challenges. PACEvolve combines hierarchical context management (HCM) with pruning to address context pollution; momentum-based backtracking (MBB) to escape local minima; and a self-adaptive sampling policy that unifies backtracking and crossover for dynamic search coordination (CE), allowing agents to balance internal refinement with cross-trajectory collaboration. We demonstrate that PACEvolve provides a systematic path to consistent, long-horizon self-improvement, achieving state-of-the-art results on LLM-SR and KernelBench, while discovering solutions surpassing the record on Modded NanoGPT.

