---
layout: default
title: ParamExplorer: A framework for exploring parameters in generative art
---

# ParamExplorer: A framework for exploring parameters in generative art
**arXiv**：[2512.16529v1](https://arxiv.org/abs/2512.16529) · [PDF](https://arxiv.org/pdf/2512.16529.pdf)  
**作者**：Julien Gachadoat, Guillaume Lagarde  

**一句话要点**：提出ParamExplorer框架以解决生成艺术中参数空间探索的难题

**关键词**：生成艺术, 参数空间探索, 交互式框架, 强化学习, p5.js集成

## 3 点简述
- 生成艺术系统常涉及高维复杂参数空间，美学输出仅占小区域，导致探索困难
- ParamExplorer为交互式模块化框架，受强化学习启发，支持人机协作或自动反馈引导探索
- 框架集成p5.js，实现并评估多种探索策略（称为代理）

## 摘要（原文）

> Generative art systems often involve high-dimensional and complex parameter spaces in which aesthetically compelling outputs occupy only small, fragmented regions. Because of this combinatorial explosion, artists typically rely on extensive manual trial-and-error, leaving many potentially interesting configurations undiscovered. In this work we make two contributions. First, we introduce ParamExplorer, an interactive and modular framework inspired by reinforcement learning that helps the exploration of parameter spaces in generative art algorithms, guided by human-in-the-loop or even automated feedback. The framework also integrates seamlessly with existing p5.js projects. Second, within this framework we implement and evaluate several exploration strategies, referred to as agents.

