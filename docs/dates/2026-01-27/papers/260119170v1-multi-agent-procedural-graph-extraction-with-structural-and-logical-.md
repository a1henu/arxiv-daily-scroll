---
layout: default
title: Multi-Agent Procedural Graph Extraction with Structural and Logical Refinement
---

# Multi-Agent Procedural Graph Extraction with Structural and Logical Refinement
**arXiv**：[2601.19170v1](https://arxiv.org/abs/2601.19170) · [PDF](https://arxiv.org/pdf/2601.19170.pdf)  
**作者**：Wangyang Ying, Yanchi Liu, Xujiang Zhao, Wei Cheng, Zhengzhang Chen, Wenchao Yu, Yanjie Fu, Haifeng Chen  

**一句话要点**：提出多智能体框架以从自然语言中提取结构有效且逻辑对齐的程序图

**关键词**：程序图提取, 多智能体框架, 结构反馈, 逻辑对齐, 自然语言处理, 工作流自动化

## 3 点简述
- 核心问题：从自然语言自动提取程序图需保证结构有效性和逻辑一致性，现有大语言模型常产生错误
- 方法要点：采用多轮推理框架，通过图构建、结构反馈和逻辑反馈三阶段迭代优化，无需监督或参数更新
- 实验或效果：在结构正确性和逻辑一致性上显著优于基线模型，实现可解释和可控的细化

## 摘要（原文）

> Automatically extracting workflows as procedural graphs from natural language is promising yet underexplored, demanding both structural validity and logical alignment. While recent large language models (LLMs) show potential for procedural graph extraction, they often produce ill-formed structures or misinterpret logical flows. We present \model{}, a multi-agent framework that formulates procedural graph extraction as a multi-round reasoning process with dedicated structural and logical refinement. The framework iterates through three stages: (1) a graph extraction phase with the graph builder agent, (2) a structural feedback phase in which a simulation agent diagnoses and explains structural defects, and (3) a logical feedback phase in which a semantic agent aligns semantics between flow logic and linguistic cues in the source text. Important feedback is prioritized and expressed in natural language, which is injected into subsequent prompts, enabling interpretable and controllable refinement. This modular design allows agents to target distinct error types without supervision or parameter updates. Experiments demonstrate that \model{} achieves substantial improvements in both structural correctness and logical consistency over strong baselines.

