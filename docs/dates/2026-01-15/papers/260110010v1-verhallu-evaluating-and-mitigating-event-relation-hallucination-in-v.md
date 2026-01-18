---
layout: default
title: VERHallu: Evaluating and Mitigating Event Relation Hallucination in Video Large Language Models
---

# VERHallu: Evaluating and Mitigating Event Relation Hallucination in Video Large Language Models
**arXiv**：[2601.10010v1](https://arxiv.org/abs/2601.10010) · [PDF](https://arxiv.org/pdf/2601.10010.pdf)  
**作者**：Zefan Zhang, Kehua Zhu, Shijie Jiang, Hongyuan Lu, Shengkai Sun, Tian Bai  

**一句话要点**：提出VERHallu基准与KFP策略，以评估和缓解视频大语言模型中的事件关系幻觉问题

**关键词**：视频大语言模型, 事件关系幻觉, 基准评估, 注意力机制, 多事件推理

## 3 点简述
- 核心问题：现有研究忽视视频事件关系幻觉，模型依赖先验知识而忽略帧级线索
- 方法要点：构建VERHallu基准评估因果、时序等关系，提出KFP策略重分配帧级注意力
- 实验效果：KFP策略有效缓解事件关系幻觉，且不影响推理速度

## 摘要（原文）

> Video Large Language Models (VideoLLMs) exhibit various types of hallucinations. Existing research has primarily focused on hallucinations involving the presence of events, objects, and scenes in videos, while largely neglecting event relation hallucination. In this paper, we introduce a novel benchmark for evaluating the Video Event Relation Hallucination, named VERHallu. This benchmark focuses on causal, temporal, and subevent relations between events, encompassing three types of tasks: relation classification, question answering, and counterfactual question answering, for a comprehensive evaluation of event relation hallucination. Additionally, it features counterintuitive video scenarios that deviate from typical pretraining distributions, with each sample accompanied by human-annotated candidates covering both vision-language and pure language biases. Our analysis reveals that current state-of-the-art VideoLLMs struggle with dense-event relation reasoning, often relying on prior knowledge due to insufficient use of frame-level cues. Although these models demonstrate strong grounding capabilities for key events, they often overlook the surrounding subevents, leading to an incomplete and inaccurate understanding of event relations. To tackle this, we propose a Key-Frame Propagating (KFP) strategy, which reallocates frame-level attention within intermediate layers to enhance multi-event understanding. Experiments show it effectively mitigates the event relation hallucination without affecting inference speed.

