---
layout: default
title: Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation
---

# Temporal Graph Network: Hallucination Detection in Multi-Turn Conversation
**arXiv**：[2601.03051v1](https://arxiv.org/abs/2601.03051) · [PDF](https://arxiv.org/pdf/2601.03051.pdf)  
**作者**：Vidhi Rathore, Sambu Aneesh, Himanshu Singh  

**一句话要点**：提出基于时序图网络的对话级幻觉检测方法，用于多轮对话场景。

**关键词**：对话幻觉检测, 时序图网络, 消息传递, 注意力机制, 多轮对话

## 3 点简述
- 核心问题：多轮对话中上下文变化和矛盾可能导致AI系统产生幻觉。
- 方法要点：将对话建模为时序图，通过共享实体边和时序边连接节点，使用消息传递更新嵌入。
- 实验或效果：方法性能略优于现有方法，注意力机制可解释决策过程。

## 摘要（原文）

> Hallucinations can be produced by conversational AI systems, particularly in multi-turn conversations where context changes and contradictions may eventually surface. By representing the entire conversation as a temporal graph, we present a novel graph-based method for detecting dialogue-level hallucinations. Our framework models each dialogue as a node, encoding it using a sentence transformer. We explore two different ways of connectivity: i) shared-entity edges, which connect turns that refer to the same entities; ii) temporal edges, which connect contiguous turns in the conversation. Message-passing is used to update the node embeddings, allowing flow of information between related nodes. The context-aware node embeddings are then combined using attention pooling into a single vector, which is then passed on to a classifier to determine the presence and type of hallucinations. We demonstrate that our method offers slightly improved performance over existing methods. Further, we show the attention mechanism can be used to justify the decision making process. The code and model weights are made available at: https://github.com/sambuaneesh/anlp-project.

