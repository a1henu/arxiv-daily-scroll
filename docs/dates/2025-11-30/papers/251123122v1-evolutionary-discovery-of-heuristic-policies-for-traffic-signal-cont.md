---
layout: default
title: Evolutionary Discovery of Heuristic Policies for Traffic Signal Control
---

# Evolutionary Discovery of Heuristic Policies for Traffic Signal Control
**arXiv**：[2511.23122v1](https://arxiv.org/abs/2511.23122) · [PDF](https://arxiv.org/pdf/2511.23122.pdf)  
**作者**：Ruibing Wang, Shuhan Guo, Zeen Li, Zhen Wang, Quanming Yao  

**一句话要点**：提出Temporal Policy Evolution for Traffic，利用LLM演化引擎生成交通信号控制的专用启发式策略。

**关键词**：交通信号控制, 启发式策略, 大语言模型演化, 结构化状态抽象, 信用分配反馈, 无训练优化

## 3 点简述
- 核心问题：交通信号控制中，传统启发式方法效率高但简化过度，DRL性能好但泛化差且策略不透明，在线LLM推理通用但延迟高且缺乏环境优化。
- 方法要点：引入结构化状态抽象将高维交通数据转换为时序逻辑事实，以及信用分配反馈追踪微观决策错误以进行针对性批评，完全在提示层面操作无需训练。
- 实验或效果：生成轻量级、鲁棒的策略，针对特定交通环境优化，性能优于启发式方法和在线LLM执行者。

## 摘要（原文）

> Traffic Signal Control (TSC) involves a challenging trade-off: classic heuristics are efficient but oversimplified, while Deep Reinforcement Learning (DRL) achieves high performance yet suffers from poor generalization and opaque policies. Online Large Language Models (LLMs) provide general reasoning but incur high latency and lack environment-specific optimization. To address these issues, we propose Temporal Policy Evolution for Traffic (\textbf{\method{}}), which uses LLMs as an evolution engine to derive specialized heuristic policies. The framework introduces two key modules: (1) Structured State Abstraction (SSA), converting high-dimensional traffic data into temporal-logical facts for reasoning; and (2) Credit Assignment Feedback (CAF), tracing flawed micro-decisions to poor macro-outcomes for targeted critique. Operating entirely at the prompt level without training, \method{} yields lightweight, robust policies optimized for specific traffic environments, outperforming both heuristics and online LLM actors.

