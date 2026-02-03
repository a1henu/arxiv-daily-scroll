---
layout: default
title: Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization
---

# Bandwidth-Efficient Multi-Agent Communication through Information Bottleneck and Vector Quantization
**arXiv**：[2602.02035v1](https://arxiv.org/abs/2602.02035) · [PDF](https://arxiv.org/pdf/2602.02035.pdf)  
**作者**：Ahmad Farooq, Kamran Iqbal  

**一句话要点**：提出结合信息瓶颈与矢量量化的框架，以解决多智能体强化学习在带宽受限环境中的通信效率问题。

**关键词**：多智能体强化学习, 信息瓶颈, 矢量量化, 带宽效率, 门控通信, 机器人协调

## 3 点简述
- 核心问题：多智能体强化学习在真实机器人应用中面临严重通信约束，影响协调效果。
- 方法要点：通过信息瓶颈理论和矢量量化，学习压缩和离散化通信消息，保留任务关键信息，并引入门控机制动态决定通信时机。
- 实验或效果：在协调任务中，性能提升181.8%，带宽使用减少41.4%，帕累托前沿分析显示优于现有方法。

## 摘要（原文）

> Multi-agent reinforcement learning systems deployed in real-world robotics applications face severe communication constraints that significantly impact coordination effectiveness. We present a framework that combines information bottleneck theory with vector quantization to enable selective, bandwidth-efficient communication in multi-agent environments. Our approach learns to compress and discretize communication messages while preserving task-critical information through principled information-theoretic optimization. We introduce a gated communication mechanism that dynamically determines when communication is necessary based on environmental context and agent states. Experimental evaluation on challenging coordination tasks demonstrates that our method achieves 181.8% performance improvement over no-communication baselines while reducing bandwidth usage by 41.4%. Comprehensive Pareto frontier analysis shows dominance across the entire success-bandwidth spectrum with area-under-curve of 0.198 vs 0.142 for next-best methods. Our approach significantly outperforms existing communication strategies and establishes a theoretically grounded framework for deploying multi-agent systems in bandwidth-constrained environments such as robotic swarms, autonomous vehicle fleets, and distributed sensor networks.

