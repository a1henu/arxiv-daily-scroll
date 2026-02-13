---
layout: default
title: Improving HPC Code Generation Capability of LLMs via Online Reinforcement Learning with Real-Machine Benchmark Rewards
---

# Improving HPC Code Generation Capability of LLMs via Online Reinforcement Learning with Real-Machine Benchmark Rewards
**arXiv**：[2602.12049v1](https://arxiv.org/abs/2602.12049) · [PDF](https://arxiv.org/pdf/2602.12049.pdf)  
**作者**：Ryo Mikasa, Shun-ichiro Hayashi, Daichi Mukunoki, Tetsuya Hoshino, Takahiro Katagiri  

**一句话要点**：提出在线强化学习方法，结合实时性能反馈与分阶段优化，提升LLM的HPC代码生成能力。

**关键词**：高性能计算, 代码生成, 强化学习, 在线训练, 性能优化, 分阶段算法

## 3 点简述
- 核心问题：LLM生成的代码在HPC领域运行时性能无保证，缺乏基于性能奖励的训练尝试。
- 方法要点：在线强化学习，在超算上执行代码并以GFLOPS作为奖励，引入分阶段质量多样性算法。
- 实验或效果：训练Qwen2.5 Coder 14B于矩阵乘法任务，结合GRPO，实验显示方法能提升代码生成能力。

## 摘要（原文）

> Large language models (LLMs) have demonstrated strong code generation capabilities, yet the runtime performance of generated code is not guaranteed, and there have been few attempts to train LLMs using runtime performance as a reward in the HPC domain. We propose an online reinforcement learning approach that executes LLM-generated code on a supercomputer and directly feeds back the measured runtime performance (GFLOPS) as a reward. We further introduce a Staged Quality-Diversity (SQD) algorithm that progressively varies the permitted optimization techniques on a per-problem basis, enabling the model to learn code optimization from diverse perspectives. We build a distributed system connecting a GPU training cluster with a CPU benchmarking cluster, and train Qwen2.5 Coder 14B on a double-precision matrix multiplication task using Group Relative Policy Optimization (GRPO). Through two experiments, we show that reinforcement learning combining runtime performance feedback with staged optimization can improve the HPC code generation capability of LLMs.

