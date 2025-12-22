---
layout: default
title: Video Detective: Seek Critical Clues Recurrently to Answer Question from Long Videos
---

# Video Detective: Seek Critical Clues Recurrently to Answer Question from Long Videos
**arXiv**：[2512.17229v1](https://arxiv.org/abs/2512.17229) · [PDF](https://arxiv.org/pdf/2512.17229.pdf)  
**作者**：Henghui Du, Chang Zhou, Chunjie Zhang, Xi Chen, Di Hu  

**一句话要点**：提出VideoDetective，通过循环搜索关键线索以解决长视频问答中的信息过载问题。

**关键词**：长视频问答, 多模态大语言模型, 问题感知压缩, 循环搜索, 关键线索提取

## 3 点简述
- 核心问题：长视频问答因信息过载和内存消耗大而挑战多模态大语言模型。
- 方法要点：采用问题感知压缩策略，循环处理视频子段以聚合关键线索。
- 实验或效果：在32K上下文长度下高效处理100K令牌，评估显示能更有效从海量信息中寻找关键线索。

## 摘要（原文）

> Long Video Question-Answering (LVQA) presents a significant challenge for Multi-modal Large Language Models (MLLMs) due to immense context and overloaded information, which could also lead to prohibitive memory consumption. While existing methods attempt to address these issues by reducing visual tokens or extending model's context length, they may miss useful information or take considerable computation. In fact, when answering given questions, only a small amount of crucial information is required. Therefore, we propose an efficient question-aware memory mechanism, enabling MLLMs to recurrently seek these critical clues. Our approach, named VideoDetective, simplifies this task by iteratively processing video sub-segments. For each sub-segment, a question-aware compression strategy is employed by introducing a few special memory tokens to achieve purposefully compression. This allows models to effectively seek critical clues while reducing visual tokens. Then, due to history context could have a significant impact, we recurrently aggregate and store these memory tokens to update history context, which would be reused for subsequent sub-segments. Furthermore, to more effectively measure model's long video understanding ability, we introduce GLVC (Grounding Long Video Clues), a long video question-answering dataset, which features grounding critical and concrete clues scattered throughout entire videos. Experimental results demonstrate our method enables MLLMs with limited context length of 32K to efficiently process 100K tokens (3600 frames, an hour-long video sampled at 1fps), requiring only 2 minutes and 37GB GPU memory usage. Evaluation results across multiple long video benchmarks illustrate our method can more effectively seek critical clues from massive information.

