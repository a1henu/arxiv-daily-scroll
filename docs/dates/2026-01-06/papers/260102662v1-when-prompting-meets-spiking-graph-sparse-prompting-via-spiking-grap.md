---
layout: default
title: When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph Prompt Learning
---

# When Prompting Meets Spiking: Graph Sparse Prompting via Spiking Graph Prompt Learning
**arXiv**：[2601.02662v1](https://arxiv.org/abs/2601.02662) · [PDF](https://arxiv.org/pdf/2601.02662.pdf)  
**作者**：Bo Jiang, Weijun Zhao, Beibei Wang, Jin Tang  

**一句话要点**：提出SpikingGPF，利用脉冲神经元机制学习稀疏图提示以解决图提示特征冗余和噪声敏感问题。

**关键词**：图神经网络, 提示学习, 稀疏表示, 脉冲神经元, 图节点特征, 鲁棒性优化

## 3 点简述
- 核心问题：现有图提示特征方法在所有特征维度上提示，导致冗余且对节点噪声敏感。
- 方法要点：引入脉冲神经元架构学习稀疏提示向量，实现选择性特征提示，并基于稀疏表示理论优化提示表示。
- 实验或效果：在多个基准测试中验证了SpikingGPF的有效性和鲁棒性。

## 摘要（原文）

> Graph Prompt Feature (GPF) learning has been widely used in adapting pre-trained GNN model on the downstream task. GPFs first introduce some prompt atoms and then learns the optimal prompt vector for each graph node using the linear combination of prompt atoms. However, existing GPFs generally conduct prompting over node's all feature dimensions which is obviously redundant and also be sensitive to node feature noise. To overcome this issue, for the first time, this paper proposes learning sparse graph prompts by leveraging the spiking neuron mechanism, termed Spiking Graph Prompt Feature (SpikingGPF). Our approach is motivated by the observation that spiking neuron can perform inexpensive information processing and produce sparse outputs which naturally fits the task of our graph sparse prompting. Specifically, SpikingGPF has two main aspects. First, it learns a sparse prompt vector for each node by exploiting a spiking neuron architecture, enabling prompting on selective node features. This yields a more compact and lightweight prompting design while also improving robustness against node noise. Second, SpikingGPF introduces a novel prompt representation learning model based on sparse representation theory, i.e., it represents each node prompt as a sparse combination of prompt atoms. This encourages a more compact representation and also facilitates efficient computation. Extensive experiments on several benchmarks demonstrate the effectiveness and robustness of SpikingGPF.

