---
layout: default
title: Bridging Graph Structure and Knowledge-Guided Editing for Interpretable Temporal Knowledge Graph Reasoning
---

# Bridging Graph Structure and Knowledge-Guided Editing for Interpretable Temporal Knowledge Graph Reasoning
**arXiv**：[2601.21978v1](https://arxiv.org/abs/2601.21978) · [PDF](https://arxiv.org/pdf/2601.21978.pdf)  
**作者**：Shiqi Fan, Quanming Yao, Hongyi Nie, Wentao Ma, Zhen Wang, Wen Hua  

**一句话要点**：提出IGETR框架，结合图神经网络与LLM，解决时序知识图谱推理中的结构信息缺失与幻觉问题。

**关键词**：时序知识图谱推理, 图神经网络, 大语言模型, 路径编辑, 可解释推理, 混合框架

## 3 点简述
- 核心问题：现有LLM方法忽视动态图结构，导致推理不准确且易产生幻觉。
- 方法要点：采用三阶段流程，包括时序GNN路径提取、LLM引导路径编辑和集成预测。
- 实验或效果：在ICEWS数据集上，Hits@1和Hits@3相对提升达5.6%和8.1%。

## 摘要（原文）

> Temporal knowledge graph reasoning (TKGR) aims to predict future events by inferring missing entities with dynamic knowledge structures. Existing LLM-based reasoning methods prioritize contextual over structural relations, struggling to extract relevant subgraphs from dynamic graphs. This limits structural information understanding, leading to unstructured, hallucination-prone inferences especially with temporal inconsistencies. To address this problem, we propose IGETR (Integration of Graph and Editing-enhanced Temporal Reasoning), a hybrid reasoning framework that combines the structured temporal modeling capabilities of Graph Neural Networks (GNNs) with the contextual understanding of LLMs. IGETR operates through a three-stage pipeline. The first stage aims to ground the reasoning process in the actual data by identifying structurally and temporally coherent candidate paths through a temporal GNN, ensuring that inference starts from reliable graph-based evidence. The second stage introduces LLM-guided path editing to address logical and semantic inconsistencies, leveraging external knowledge to refine and enhance the initial paths. The final stage focuses on integrating the refined reasoning paths to produce predictions that are both accurate and interpretable. Experiments on standard TKG benchmarks show that IGETR achieves state-of-the-art performance, outperforming strong baselines with relative improvements of up to 5.6% on Hits@1 and 8.1% on Hits@3 on the challenging ICEWS datasets. Additionally, we execute ablation studies and additional analyses confirm the effectiveness of each component.

