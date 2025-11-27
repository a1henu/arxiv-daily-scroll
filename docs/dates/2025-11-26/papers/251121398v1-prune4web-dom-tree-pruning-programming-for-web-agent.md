---
layout: default
title: Prune4Web: DOM Tree Pruning Programming for Web Agent
---

# Prune4Web: DOM Tree Pruning Programming for Web Agent
**arXiv**：[2511.21398v1](https://arxiv.org/abs/2511.21398) · [PDF](https://arxiv.org/pdf/2511.21398.pdf)  
**作者**：Jiayuan Zhang, Kaiquan Chen, Zhihao Lu, Enshen Zhou, Qian Yu, Jing Zhang  

**一句话要点**：提出Prune4Web以解决网页自动化中DOM树过大导致的效率与精度问题

**关键词**：网页自动化, DOM树剪枝, 程序化过滤, 大语言模型, 动作定位, 数据标注

## 3 点简述
- 核心问题：网页DOM结构庞大（1万至10万令牌），现有方法易丢失关键信息或效率低下。
- 方法要点：LLM生成Python脚本动态过滤DOM元素，实现程序化剪枝，减少候选元素25-50倍。
- 实验效果：在低层定位任务中，准确率从46.8%提升至88.28%，达到先进性能。

## 摘要（原文）

> Web automation employs intelligent agents to execute high-level tasks by mimicking human interactions with web interfaces. Despite the capabilities of recent Large Language Model (LLM)-based web agents, navigating complex, real-world webpages efficiently remains a significant hurdle due to the prohibitively large size of Document Object Model (DOM) structures, often ranging from 10,000 to 100,000 tokens. Existing strategies typically rely on crude DOM truncation -- risking the loss of critical information -- or employ inefficient heuristics and separate ranking models, failing to achieve an optimal balance between precision and scalability. To address these challenges, we introduce Prune4Web, a novel paradigm that shifts DOM processing from resource-intensive LLM reading to efficient programmatic pruning. Central to our approach is DOM Tree Pruning Programming, where an LLM generates executable Python scoring scripts to dynamically filter DOM elements based on semantic cues from decomposed sub-tasks. This mechanism eliminates the need for LLMs to ingest raw, massive DOMs, instead delegating traversal and scoring to lightweight, interpretable programs. This methodology achieves a 25x to 50x reduction in candidate elements for grounding, thereby facilitating precise action localization while mitigating attention dilution. Furthermore, we propose a specialized data annotation pipeline and a two-turn dialogue training strategy that jointly optimizes the Planner, Programmatic Filter, and Grounder within a unified framework. Extensive experiments demonstrate state-of-the-art performance. Notably, on our low-level grounding task, Prune4Web dramatically improves accuracy from 46.8% to 88.28%, underscoring its efficacy in real-world web automation.

