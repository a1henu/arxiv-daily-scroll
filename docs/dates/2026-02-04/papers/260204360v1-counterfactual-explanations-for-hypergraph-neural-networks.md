---
layout: default
title: Counterfactual Explanations for Hypergraph Neural Networks
---

# Counterfactual Explanations for Hypergraph Neural Networks
**arXiv**：[2602.04360v1](https://arxiv.org/abs/2602.04360) · [PDF](https://arxiv.org/pdf/2602.04360.pdf)  
**作者**：Fabiano Veglianti, Lorenzo Antonelli, Gabriele Tolomei  

**一句话要点**：提出CF-HyperGNNExplainer以生成超图神经网络的对抗性解释，解决高风险场景中的可解释性问题。

**关键词**：超图神经网络, 对抗性解释, 可解释人工智能, 高阶交互建模, 结构编辑

## 3 点简述
- 超图神经网络（HGNNs）能有效建模高阶交互，但可解释性差，限制其在高风险场景的应用。
- CF-HyperGNNExplainer通过移除节点-超边关联或删除超边，生成最小结构变化的对抗性超图解释。
- 在三个基准数据集上实验验证，该方法能生成有效且简洁的对抗性解释，突出对HGNN决策最关键的高阶关系。

## 摘要（原文）

> Hypergraph neural networks (HGNNs) effectively model higher-order interactions in many real-world systems but remain difficult to interpret, limiting their deployment in high-stakes settings.
>   We introduce CF-HyperGNNExplainer, a counterfactual explanation method for HGNNs that identifies the minimal structural changes required to alter a model's prediction. The method generates counterfactual hypergraphs using actionable edits limited to removing node-hyperedge incidences or deleting hyperedges, producing concise and structurally meaningful explanations. Experiments on three benchmark datasets show that CF-HyperGNNExplainer generates valid and concise counterfactuals, highlighting the higher-order relations most critical to HGNN decisions.

