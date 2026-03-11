---
layout: default
title: Learning the Hierarchical Organization in Brain Network for Brain Disorder Diagnosis
---

# Learning the Hierarchical Organization in Brain Network for Brain Disorder Diagnosis
**arXiv**：[2603.09606v1](https://arxiv.org/abs/2603.09606) · [PDF](https://arxiv.org/pdf/2603.09606.pdf)  
**作者**：Jingfeng Tang, Peng Cao, Guangqi Wen, Jinzhu Yang, Xiaoli Liu, Osmar R. Zaiane  

**一句话要点**：提出BrainHO以学习脑网络层次组织，用于脑疾病诊断

**关键词**：脑网络分析, 分层组织学习, 功能磁共振成像, 注意力机制, 脑疾病诊断, 生物标志物发现

## 3 点简述
- 现有方法依赖预定义子网络，忽略高相关跨网络交互模式
- 设计分层注意力机制，基于内在特征聚合节点捕获子图级连接模式
- 在ABIDE和REST-meta-MDD数据集上实现SOTA性能并发现可解释生物标志物

## 摘要（原文）

> Brain network analysis based on functional Magnetic Resonance Imaging (fMRI) is pivotal for diagnosing brain disorders. Existing approaches typically rely on predefined functional sub-networks to construct sub-network associations. However, we identified many cross-network interaction patterns with high Pearson correlations that this strict, prior-based organization fails to capture. To overcome this limitation, we propose the Brain Hierarchical Organization Learning (BrainHO) to learn inherently hierarchical brain network dependencies based on their intrinsic features rather than predefined sub-network labels. Specifically, we design a hierarchical attention mechanism that allows the model to aggregate nodes into a hierarchical organization, effectively capturing intricate connectivity patterns at the subgraph level. To ensure diverse, complementary, and stable organizations, we incorporate an orthogonality constraint loss, alongside a hierarchical consistency constraint strategy, to refine node-level features using high-level graph semantics. Extensive experiments on the publicly available ABIDE and REST-meta-MDD datasets demonstrate that BrainHO not only achieves state-of-the-art classification performance but also uncovers interpretable, clinically significant biomarkers by precisely localizing disease-related sub-networks.

