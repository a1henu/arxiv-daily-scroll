---
layout: default
title: See and Remember: A Multimodal Agent for Web Traversal
---

# See and Remember: A Multimodal Agent for Web Traversal
**arXiv**：[2603.02626v1](https://arxiv.org/abs/2603.02626) · [PDF](https://arxiv.org/pdf/2603.02626.pdf)  
**作者**：Xinjun Wang, Shengyao Wang, Aimin Zhou, Hao Hao  

**一句话要点**：提出V-GEMS多模态代理架构，通过视觉接地和显式记忆系统解决网页遍历中的空间迷失和循环导航问题。

**关键词**：多模态代理, 网页遍历, 视觉接地, 显式记忆系统, 自主导航, 基准评估

## 3 点简述
- 核心问题：基于LLM的代理在自主网页导航中常面临空间迷失和导航循环，难以处理复杂视觉环境和长期上下文。
- 方法要点：集成视觉接地以解析模糊交互元素，并引入带状态跟踪的显式记忆栈，构建结构化遍历路径图，支持有效回溯和避免循环失败。
- 实验或效果：在动态基准测试中，V-GEMS显著优于WebWalker基线，性能提升28.7%，代码已开源。

## 摘要（原文）

> Autonomous web navigation requires agents to perceive complex visual environments and maintain long-term context, yet current Large Language Model (LLM) based agents often struggle with spatial disorientation and navigation loops. In this paper, we propose generally applicable V-GEMS(Visual Grounding and Explicit Memory System), a robust multimodal agent architecture designed for precise and resilient web traversal. Our agent integrates visual grounding to resolve ambiguous interactive elements and introduces an explicit memory stack with state tracking. This dual mechanism allows the agent to maintain a structured map of its traversal path, enabling valid backtracking and preventing cyclical failures in deep navigation tasks. We also introduce an updatable dynamic benchmark to rigorously evaluate adaptability. Experiments show V-GEMS significantly dominates the WebWalker baseline, achieving a substantial 28.7% performance gain. Code is available at https://github.com/Vaultttttttttttt/V-GEMS.

