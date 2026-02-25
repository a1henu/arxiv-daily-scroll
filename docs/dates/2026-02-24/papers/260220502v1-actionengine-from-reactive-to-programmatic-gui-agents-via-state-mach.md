---
layout: default
title: ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory
---

# ActionEngine: From Reactive to Programmatic GUI Agents via State Machine Memory
**arXiv**：[2602.20502v1](https://arxiv.org/abs/2602.20502) · [PDF](https://arxiv.org/pdf/2602.20502.pdf)  
**作者**：Hongbin Zhong, Fazle Faisal, Luis França, Tanakorn Leesatapornwongsa, Adriana Szekeres, Kexin Rong, Suman Nath  

**一句话要点**：提出ActionEngine框架，通过状态机内存实现从反应式到程序化GUI代理的转变。

**关键词**：GUI代理, 状态机内存, 程序化规划, 视觉重定位, 离线探索, 在线执行

## 3 点简述
- 现有GUI代理依赖逐步视觉语言模型调用，导致高成本、高延迟和低准确性。
- 采用双代理架构：爬虫代理构建可更新状态机内存，执行代理合成完整Python程序执行任务。
- 在Reddit任务上实现95%成功率，平均单次LLM调用，成本降低11.8倍，延迟减半。

## 摘要（原文）

> Existing Graphical User Interface (GUI) agents operate through step-by-step calls to vision language models--taking a screenshot, reasoning about the next action, executing it, then repeating on the new page--resulting in high costs and latency that scale with the number of reasoning steps, and limited accuracy due to no persistent memory of previously visited pages.
>   We propose ActionEngine, a training-free framework that transitions from reactive execution to programmatic planning through a novel two-agent architecture: a Crawling Agent that constructs an updatable state-machine memory of the GUIs through offline exploration, and an Execution Agent that leverages this memory to synthesize complete, executable Python programs for online task execution.
>   To ensure robustness against evolving interfaces, execution failures trigger a vision-based re-grounding fallback that repairs the failed action and updates the memory.
>   This design drastically improves both efficiency and accuracy: on Reddit tasks from the WebArena benchmark, our agent achieves 95% task success with on average a single LLM call, compared to 66% for the strongest vision-only baseline, while reducing cost by 11.8x and end-to-end latency by 2x.
>   Together, these components yield scalable and reliable GUI interaction by combining global programmatic planning, crawler-validated action templates, and node-level execution with localized validation and repair.

