---
layout: default
title: Adaptive Confidence Gating in Multi-Agent Collaboration for Efficient and Optimized Code Generation
---

# Adaptive Confidence Gating in Multi-Agent Collaboration for Efficient and Optimized Code Generation
**arXiv**：[2601.21469v1](https://arxiv.org/abs/2601.21469) · [PDF](https://arxiv.org/pdf/2601.21469.pdf)  
**作者**：Haoji Zhang, Yuzhe Li, Zhenqiang Liu, Chenyang Liu, Shenyang Zhang, Yi Zhou  

**一句话要点**：提出DebateCoder多智能体协作框架，以提升资源受限环境下小语言模型的代码生成推理能力。

**关键词**：代码生成, 多智能体协作, 小语言模型, 自适应置信门控, 推理优化

## 3 点简述
- 核心问题：小语言模型在复杂逻辑代码生成中面临推理瓶颈和失败循环。
- 方法要点：采用三智能体角色扮演协议，结合自适应置信门控和多轮审议模块。
- 实验或效果：在HumanEval上实现70.12% Pass@1，优于MapCoder并减少约35%API开销。

## 摘要（原文）

> While Large Language Models (LLMs) have catalyzed breakthroughs in automated code generation, Small Language Models (SLMs) often encounter reasoning bottlenecks and failure loops when addressing complex logical requirements. To overcome these challenges, we propose DebateCoder, a multi-agent collaborative framework designed to improve the reasoning ability of SLMs (e.g., Pangu-1B) in resource-constrained environments. DebateCoder uses a structured role-playing protocol with three agents: User Agent (A_UA), Technical Agent (A_TA), and Quality Assurance Agent (A_QA). It also includes an Adaptive Confidence Gating mechanism with a 95% threshold to balance accuracy and inference efficiency. In addition, we introduce a multi-turn deliberation module and a reviewer-guided analytical debugging loop for orthogonal pre-generation debate and post-generation refinement. Experiments on HumanEval and MBPP show that DebateCoder achieves 70.12% Pass@1 on HumanEval, outperforming MapCoder while reducing API overhead by about 35%. These results indicate that collaborative protocols can mitigate limitations of small-parameter models and provide a scalable, efficient approach to high-quality automated software engineering.

