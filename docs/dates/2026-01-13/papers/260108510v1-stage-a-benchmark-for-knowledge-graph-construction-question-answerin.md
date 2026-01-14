---
layout: default
title: STAGE: A Benchmark for Knowledge Graph Construction, Question Answering, and In-Script Role-Playing over Movie Screenplays
---

# STAGE: A Benchmark for Knowledge Graph Construction, Question Answering, and In-Script Role-Playing over Movie Screenplays
**arXiv**：[2601.08510v1](https://arxiv.org/abs/2601.08510) · [PDF](https://arxiv.org/pdf/2601.08510.pdf)  
**作者**：Qiuyu Tian, Yiding Li, Fengyi Chen, Zequn Liu, Youyong Kong, Fan Guo, Yuyao Li, Jinjing Shen, Zhijing Xie, Yiyun Luo, Xin Zhang  

**一句话要点**：提出STAGE基准，用于评估模型在电影剧本上的知识图谱构建、问答和角色扮演能力。

**关键词**：电影剧本理解, 知识图谱构建, 长文本问答, 角色扮演, 叙事评估

## 3 点简述
- 核心问题：现有基准缺乏对模型构建连贯故事世界并在多任务中一致使用的评估。
- 方法要点：定义四个任务，基于共享叙事世界表示，覆盖知识图谱构建、事件摘要、问答和角色扮演。
- 实验或效果：提供150部电影的清洗剧本、知识图谱和注释，支持模型能力的整体评估。

## 摘要（原文）

> Movie screenplays are rich long-form narratives that interleave complex character relationships, temporally ordered events, and dialogue-driven interactions. While prior benchmarks target individual subtasks such as question answering or dialogue generation, they rarely evaluate whether models can construct a coherent story world and use it consistently across multiple forms of reasoning and generation. We introduce STAGE (Screenplay Text, Agents, Graphs and Evaluation), a unified benchmark for narrative understanding over full-length movie screenplays. STAGE defines four tasks: knowledge graph construction, scene-level event summarization, long-context screenplay question answering, and in-script character role-playing, all grounded in a shared narrative world representation. The benchmark provides cleaned scripts, curated knowledge graphs, and event- and character-centric annotations for 150 films across English and Chinese, enabling holistic evaluation of models' abilities to build world representations, abstract and verify narrative events, reason over long narratives, and generate character-consistent responses.

