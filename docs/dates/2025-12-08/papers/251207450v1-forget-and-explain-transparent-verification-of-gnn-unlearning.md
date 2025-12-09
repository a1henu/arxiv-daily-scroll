---
layout: default
title: Forget and Explain: Transparent Verification of GNN Unlearning
---

# Forget and Explain: Transparent Verification of GNN Unlearning
**arXiv**：[2512.07450v1](https://arxiv.org/abs/2512.07450) · [PDF](https://arxiv.org/pdf/2512.07450.pdf)  
**作者**：Imran Ahsan, Hyunwook Yu, Jinsung Kim, Mucheol Kim  

**一句话要点**：提出基于可解释性的验证器以透明验证图神经网络遗忘效果

**关键词**：图神经网络遗忘, 可解释性验证, 隐私保护, 归因分析, 图编辑距离

## 3 点简述
- 核心问题：图神经网络遗忘缺乏透明度，难以验证信息是否真正删除
- 方法要点：利用归因偏移和局部结构变化作为透明证据，定义五种可解释性指标
- 实验或效果：评估多种遗忘策略，结果显示Retrain和GNNDelete接近完全遗忘，解释差异提供主要证据

## 摘要（原文）

> Graph neural networks (GNNs) are increasingly used to model complex patterns in graph-structured data. However, enabling them to "forget" designated information remains challenging, especially under privacy regulations such as the GDPR. Existing unlearning methods largely optimize for efficiency and scalability, yet they offer little transparency, and the black-box nature of GNNs makes it difficult to verify whether forgetting has truly occurred. We propose an explainability-driven verifier for GNN unlearning that snapshots the model before and after deletion, using attribution shifts and localized structural changes (for example, graph edit distance) as transparent evidence. The verifier uses five explainability metrics: residual attribution, heatmap shift, explainability score deviation, graph edit distance, and a diagnostic graph rule shift. We evaluate two backbones (GCN, GAT) and four unlearning strategies (Retrain, GraphEditor, GNNDelete, IDEA) across five benchmarks (Cora, Citeseer, Pubmed, Coauthor-CS, Coauthor-Physics). Results show that Retrain and GNNDelete achieve near-complete forgetting, GraphEditor provides partial erasure, and IDEA leaves residual signals. These explanation deltas provide the primary, human-readable evidence of forgetting; we also report membership-inference ROC-AUC as a complementary, graph-wide privacy signal.

