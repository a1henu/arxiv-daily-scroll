---
layout: default
title: NeoAMT: Neologism-Aware Agentic Machine Translation with Reinforcement Learning
---

# NeoAMT: Neologism-Aware Agentic Machine Translation with Reinforcement Learning
**arXiv**：[2601.03790v1](https://arxiv.org/abs/2601.03790) · [PDF](https://arxiv.org/pdf/2601.03790.pdf)  
**作者**：Zhongtao Miao, Kaiyan Zhao, Masaaki Nagata, Yoshimasa Tsuruoka  

**一句话要点**：提出NeoAMT框架，利用强化学习解决新词感知机器翻译问题

**关键词**：新词感知机器翻译, 强化学习, Wiktionary搜索工具, 多语言数据集, 翻译代理

## 3 点简述
- 核心问题：新词感知机器翻译领域研究不足，需处理源句中的新词翻译
- 方法要点：基于Wiktionary构建搜索工具和数据集，采用强化学习训练翻译代理
- 实验或效果：创建多语言数据集，提出自适应奖励设计，提升翻译质量

## 摘要（原文）

> Neologism-aware machine translation aims to translate source sentences containing neologisms into target languages. This field remains underexplored compared with general machine translation (MT). In this paper, we propose an agentic framework, NeoAMT, for neologism-aware machine translation using a Wiktionary search tool. Specifically, we first create a new dataset for neologism-aware machine translation and develop a search tool based on Wiktionary. The new dataset covers 16 languages and 75 translation directions and is derived from approximately 10 million records of an English Wiktionary dump. The retrieval corpus of the search tool is also constructed from around 3 million cleaned records of the Wiktionary dump. We then use it for training the translation agent with reinforcement learning (RL) and evaluating the accuracy of neologism-aware machine translation. Based on this, we also propose an RL training framework that contains a novel reward design and an adaptive rollout generation approach by leveraging "translation difficulty" to further improve the translation quality of translation agents using our search tool.

