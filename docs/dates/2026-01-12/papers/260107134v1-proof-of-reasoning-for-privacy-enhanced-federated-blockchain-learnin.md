---
layout: default
title: Proof of Reasoning for Privacy Enhanced Federated Blockchain Learning at the Edge
---

# Proof of Reasoning for Privacy Enhanced Federated Blockchain Learning at the Edge
**arXiv**：[2601.07134v1](https://arxiv.org/abs/2601.07134) · [PDF](https://arxiv.org/pdf/2601.07134.pdf)  
**作者**：James Calo, Benny Lo  

**一句话要点**：提出Proof of Reasoning共识机制，以解决边缘联邦区块链学习中隐私保护与高效聚合问题。

**关键词**：联邦学习, 区块链共识, 隐私保护, 边缘计算, 物联网网络, 模型聚合

## 3 点简述
- 核心问题：现有区块链共识机制不直接支持联邦学习，缺乏隐私保护和高效聚合方法。
- 方法要点：集成掩码自编码器、边缘下游分类器训练和可验证聚合，实现数据隐私和低计算复杂度。
- 实验或效果：在大型物联网网络中实现低延迟、高准确性和适应性，抵御恶意攻击。

## 摘要（原文）

> Consensus mechanisms are the core of any blockchain system. However, the majority of these mechanisms do not target federated learning directly nor do they aid in the aggregation step. This paper introduces Proof of Reasoning (PoR), a novel consensus mechanism specifically designed for federated learning using blockchain, aimed at preserving data privacy, defending against malicious attacks, and enhancing the validation of participating networks. Unlike generic blockchain consensus mechanisms commonly found in the literature, PoR integrates three distinct processes tailored for federated learning. Firstly, a masked autoencoder (MAE) is trained to generate an encoder that functions as a feature map and obfuscates input data, rendering it resistant to human reconstruction and model inversion attacks. Secondly, a downstream classifier is trained at the edge, receiving input from the trained encoder. The downstream network's weights, a single encoded datapoint, the network's output and the ground truth are then added to a block for federated aggregation. Lastly, this data facilitates the aggregation of all participating networks, enabling more complex and verifiable aggregation methods than previously possible. This three-stage process results in more robust networks with significantly reduced computational complexity, maintaining high accuracy by training only the downstream classifier at the edge. PoR scales to large IoT networks with low latency and storage growth, and adapts to evolving data, regulations, and network conditions.

