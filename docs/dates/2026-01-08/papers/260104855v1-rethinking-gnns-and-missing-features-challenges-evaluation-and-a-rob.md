---
layout: default
title: Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution
---

# Rethinking GNNs and Missing Features: Challenges, Evaluation and a Robust Solution
**arXiv**：[2601.04855v1](https://arxiv.org/abs/2601.04855) · [PDF](https://arxiv.org/pdf/2601.04855.pdf)  
**作者**：Francesco Ferrini, Veronica Lachi, Antonio Longa, Bruno Lepri, Matono Akiyoshi, Andrea Passerini, Xin Liu, Manfred Jaeger  

**一句话要点**：提出GNNmim以解决图神经网络在节点特征缺失场景下的鲁棒性问题

**关键词**：图神经网络, 缺失特征处理, 节点分类, 鲁棒性评估, 缺失机制

## 3 点简述
- 核心问题：现有研究在稀疏特征和随机缺失机制下评估不足，难以反映真实挑战
- 方法要点：引入密集特征数据集和更真实缺失机制，提出GNNmim作为简单有效基线
- 实验或效果：GNNmim在多样化数据集和缺失机制下与专用架构竞争

## 摘要（原文）

> Handling missing node features is a key challenge for deploying Graph Neural Networks (GNNs) in real-world domains such as healthcare and sensor networks. Existing studies mostly address relatively benign scenarios, namely benchmark datasets with (a) high-dimensional but sparse node features and (b) incomplete data generated under Missing Completely At Random (MCAR) mechanisms. For (a), we theoretically prove that high sparsity substantially limits the information loss caused by missingness, making all models appear robust and preventing a meaningful comparison of their performance. To overcome this limitation, we introduce one synthetic and three real-world datasets with dense, semantically meaningful features. For (b), we move beyond MCAR and design evaluation protocols with more realistic missingness mechanisms. Moreover, we provide a theoretical background to state explicit assumptions on the missingness process and analyze their implications for different methods. Building on this analysis, we propose GNNmim, a simple yet effective baseline for node classification with incomplete feature data. Experiments show that GNNmim is competitive with respect to specialized architectures across diverse datasets and missingness regimes.

