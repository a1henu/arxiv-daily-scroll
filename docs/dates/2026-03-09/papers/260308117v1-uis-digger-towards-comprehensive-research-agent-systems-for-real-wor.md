---
layout: default
title: UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking
---

# UIS-Digger: Towards Comprehensive Research Agent Systems for Real-world Unindexed Information Seeking
**arXiv**：[2603.08117v1](https://arxiv.org/abs/2603.08117) · [PDF](https://arxiv.org/pdf/2603.08117.pdf)  
**作者**：Chang Liu, Chuqiao Kuang, Tianyi Zhuang, Yuxin Cheng, Huichi Zhou, Xiaoguang Li, Lifeng Shang  

**一句话要点**：提出UIS-Digger多智能体框架以解决未索引信息检索问题

**关键词**：未索引信息检索, 多智能体框架, 双模式浏览, 基准评估, 训练优化, 信息检索系统

## 3 点简述
- 核心问题：现有信息检索智能体依赖搜索引擎索引，忽略未索引信息如动态网页和嵌入文件。
- 方法要点：引入双模式浏览，同时支持网页搜索和文件解析，采用SFT和RFT训练优化约30B参数骨干LLM。
- 实验或效果：在UIS-QA基准上达到27.27%准确率，优于集成O3和GPT-4.1的系统，揭示未索引源交互的重要性。

## 摘要（原文）

> Recent advancements in LLM-based information-seeking agents have achieved record-breaking performance on established benchmarks. However, these agents remain heavily reliant on search-engine-indexed knowledge, leaving a critical blind spot: Unindexed Information Seeking (UIS). This paper identifies and explores the UIS problem, where vital information is not captured by search engine crawlers, such as overlooked content, dynamic webpages, and embedded files. Despite its significance, UIS remains an underexplored challenge. To address this gap, we introduce UIS-QA, the first dedicated UIS benchmark, comprising 110 expert-annotated QA pairs. Notably, even state-of-the-art agents experience a drastic performance drop on UIS-QA (e.g., from 70.90 on GAIA and 46.70 on BrowseComp-zh to 24.55 on UIS-QA), underscoring the severity of the problem. To mitigate this, we propose UIS-Digger, a novel multi-agent framework that incorporates dual-mode browsing and enables simultaneous webpage searching and file parsing. With a relatively small $\sim$30B-parameter backbone LLM optimized using SFT and RFT training strategies, UIS-Digger sets a strong baseline at 27.27\%, outperforming systems integrating sophisticated LLMs such as O3 and GPT-4.1. This demonstrates the importance of proactive interaction with unindexed sources for effective and comprehensive information-seeking. Our work not only uncovers a fundamental limitation in current agent evaluation paradigms but also provides the first toolkit for advancing UIS research, defining a new and promising direction for robust information-seeking systems.

