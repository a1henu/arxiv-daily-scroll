---
layout: default
title: MuseCPBench: an Empirical Study of Music Editing Methods through Music Context Preservation
---

# MuseCPBench: an Empirical Study of Music Editing Methods through Music Context Preservation
**arXiv**：[2512.14629v1](https://arxiv.org/abs/2512.14629) · [PDF](https://arxiv.org/pdf/2512.14629.pdf)  
**作者**：Yash Vishe, Eric Xue, Xunyi Jiang, Zachary Novack, Junda Wu, Julian McAuley, Xin Xu  

**一句话要点**：提出MuseCPBench基准以解决音乐编辑中上下文保存评估不一致的问题

**关键词**：音乐编辑, 上下文保存评估, 基准测试, 音乐生成模型, 多方法比较

## 3 点简述
- 核心问题：现有音乐编辑方法缺乏统一评估音乐上下文保存能力，导致比较不可靠
- 方法要点：引入首个MCP评估基准，覆盖四类音乐方面，支持五种基线方法比较
- 实验或效果：通过系统分析揭示当前方法在音乐上下文保存上的差距，提供实用指导

## 摘要（原文）

> Music editing plays a vital role in modern music production, with applications in film, broadcasting, and game development. Recent advances in music generation models have enabled diverse editing tasks such as timbre transfer, instrument substitution, and genre transformation. However, many existing works overlook the evaluation of their ability to preserve musical facets that should remain unchanged during editing a property we define as Music Context Preservation (MCP). While some studies do consider MCP, they adopt inconsistent evaluation protocols and metrics, leading to unreliable and unfair comparisons. To address this gap, we introduce the first MCP evaluation benchmark, MuseCPBench, which covers four categories of musical facets and enables comprehensive comparisons across five representative music editing baselines. Through systematic analysis along musical facets, methods, and models, we identify consistent preservation gaps in current music editing methods and provide insightful explanations. We hope our findings offer practical guidance for developing more effective and reliable music editing strategies with strong MCP capability

