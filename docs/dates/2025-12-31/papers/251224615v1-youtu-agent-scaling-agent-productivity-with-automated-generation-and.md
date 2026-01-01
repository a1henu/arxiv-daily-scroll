---
layout: default
title: Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization
---

# Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization
**arXiv**：[2512.24615v1](https://arxiv.org/abs/2512.24615) · [PDF](https://arxiv.org/pdf/2512.24615.pdf)  
**作者**：Yuchen Shi, Yuzheng Cai, Siqi Cai, Zihan Xu, Lichao Chen, Yulei Qin, Zhijian Zhou, Xiang Fei, Chaofan Qiu, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Guocan Cai, Yong Mao, Yunsheng Wu, Ke Li, Xing Sun  

**一句话要点**：提出Youtu-Agent框架以自动化生成和优化LLM代理，解决高配置成本和静态能力问题。

**关键词**：LLM代理框架, 自动化生成, 混合策略优化, 强化学习, 上下文优化, 模块化设计

## 3 点简述
- 核心问题：现有LLM代理框架配置成本高且能力静态，难以适应动态环境。
- 方法要点：采用模块化设计，支持工作流和元代理两种生成模式，结合上下文优化和强化学习进行混合策略优化。
- 实验或效果：在WebWalkerQA和GAIA基准上达到SOTA，自动化生成工具合成成功率超81%，实践模块提升AIME性能，强化学习加速40%并增强能力。

## 摘要（原文）

> Existing Large Language Model (LLM) agent frameworks face two significant challenges: high configuration costs and static capabilities. Building a high-quality agent often requires extensive manual effort in tool integration and prompt engineering, while deployed agents struggle to adapt to dynamic environments without expensive fine-tuning. To address these issues, we propose \textbf{Youtu-Agent}, a modular framework designed for the automated generation and continuous evolution of LLM agents. Youtu-Agent features a structured configuration system that decouples execution environments, toolkits, and context management, enabling flexible reuse and automated synthesis. We introduce two generation paradigms: a \textbf{Workflow} mode for standard tasks and a \textbf{Meta-Agent} mode for complex, non-standard requirements, capable of automatically generating tool code, prompts, and configurations. Furthermore, Youtu-Agent establishes a hybrid policy optimization system: (1) an \textbf{Agent Practice} module that enables agents to accumulate experience and improve performance through in-context optimization without parameter updates; and (2) an \textbf{Agent RL} module that integrates with distributed training frameworks to enable scalable and stable reinforcement learning of any Youtu-Agents in an end-to-end, large-scale manner. Experiments demonstrate that Youtu-Agent achieves state-of-the-art performance on WebWalkerQA (71.47\%) and GAIA (72.8\%) using open-weight models. Our automated generation pipeline achieves over 81\% tool synthesis success rate, while the Practice module improves performance on AIME 2024/2025 by +2.7\% and +5.4\% respectively. Moreover, our Agent RL training achieves 40\% speedup with steady performance improvement on 7B LLMs, enhancing coding/reasoning and searching capabilities respectively up to 35\% and 21\% on Maths and general/multi-hop QA benchmarks.

