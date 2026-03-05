---
layout: default
title: LabelBuddy: An Open Source Music and Audio Language Annotation Tagging Tool Using AI Assistance
---

# LabelBuddy: An Open Source Music and Audio Language Annotation Tagging Tool Using AI Assistance
**arXiv**：[2603.04293v1](https://arxiv.org/abs/2603.04293) · [PDF](https://arxiv.org/pdf/2603.04293.pdf)  
**作者**：Ioannis Prokopiou, Ioannis Sina, Agisilaos Kounelis, Pantelis Vikatos, Themos Stafylakis  

**一句话要点**：提出开源协作式音频标注工具LabelBuddy，以解决音乐信息检索中主观标注与AI辅助的瓶颈问题。

**关键词**：音频标注工具, 音乐信息检索, AI辅助标注, 容器化后端, 开源协作

## 3 点简述
- 核心问题：开源工具缺乏捕捉音频主观细微差异的能力，阻碍了音乐信息检索中人类意图与机器理解的融合。
- 方法要点：通过容器化后端解耦界面与推理，支持用户插入自定义模型进行AI辅助预标注，实现多用户共识和模型隔离。
- 实验或效果：未知具体实验数据，但提供了系统架构描述和代码开源，旨在促进代理和大型音频语言模型的扩展。

## 摘要（原文）

> The advancement of Machine learning (ML), Large Audio Language Models (LALMs), and autonomous AI agents in Music Information Retrieval (MIR) necessitates a shift from static tagging to rich, human-aligned representation learning. However, the scarcity of open-source infrastructure capable of capturing the subjective nuances of audio annotation remains a critical bottleneck. This paper introduces \textbf{LabelBuddy}, an open-source collaborative auto-tagging audio annotation tool designed to bridge the gap between human intent and machine understanding. Unlike static tools, it decouples the interface from inference via containerized backends, allowing users to plug in custom models for AI-assisted pre-annotation. We describe the system architecture, which supports multi-user consensus, containerized model isolation, and a roadmap for extending agents and LALMs. Code available at https://github.com/GiannisProkopiou/gsoc2022-Label-buddy.

