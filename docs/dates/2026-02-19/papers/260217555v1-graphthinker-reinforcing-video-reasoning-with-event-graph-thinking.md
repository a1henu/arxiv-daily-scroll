---
layout: default
title: GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking
---

# GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking
**arXiv**：[2602.17555v1](https://arxiv.org/abs/2602.17555) · [PDF](https://arxiv.org/pdf/2602.17555.pdf)  
**作者**：Zixu Cheng, Da Li, Jian Hu, Ziquan Liu, Wei Li, Shaogang Gong  

**一句话要点**：提出GraphThinker方法，通过事件图强化和视觉注意力奖励，减少视频推理中的幻觉问题。

**关键词**：视频推理, 事件图建模, 强化微调, 视觉注意力, 幻觉减少, 多模态大语言模型

## 3 点简述
- 视频推理中事件因果关系隐式且标注成本高，现有MLLMs缺乏显式因果建模，易产生幻觉。
- GraphThinker构建事件级场景图作为中间思考过程，并引入视觉注意力奖励进行强化微调。
- 在RexTime和VidHalluc数据集上，GraphThinker能更精确捕捉事件关系，减少幻觉，优于先前方法。

## 摘要（原文）

> Video reasoning requires understanding the causal relationships between events in a video. However, such relationships are often implicit and costly to annotate manually. While existing multimodal large language models (MLLMs) often infer event relations through dense captions or video summaries for video reasoning, such modeling still lacks causal understanding. Without explicit causal structure modeling within and across video events, these models suffer from hallucinations during the video reasoning. In this work, we propose GraphThinker, a reinforcement finetuning-based method that constructs structural event-level scene graphs and enhances visual grounding to jointly reduce hallucinations in video reasoning. Specifically, we first employ an MLLM to construct an event-based video scene graph (EVSG) that explicitly models both intra- and inter-event relations, and incorporate these formed scene graphs into the MLLM as an intermediate thinking process. We also introduce a visual attention reward during reinforcement finetuning, which strengthens video grounding and further mitigates hallucinations. We evaluate GraphThinker on two datasets, RexTime and VidHalluc, where it shows superior ability to capture object and event relations with more precise event localization, reducing hallucinations in video reasoning compared to prior methods.

