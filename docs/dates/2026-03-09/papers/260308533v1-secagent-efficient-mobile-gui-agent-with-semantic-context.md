---
layout: default
title: SecAgent: Efficient Mobile GUI Agent with Semantic Context
---

# SecAgent: Efficient Mobile GUI Agent with Semantic Context
**arXiv**：[2603.08533v1](https://arxiv.org/abs/2603.08533) · [PDF](https://arxiv.org/pdf/2603.08533.pdf)  
**作者**：Yiping Xie, Song Chen, Jingxuan Xing, Wei Jiang, Zekun Zhu, Yingyao Wang, Pi Bu, Jun Song, Yuning Jiang, Bo Zheng  

**一句话要点**：提出SecAgent，一种高效的移动GUI代理，通过语义上下文机制解决多语言数据集稀缺和历史表示低效问题。

**关键词**：移动GUI代理, 多语言数据集, 语义上下文, 强化微调, 导航基准

## 3 点简述
- 核心问题：现有移动GUI代理面临高质量多语言数据集稀缺和历史表示方法低效的挑战。
- 方法要点：构建中文移动GUI数据集，并设计语义上下文机制，将历史信息蒸馏为自然语言摘要以降低计算成本。
- 实验或效果：SecAgent在3B规模上超越类似基线，性能媲美7B-8B模型，并在导航基准测试中表现优异。

## 摘要（原文）

> Mobile Graphical User Interface (GUI) agents powered by multimodal large language models have demonstrated promising capabilities in automating complex smartphone tasks. However, existing approaches face two critical limitations: the scarcity of high-quality multilingual datasets, particularly for non-English ecosystems, and inefficient history representation methods. To address these challenges, we present SecAgent, an efficient mobile GUI agent at 3B scale. We first construct a human-verified Chinese mobile GUI dataset with 18k grounding samples and 121k navigation steps across 44 applications, along with a Chinese navigation benchmark featuring multi-choice action annotations. Building upon this dataset, we propose a semantic context mechanism that distills history screenshots and actions into concise, natural language summaries, significantly reducing computational costs while preserving task-relevant information. Through supervised and reinforcement fine-tuning, SecAgent outperforms similar-scale baselines and achieves performance comparable to 7B-8B models on our and public navigation benchmarks. We will open-source the training dataset, benchmark, model, and code to advance research in multilingual mobile GUI automation.

