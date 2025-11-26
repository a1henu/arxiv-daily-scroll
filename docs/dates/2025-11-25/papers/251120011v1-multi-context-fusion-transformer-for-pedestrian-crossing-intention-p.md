---
layout: default
title: Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments
---

# Multi-Context Fusion Transformer for Pedestrian Crossing Intention Prediction in Urban Environments
**arXiv**：[2511.20011v1](https://arxiv.org/abs/2511.20011) · [PDF](https://arxiv.org/pdf/2511.20011.pdf)  
**作者**：Yuanzhe Li, Hang Zhong, Steffen Müller  

**一句话要点**：提出多上下文融合Transformer以提升城市环境中行人过街意图预测准确性

**关键词**：行人意图预测, 多上下文融合, Transformer模型, 注意力机制, 自动驾驶安全

## 3 点简述
- 城市环境中行人意图预测受多因素影响，准确性低
- 融合四种上下文，采用渐进注意力机制实现特征交互与集成
- 在JAADbeh等数据集上准确率达73%至93%，优于现有方法

## 摘要（原文）

> Pedestrian crossing intention prediction is essential for autonomous vehicles to improve pedestrian safety and reduce traffic accidents. However, accurate pedestrian intention prediction in urban environments remains challenging due to the multitude of factors affecting pedestrian behavior. In this paper, we propose a multi-context fusion Transformer (MFT) that leverages diverse numerical contextual attributes across four key dimensions, encompassing pedestrian behavior context, environmental context, pedestrian localization context and vehicle motion context, to enable accurate pedestrian intention prediction. MFT employs a progressive fusion strategy, where mutual intra-context attention enables reciprocal interactions within each context, thereby facilitating feature sequence fusion and yielding a context token as a context-specific representation. This is followed by mutual cross-context attention, which integrates features across contexts with a global CLS token serving as a compact multi-context representation. Finally, guided intra-context attention refines context tokens within each context through directed interactions, while guided cross-context attention strengthens the global CLS token to promote multi-context fusion via guided information propagation, yielding deeper and more efficient integration. Experimental results validate the superiority of MFT over state-of-the-art methods, achieving accuracy rates of 73%, 93%, and 90% on the JAADbeh, JAADall, and PIE datasets, respectively. Extensive ablation studies are further conducted to investigate the effectiveness of the network architecture and contribution of different input context. Our code is open-source: https://github.com/ZhongHang0307/Multi-Context-Fusion-Transformer.

