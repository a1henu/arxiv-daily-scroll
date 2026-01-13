---
layout: default
title: ES-Mem: Event Segmentation-Based Memory for Long-Term Dialogue Agents
---

# ES-Mem: Event Segmentation-Based Memory for Long-Term Dialogue Agents
**arXiv**：[2601.07582v1](https://arxiv.org/abs/2601.07582) · [PDF](https://arxiv.org/pdf/2601.07582.pdf)  
**作者**：Huhai Zou, Tianhao Sun, Chuanjiang He, Yu Tian, Zhenyang Li, Li Jin, Nayu Liu, Jiang Zhong, Kaiwen Wei  

**一句话要点**：提出ES-Mem框架，基于事件分割理论解决长时对话代理中记忆碎片化和检索不精确问题。

**关键词**：长时对话代理, 事件分割理论, 分层记忆架构, 动态事件分割, 记忆检索, 对话分割

## 3 点简述
- 核心问题：现有记忆机制存在记忆粒度僵化和检索依赖表面语义相似性，导致记忆不连贯和上下文定位困难。
- 方法要点：引入动态事件分割模块划分语义连贯事件，构建分层记忆架构利用边界语义锚定特定情景记忆。
- 实验或效果：在两个记忆基准测试中表现优于基线方法，事件分割模块在对话分割数据集上展示稳健适用性。

## 摘要（原文）

> Memory is critical for dialogue agents to maintain coherence and enable continuous adaptation in long-term interactions. While existing memory mechanisms offer basic storage and retrieval capabilities, they are hindered by two primary limitations: (1) rigid memory granularity often disrupts semantic integrity, resulting in fragmented and incoherent memory units; (2) prevalent flat retrieval paradigms rely solely on surface-level semantic similarity, neglecting the structural cues of discourse required to navigate and locate specific episodic contexts. To mitigate these limitations, drawing inspiration from Event Segmentation Theory, we propose ES-Mem, a framework incorporating two core components: (1) a dynamic event segmentation module that partitions long-term interactions into semantically coherent events with distinct boundaries; (2) a hierarchical memory architecture that constructs multi-layered memories and leverages boundary semantics to anchor specific episodic memory for precise context localization. Evaluations on two memory benchmarks demonstrate that ES-Mem yields consistent performance gains over baseline methods. Furthermore, the proposed event segmentation module exhibits robust applicability on dialogue segmentation datasets.

