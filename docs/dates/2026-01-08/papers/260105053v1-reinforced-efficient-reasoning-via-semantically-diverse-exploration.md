---
layout: default
title: Reinforced Efficient Reasoning via Semantically Diverse Exploration
---

# Reinforced Efficient Reasoning via Semantically Diverse Exploration
**arXiv**：[2601.05053v1](https://arxiv.org/abs/2601.05053) · [PDF](https://arxiv.org/pdf/2601.05053.pdf)  
**作者**：Ziqi Zhao, Zhaochun Ren, Jiahong Zou, Liu Yang, Zhiwei Xu, Xuri Ge, Zhumin Chen, Xinyu Ma, Daiting Shi, Shuaiqiang Wang, Dawei Yin, Xin Xin  

**一句话要点**：提出ROSE方法以增强大语言模型推理的探索多样性和效率

**关键词**：强化学习, 大语言模型推理, 蒙特卡洛树搜索, 语义多样性探索, 数学推理

## 3 点简述
- 现有基于MCTS的强化学习方法存在探索多样性不足和推理效率低的问题
- ROSE引入语义熵分支策略和ε探索机制以促进多样化探索，并设计长度感知优势估计器提升效率
- 在数学推理基准测试中验证了ROSE的有效性和效率，代码已开源

## 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has proven effective in enhancing the reasoning of large language models (LLMs). Monte Carlo Tree Search (MCTS)-based extensions improve upon vanilla RLVR (e.g., GRPO) by providing tree-based reasoning rollouts that enable fine-grained and segment-level credit assignment. However, existing methods still suffer from limited exploration diversity and inefficient reasoning. To address the above challenges, we propose reinforced efficient reasoning via semantically diverse explorations, i.e., ROSE, for LLMs. To encourage more diverse reasoning exploration, our method incorporates a semantic-entropy-based branching strategy and an $\varepsilon$-exploration mechanism. The former operates on already sampled reasoning rollouts to capture semantic uncertainty and select branching points with high semantic divergence to generate new successive reasoning paths, whereas the latter stochastically initiates reasoning rollouts from the root, preventing the search process from becoming overly local. To improve efficiency, we design a length-aware segment-level advantage estimator that rewards concise and correct reasoning while penalizing unnecessarily long reasoning chains. Extensive experiments on various mathematical reasoning benchmarks with Qwen and Llama models validate the effectiveness and efficiency of ROSE. Codes are available at https://github.com/ZiqiZhao1/ROSE-rl.

