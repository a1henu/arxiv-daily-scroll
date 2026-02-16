---
layout: default
title: INHerit-SG: Incremental Hierarchical Semantic Scene Graphs with RAG-Style Retrieval
---

# INHerit-SG: Incremental Hierarchical Semantic Scene Graphs with RAG-Style Retrieval
**arXiv**：[2602.12971v1](https://arxiv.org/abs/2602.12971) · [PDF](https://arxiv.org/pdf/2602.12971.pdf)  
**作者**：YukTungSamuel Fang, Zhikang Shi, Jiabin Qiu, Zixuan Chen, Jieqi Shi, Hao Xu, Jing Huo, Yang Gao  

**一句话要点**：提出INHerit-SG以解决机器人导航中语义场景图与具身任务需求不匹配的问题。

**关键词**：语义场景图, 机器人导航, 检索增强生成, 层次化结构, 异步处理, 可解释推理

## 3 点简述
- 现有语义场景图方法依赖离线处理或隐式特征，难以支持复杂环境中可解释的人类意图推理。
- INHerit-SG采用异步双进程架构和层次化结构，将几何分割与语义推理解耦，并通过事件触发更新保持长期一致性。
- 在HM3DSem-SQR数据集和真实环境中评估，系统在复杂查询上达到先进性能，并展示下游导航任务的可扩展性。

## 摘要（原文）

> Driven by advancements in foundation models, semantic scene graphs have emerged as a prominent paradigm for high-level 3D environmental abstraction in robot navigation. However, existing approaches are fundamentally misaligned with the needs of embodied tasks. As they rely on either offline batch processing or implicit feature embeddings, the maps can hardly support interpretable human-intent reasoning in complex environments. To address these limitations, we present INHerit-SG. We redefine the map as a structured, RAG-ready knowledge base where natural-language descriptions are introduced as explicit semantic anchors to better align with human intent. An asynchronous dual-process architecture, together with a Floor-Room-Area-Object hierarchy, decouples geometric segmentation from time-consuming semantic reasoning. An event-triggered map update mechanism reorganizes the graph only when meaningful semantic events occur. This strategy enables our graph to maintain long-term consistency with relatively low computational overhead. For retrieval, we deploy multi-role Large Language Models (LLMs) to decompose queries into atomic constraints and handle logical negations, and employ a hard-to-soft filtering strategy to ensure robust reasoning. This explicit interpretability improves the success rate and reliability of complex retrievals, enabling the system to adapt to a broader spectrum of human interaction tasks. We evaluate INHerit-SG on a newly constructed dataset, HM3DSem-SQR, and in real-world environments. Experiments demonstrate that our system achieves state-of-the-art performance on complex queries, and reveal its scalability for downstream navigation tasks. Project Page: https://fangyuktung.github.io/INHeritSG.github.io/

