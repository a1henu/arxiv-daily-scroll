---
layout: default
title: Beyond Fast and Slow: Cognitive-Inspired Elastic Reasoning for Large Language Models
---

# Beyond Fast and Slow: Cognitive-Inspired Elastic Reasoning for Large Language Models
**arXiv**：[2512.15089v1](https://arxiv.org/abs/2512.15089) · [PDF](https://arxiv.org/pdf/2512.15089.pdf)  
**作者**：Jinwu Hu, Dongjin Yang, Langyu Bian, Zhiquan Wen, Yufeng Wang, Yaofo Chen, Bin Xiao, Yuanqing Li, Mingkui Tan  

**一句话要点**：提出认知启发弹性推理框架以动态平衡大语言模型推理效率与准确性

**关键词**：大语言模型推理, 弹性推理策略, 强化学习代理, 认知工具辅助, 查询难度评估

## 3 点简述
- 现有大语言模型推理策略依赖快慢模式，难以平衡不同难度查询的效率与准确性
- CogER框架基于人类分层推理，通过强化学习训练代理动态选择策略，并引入认知工具辅助推理
- 实验显示CogER在领域内外任务上优于现有方法，准确率相对提升至少8%

## 摘要（原文）

> Large language models (LLMs) have demonstrated impressive performance across various language tasks. However, existing LLM reasoning strategies mainly rely on the LLM itself with fast or slow mode (like o1 thinking) and thus struggle to balance reasoning efficiency and accuracy across queries of varying difficulties. In this paper, we propose Cognitive-Inspired Elastic Reasoning (CogER), a framework inspired by human hierarchical reasoning that dynamically selects the most suitable reasoning strategy for each query. Specifically, CogER first assesses the complexity of incoming queries and assigns them to one of several predefined levels, each corresponding to a tailored processing strategy, thereby addressing the challenge of unobservable query difficulty. To achieve automatic strategy selection, we model the process as a Markov Decision Process and train a CogER-Agent using reinforcement learning. The agent is guided by a reward function that balances solution quality and computational cost, ensuring resource-efficient reasoning. Moreover, for queries requiring external tools, we introduce Cognitive Tool-Assisted Reasoning, which enables the LLM to autonomously invoke external tools within its chain-of-thought. Extensive experiments demonstrate that CogER outperforms state-of-the-art Test-Time scaling methods, achieving at least a 13% relative improvement in average exact match on In-Domain tasks and an 8% relative gain on Out-of-Domain tasks.

