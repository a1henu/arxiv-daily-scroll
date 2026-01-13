---
layout: default
title: ShowUI-Aloha: Human-Taught GUI Agent
---

# ShowUI-Aloha: Human-Taught GUI Agent
**arXiv**：[2601.07181v1](https://arxiv.org/abs/2601.07181) · [PDF](https://arxiv.org/pdf/2601.07181.pdf)  
**作者**：Yichun Zhang, Xiangwu Guo, Yauhong Goh, Jessica Hu, Zhiheng Chen, Xin Wang, Difei Gao, Mike Zheng Shou  

**一句话要点**：提出ShowUI-Aloha管道，将非结构化人类屏幕录像转化为结构化任务，以解决GUI自动化中高质量训练数据缺乏的问题。

**关键词**：GUI自动化, 人类演示学习, 屏幕录像解析, 自然语言生成, 任务规划, 实时执行

## 3 点简述
- 核心问题：GUI自动化因缺乏可扩展的高质量训练数据而面临挑战，人类演示录像长且无标注。
- 方法要点：通过记录器、学习者、规划器和执行器四组件，解析录像为自然语言描述和可执行动作。
- 实验或效果：展示从观察人类学习构建通用GUI代理的可行路径，提供实时反馈和安全检查。

## 摘要（原文）

> Graphical User Interfaces (GUIs) are central to human-computer interaction, yet automating complex GUI tasks remains a major challenge for autonomous agents, largely due to a lack of scalable, high-quality training data. While recordings of human demonstrations offer a rich data source, they are typically long, unstructured, and lack annotations, making them difficult for agents to learn from.To address this, we introduce ShowUI-Aloha, a comprehensive pipeline that transforms unstructured, in-the-wild human screen recordings from desktop environments into structured, actionable tasks. Our framework includes four key components: A recorder that captures screen video along with precise user interactions like mouse clicks, keystrokes, and scrolls. A learner that semantically interprets these raw interactions and the surrounding visual context, translating them into descriptive natural language captions. A planner that reads the parsed demonstrations, maintains task states, and dynamically formulates the next high-level action plan based on contextual reasoning. An executor that faithfully carries out these action plans at the OS level, performing precise clicks, drags, text inputs, and window operations with safety checks and real-time feedback. Together, these components provide a scalable solution for collecting and parsing real-world human data, demonstrating a viable path toward building general-purpose GUI agents that can learn effectively from simply observing humans.

