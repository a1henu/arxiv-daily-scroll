---
layout: default
title: FSX: Message Flow Sensitivity Enhanced Structural Explainer for Graph Neural Networks
---

# FSX: Message Flow Sensitivity Enhanced Structural Explainer for Graph Neural Networks
**arXiv**：[2601.14730v1](https://arxiv.org/abs/2601.14730) · [PDF](https://arxiv.org/pdf/2601.14730.pdf)  
**作者**：Bizu Feng, Zhimu Yang, Shaode Yu, Zixin Hu  

**一句话要点**：提出FSX框架，结合消息流敏感性与合作博弈，高效解释图神经网络预测的结构逻辑。

**关键词**：图神经网络解释, 消息流分析, 合作博弈, 结构敏感性, Shapley值, 计算效率

## 3 点简述
- 核心问题：现有GNN解释方法在计算效率与结构交互捕获间存在权衡，梯度法忽略结构，博弈法计算开销大且可能偏离真实推理路径。
- 方法要点：通过流敏感性分析识别关键消息流，投影为子图，在子图中应用流感知合作博弈评估节点贡献，结合特征重要性和流稳定性角色。
- 实验或效果：在多数据集和GNN架构上验证，FSX在解释保真度和运行时间上优于现有方法，提供对结构逻辑的新见解。

## 摘要（原文）

> Despite the widespread success of Graph Neural Networks (GNNs), understanding the reasons behind their specific predictions remains challenging. Existing explainability methods face a trade-off that gradient-based approaches are computationally efficient but often ignore structural interactions, while game-theoretic techniques capture interactions at the cost of high computational overhead and potential deviation from the model's true reasoning path. To address this gap, we propose FSX (Message Flow Sensitivity Enhanced Structural Explainer), a novel hybrid framework that synergistically combines the internal message flows of the model with a cooperative game approach applied to the external graph data. FSX first identifies critical message flows via a novel flow-sensitivity analysis: during a single forward pass, it simulates localized node perturbations and measures the resulting changes in message flow intensities. These sensitivity-ranked flows are then projected onto the input graph to define compact, semantically meaningful subgraphs. Within each subgraph, a flow-aware cooperative game is conducted, where node contributions are evaluated fairly through a Shapley-like value that incorporates both node-feature importance and their roles in sustaining or destabilizing the identified critical flows. Extensive evaluation across multiple datasets and GNN architectures demonstrates that FSX achieves superior explanation fidelity with significantly reduced runtime, while providing unprecedented insights into the structural logic underlying model predictions--specifically, how important sub-structures exert influence by governing the stability of key internal computational pathways.

