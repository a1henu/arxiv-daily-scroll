---
layout: default
title: SWE-Replay: Efficient Test-Time Scaling for Software Engineering Agents
---

# SWE-Replay: Efficient Test-Time Scaling for Software Engineering Agents
**arXiv**：[2601.22129v1](https://arxiv.org/abs/2601.22129) · [PDF](https://arxiv.org/pdf/2601.22129.pdf)  
**作者**：Yifeng Ding, Lingming Zhang  

**一句话要点**：提出SWE-Replay以高效扩展软件工程代理的测试时能力

**关键词**：软件工程代理, 测试时扩展, 轨迹重用, 动态探索, 成本优化, 泛化性验证

## 3 点简述
- 核心问题：现有测试时扩展方法计算成本高，且依赖可能不准确的价值估计，难以泛化到现代代理。
- 方法要点：通过重用先前试验轨迹，动态选择从零探索或利用存档经验，基于仓库探索潜力和推理意义选择中间步骤。
- 实验或效果：在SWE-Bench Verified上，成本降低达17.4%，性能提升达3.8%，并在其他基准验证了泛化性。

## 摘要（原文）

> Test-time scaling has been widely adopted to enhance the capabilities of Large Language Model (LLM) agents in software engineering (SWE) tasks. However, the standard approach of repeatedly sampling trajectories from scratch is computationally expensive. While recent methods have attempted to mitigate costs using specialized value agents, they can suffer from model miscalibration and fail to generalize to modern agents that synthesize custom bash scripts as tools. In this paper, we introduce SWE-Replay, the first efficient and generalizable test-time scaling technique for modern agents without reliance on potentially noisy value estimates. SWE-Replay optimizes the scaling process by recycling trajectories from prior trials, dynamically choosing to either explore from scratch or exploit archived experience by branching at critical intermediate steps. This selection of intermediate steps is driven by the potential and reasoning significance of repository exploration, rather than external LLM-based quality estimates. Our evaluation shows that, on SWE-Bench Verified, SWE-Replay consistently outperforms naive scaling, reducing costs by up to 17.4% while maintaining or even improving performance by up to 3.8%. Further evaluation on SWE-Bench Pro and Multilingual validates the generalizability of SWE-Replay, establishing it as a robust foundation for efficient test-time scaling of software engineering agents.

