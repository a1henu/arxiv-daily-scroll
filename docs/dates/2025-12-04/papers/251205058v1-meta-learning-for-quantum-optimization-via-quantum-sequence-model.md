---
layout: default
title: Meta-Learning for Quantum Optimization via Quantum Sequence Model
---

# Meta-Learning for Quantum Optimization via Quantum Sequence Model
**arXiv**：[2512.05058v1](https://arxiv.org/abs/2512.05058) · [PDF](https://arxiv.org/pdf/2512.05058.pdf)  
**作者**：Yu-Cheng Lin, Yu-Chao Hsu, Samuel Yen-Chi Chen  

**一句话要点**：提出量子元学习框架，通过量子序列模型优化QAOA参数初始化以解决组合优化问题。

**关键词**：量子近似优化算法, 元学习, 量子序列模型, 参数初始化, 组合优化, 量子核

## 3 点简述
- 核心问题：QAOA中变分参数优化困难，导致收敛慢和解质量差。
- 方法要点：训练量子序列模型（如QK-LSTM）作为元学习优化器，生成高效参数初始化策略。
- 实验或效果：在Max-Cut问题上，QK-LSTM实现最高近似比和最快收敛，参数可迁移性强。

## 摘要（原文）

> The Quantum Approximate Optimization Algorithm (QAOA) is a leading approach for solving combinatorial optimization problems on near-term quantum processors. However, finding good variational parameters remains a significant challenge due to the non-convex energy landscape, often resulting in slow convergence and poor solution quality. In this work, we propose a quantum meta-learning framework that trains advanced quantum sequence models to generate effective parameter initialization policies. We investigate four classical or quantum sequence models, including the Quantum Kernel-based Long Short-Term Memory (QK-LSTM), as learned optimizers in a "learning to learn" paradigm. Our numerical experiments on the Max-Cut problem demonstrate that the QK-LSTM optimizer achieves superior performance, obtaining the highest approximation ratios and exhibiting the fastest convergence rate across all tested problem sizes (n=10 to 13). Crucially, the QK-LSTM model achieves perfect parameter transferability by synthesizing a single, fixed set of near-optimal parameters, leading to a remarkable sustained acceleration of convergence even when generalizing to larger problems. This capability, enabled by the compact and expressive power of the quantum kernel architecture, underscores its effectiveness. The QK-LSTM, with only 43 trainable parameters, substantially outperforms the classical LSTM (56 parameters) and other quantum sequence models, establishing a robust pathway toward highly efficient parameter initialization for variational quantum algorithms in the NISQ era.

