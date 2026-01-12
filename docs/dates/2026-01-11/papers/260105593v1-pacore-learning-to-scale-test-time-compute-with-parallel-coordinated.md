---
layout: default
title: PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning
---

# PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning
**arXiv**：[2601.05593v1](https://arxiv.org/abs/2601.05593) · [PDF](https://arxiv.org/pdf/2601.05593.pdf)  
**作者**：Jingcheng Hu, Yinmin Zhang, Shijie Shang, Xiaobo Yang, Yue Peng, Zhewei Huang, Hebin Zhou, Xin Wu, Jie Cheng, Fanqi Wan, Xiangwen Kong, Chengyuan Yao, Kaiwen Yan, Ailin Huang, Hongyu Zhou, Qi Han, Zheng Ge, Daxin Jiang, Xiangyu Zhang, Heung-Yeung Shum  

**一句话要点**：提出PaCoRe框架以解决语言模型测试时计算无法超越序列推理的限制

**关键词**：并行推理, 测试时计算扩展, 消息传递架构, 强化学习训练, 数学推理, 开源框架

## 3 点简述
- 核心问题：当前语言模型在固定上下文窗口下，测试时计算难以超越序列推理，限制了性能提升。
- 方法要点：通过消息传递架构协调多轮并行探索，每轮并行推理轨迹压缩为消息并合成，以指导下一轮并生成最终答案。
- 实验或效果：在数学等领域表现优异，8B模型在HMMT 2025上达到94.5%，超越GPT-5，有效测试时计算扩展至约两百万令牌。

## 摘要（原文）

> We introduce Parallel Coordinated Reasoning (PaCoRe), a training-and-inference framework designed to overcome a central limitation of contemporary language models: their inability to scale test-time compute (TTC) far beyond sequential reasoning under a fixed context window. PaCoRe departs from the traditional sequential paradigm by driving TTC through massive parallel exploration coordinated via a message-passing architecture in multiple rounds. Each round launches many parallel reasoning trajectories, compacts their findings into context-bounded messages, and synthesizes these messages to guide the next round and ultimately produce the final answer. Trained end-to-end with large-scale, outcome-based reinforcement learning, the model masters the synthesis abilities required by PaCoRe and scales to multi-million-token effective TTC without exceeding context limits. The approach yields strong improvements across diverse domains, and notably pushes reasoning beyond frontier systems in mathematics: an 8B model reaches 94.5% on HMMT 2025, surpassing GPT-5's 93.2% by scaling effective TTC to roughly two million tokens. We open-source model checkpoints, training data, and the full inference pipeline to accelerate follow-up work.

