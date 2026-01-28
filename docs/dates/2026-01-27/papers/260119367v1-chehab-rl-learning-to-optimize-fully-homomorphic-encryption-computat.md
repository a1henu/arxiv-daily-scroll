---
layout: default
title: CHEHAB RL: Learning to Optimize Fully Homomorphic Encryption Computations
---

# CHEHAB RL: Learning to Optimize Fully Homomorphic Encryption Computations
**arXiv**：[2601.19367v1](https://arxiv.org/abs/2601.19367) · [PDF](https://arxiv.org/pdf/2601.19367.pdf)  
**作者**：Bilel Sefsaf, Abderraouf Dandani, Abdessamed Seddiki, Arab Mohammed, Eduardo Chielle, Michail Maniatakos, Riyadh Baghdadi  

**一句话要点**：提出CHEHAB RL框架，利用深度强化学习自动化优化全同态加密代码编译。

**关键词**：全同态加密, 深度强化学习, 代码优化, 编译器, 向量化, 噪声管理

## 3 点简述
- 全同态加密计算成本高，手动优化代码复杂且需密码学专业知识。
- 采用深度强化学习训练代理，学习应用重写规则序列以自动向量化代码并降低延迟与噪声增长。
- 实验显示，相比Coyote编译器，生成代码执行快5.3倍、噪声累积少2.54倍、编译过程快27.9倍。

## 摘要（原文）

> Fully Homomorphic Encryption (FHE) enables computations directly on encrypted data, but its high computational cost remains a significant barrier. Writing efficient FHE code is a complex task requiring cryptographic expertise, and finding the optimal sequence of program transformations is often intractable. In this paper, we propose CHEHAB RL, a novel framework that leverages deep reinforcement learning (RL) to automate FHE code optimization. Instead of relying on predefined heuristics or combinatorial search, our method trains an RL agent to learn an effective policy for applying a sequence of rewriting rules to automatically vectorize scalar FHE code while reducing instruction latency and noise growth. The proposed approach supports the optimization of both structured and unstructured code. To train the agent, we synthesize a diverse dataset of computations using a large language model (LLM). We integrate our proposed approach into the CHEHAB FHE compiler and evaluate it on a suite of benchmarks, comparing its performance against Coyote, a state-of-the-art vectorizing FHE compiler. The results show that our approach generates code that is $5.3\times$ faster in execution, accumulates $2.54\times$ less noise, while the compilation process itself is $27.9\times$ faster than Coyote (geometric means).

