---
layout: default
title: ComplLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making
---

# ComplLLM: Fine-tuning LLMs to Discover Complementary Signals for Decision-making
**arXiv**：[2602.19458v1](https://arxiv.org/abs/2602.19458) · [PDF](https://arxiv.org/pdf/2602.19458.pdf)  
**作者**：Ziyang Guo, Yifan Wu, Jason Hartline, Kenneth Holstein, Jessica Hullman  

**一句话要点**：提出ComplLLM框架，通过决策理论微调LLM以发现互补信号，支持多智能体决策流程。

**关键词**：多智能体决策, 互补信号发现, LLM微调, 决策理论, 可解释AI

## 3 点简述
- 核心问题：多智能体决策中互补性不足，影响最终决策质量。
- 方法要点：基于决策理论，以互补信息为奖励微调LLM，生成补充现有决策的信号。
- 实验或效果：在合成和真实任务中验证，能恢复已知互补信息并提供可解释信号。

## 摘要（原文）

> Multi-agent decision pipelines can outperform single agent workflows when complementarity holds, i.e., different agents bring unique information to the table to inform a final decision. We propose ComplLLM, a post-training framework based on decision theory that fine-tunes a decision-assistant LLM using complementary information as reward to output signals that complement existing agent decisions. We validate ComplLLM on synthetic and real-world tasks involving domain experts, demonstrating how the approach recovers known complementary information and produces plausible explanations of complementary signals to support downstream decision-makers.

