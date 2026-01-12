---
layout: default
title: CyberGFM: Graph Foundation Models for Lateral Movement Detection in Enterprise Networks
---

# CyberGFM: Graph Foundation Models for Lateral Movement Detection in Enterprise Networks
**arXiv**：[2601.05988v1](https://arxiv.org/abs/2601.05988) · [PDF](https://arxiv.org/pdf/2601.05988.pdf)  
**作者**：Isaiah J. King, Bernardo Trindade, Benjamin Bowman, H. Howie Huang  

**一句话要点**：提出CyberGFM图基础模型，结合随机游走与Transformer以提升企业网络横向移动检测效果。

**关键词**：图基础模型, 横向移动检测, 随机游走, Transformer, 链接预测, 网络异常检测

## 3 点简述
- 现有方法在随机游走中无法利用丰富边数据，或GNN训练内存需求大。
- 扩展随机游走类比句子至Transformer基础模型，快速训练并微调用于链接预测。
- 在三个数据集上实现SOTA，平均精度提升达2倍，参数相同且效率相当或更优。

## 摘要（原文）

> Representing networks as a graph and training a link prediction model using benign connections is an effective method of anomaly-based intrusion detection. Existing works using this technique have shown great success using temporal graph neural networks and skip-gram-based approaches on random walks. However, random walk-based approaches are unable to incorporate rich edge data, while the GNN-based approaches require large amounts of memory to train. In this work, we propose extending the original insight from random walk-based skip-grams--that random walks through a graph are analogous to sentences in a corpus--to the more modern transformer-based foundation models. Using language models that take advantage of GPU optimizations, we can quickly train a graph foundation model to predict missing tokens in random walks through a network of computers. The graph foundation model is then finetuned for link prediction and used as a network anomaly detector. This new approach allows us to combine the efficiency of random walk-based methods and the rich semantic representation of deep learning methods. This system, which we call CyberGFM, achieved state-of-the-art results on three widely used network anomaly detection datasets, delivering a up to 2$\times$ improvement in average precision. We found that CyberGFM outperforms all prior works in unsupervised link prediction for network anomaly detection, using the same number of parameters, and with equal or better efficiency than the previous best approaches.

