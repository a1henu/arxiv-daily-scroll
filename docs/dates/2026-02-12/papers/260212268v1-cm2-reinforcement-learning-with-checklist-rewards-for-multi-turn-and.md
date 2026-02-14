---
layout: default
title: CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use
---

# CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use
**arXiv**：[2602.12268v1](https://arxiv.org/abs/2602.12268) · [PDF](https://arxiv.org/pdf/2602.12268.pdf)  
**作者**：Zhen Zhang, Kaiqiang Song, Xun Wang, Yebowen Hu, Weixiang Yan, Chenyang Zhao, Henry Peng Zou, Haoyun Deng, Sathish Reddy Indurthi, Shujian Liu, Simin Ma, Xiaoyang Wang, Xin Eric Wang, Song Wang  

**一句话要点**：提出CM2框架，通过清单奖励优化多轮多步工具使用代理，无需可验证奖励。

**关键词**：强化学习, 工具使用代理, 清单奖励, 多轮交互, LLM模拟环境

## 3 点简述
- 核心问题：多轮多步工具使用代理的强化学习缺乏可验证奖励，且环境构建成本高。
- 方法要点：使用清单奖励分解行为为细粒度标准，在LLM模拟环境中训练，平衡稳定性和信息量。
- 实验或效果：在多个基准上优于监督微调，匹配或超越开源基线，提供可扩展优化方案。

## 摘要（原文）

> AI agents are increasingly used to solve real-world tasks by reasoning over multi-turn user interactions and invoking external tools. However, applying reinforcement learning to such settings remains difficult: realistic objectives often lack verifiable rewards and instead emphasize open-ended behaviors; moreover, RL for multi-turn, multi-step agentic tool use is still underexplored; and building and maintaining executable tool environments is costly, limiting scale and coverage. We propose CM2, an RL framework that replaces verifiable outcome rewards with checklist rewards. CM2 decomposes each turn's intended behavior into fine-grained binary criteria with explicit evidence grounding and structured metadata, turning open-ended judging into more stable classification-style decisions. To balance stability and informativeness, our method adopts a strategy of sparse reward assignment but dense evaluation criteria. Training is performed in a scalable LLM-simulated tool environment, avoiding heavy engineering for large tool sets. Experiments show that CM2 consistently improves over supervised fine-tuning. Starting from an 8B Base model and training on an 8k-example RL dataset, CM2 improves over the SFT counterpart by 8 points on tau^-Bench, by 10 points on BFCL-V4, and by 12 points on ToolSandbox. The results match or even outperform similarly sized open-source baselines, including the judging model. CM2 thus provides a scalable recipe for optimizing multi-turn, multi-step tool-using agents without relying on verifiable rewards. Code provided by the open-source community: https://github.com/namezhenzhang/CM2-RLCR-Tool-Agent.

