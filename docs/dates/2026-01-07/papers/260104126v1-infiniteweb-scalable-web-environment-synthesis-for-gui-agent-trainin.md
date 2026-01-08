---
layout: default
title: InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training
---

# InfiniteWeb: Scalable Web Environment Synthesis for GUI Agent Training
**arXiv**：[2601.04126v1](https://arxiv.org/abs/2601.04126) · [PDF](https://arxiv.org/pdf/2601.04126.pdf)  
**作者**：Ziyun Zhang, Zezhou Wang, Xiaoyi Zhang, Zongyu Guo, Jiahao Li, Bin Li, Yan Lu  

**一句话要点**：提出InfiniteWeb系统以解决GUI代理训练中网络环境稀缺问题

**关键词**：GUI代理训练, 网络环境合成, 自动网站生成, 强化学习奖励, 可扩展系统

## 3 点简述
- 核心问题：GUI代理训练因缺乏真实、功能性的网络环境而受限
- 方法要点：通过统一规范、任务驱动的测试开发及多样化设计，自动生成大规模网络环境
- 实验或效果：在网站构建上超越商业编码代理，提升代理在基准测试中的性能

## 摘要（原文）

> GUI agents that interact with graphical interfaces on behalf of users represent a promising direction for practical AI assistants. However, training such agents is hindered by the scarcity of suitable environments. We present InfiniteWeb, a system that automatically generates functional web environments at scale for GUI agent training. While LLMs perform well on generating a single webpage, building a realistic and functional website with many interconnected pages faces challenges. We address these challenges through unified specification, task-centric test-driven development, and a combination of website seed with reference design image to ensure diversity. Our system also generates verifiable task evaluators enabling dense reward signals for reinforcement learning. Experiments show that InfiniteWeb surpasses commercial coding agents at realistic website construction, and GUI agents trained on our generated environments achieve significant performance improvements on OSWorld and Online-Mind2Web, demonstrating the effectiveness of proposed system.

