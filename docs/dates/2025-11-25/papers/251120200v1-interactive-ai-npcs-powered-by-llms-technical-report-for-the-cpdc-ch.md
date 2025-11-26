---
layout: default
title: Interactive AI NPCs Powered by LLMs: Technical Report for the CPDC Challenge 2025
---

# Interactive AI NPCs Powered by LLMs: Technical Report for the CPDC Challenge 2025
**arXiv**：[2511.20200v1](https://arxiv.org/abs/2511.20200) · [PDF](https://arxiv.org/pdf/2511.20200.pdf)  
**作者**：Yitian Huang, Yuxuan Lei, Jianxun Lian, Hao Liao  

**一句话要点**：提出统一框架优化LLM驱动的AI NPC，提升对话稳定性和任务性能

**关键词**：上下文工程, 强化学习, 角色扮演对话, 工具调用优化, 输入压缩

## 3 点简述
- 核心问题：解决常识角色对话中工具调用不稳定和角色扮演指导不足的问题
- 方法要点：采用上下文工程和GRPO强化学习，优化输入压缩和奖励信号训练
- 实验或效果：在CPDC 2025挑战中多项任务排名前列，验证方法有效性

## 摘要（原文）

> This report presents the solution and results of our team MSRA\_SC in the Commonsense Persona-Grounded Dialogue Challenge (CPDC 2025). We propose a simple yet effective framework that unifies improvements across both GPU Track and API Track. Our method centers on two key components. First, Context Engineering applies dynamic tool pruning and persona clipping for input compression, combined with post-processing techniques such as parameter normalization and function merging. Together with manually refined prompts, this design improves tool call stability, execution reliability, and role-playing guidance. Second, in the GPU Track, we further adopt GRPO training, replacing supervised fine-tuning with reinforcement learning directly optimized by reward signals. This mitigates small-sample overfitting and significantly enhances task-oriented dialogue performance. In the final evaluation, our team ranks 1st in Task 2 API, 2nd in Task 1 API, and 3rd in both Task 3 API and GPU track, demonstrating the effectiveness of our approach. Our code is publicly available at https://gitlab.aicrowd.com/nikoo_yu/cpdc-2025-winning-solution

