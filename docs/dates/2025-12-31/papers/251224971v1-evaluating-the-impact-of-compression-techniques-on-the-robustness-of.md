---
layout: default
title: Evaluating the Impact of Compression Techniques on the Robustness of CNNs under Natural Corruptions
---

# Evaluating the Impact of Compression Techniques on the Robustness of CNNs under Natural Corruptions
**arXiv**：[2512.24971v1](https://arxiv.org/abs/2512.24971) · [PDF](https://arxiv.org/pdf/2512.24971.pdf)  
**作者**：Itallo Patrick Castro Alves Da Silva, Emanuel Adler Medeiros Pereira, Erick de Andrade Barboza, Baldoino Fonseca dos Santos Neto, Marcio de Medeiros Ribeiro  

**一句话要点**：评估压缩技术对CNN在自然损坏下鲁棒性的影响，揭示组合策略可提升鲁棒性

**关键词**：模型压缩, 鲁棒性评估, 卷积神经网络, 自然损坏, 多目标优化

## 3 点简述
- 核心问题：模型压缩可能影响CNN在自然损坏环境下的鲁棒性，需在验证中考虑鲁棒性评估
- 方法要点：综合评估量化、剪枝和权重聚类等压缩技术，单独或组合应用于ResNet-50、VGG-19和MobileNetV2
- 实验或效果：使用CIFAR-10-C和CIFAR-100-C数据集分析鲁棒性、准确性和压缩率权衡，发现定制组合可改善鲁棒性

## 摘要（原文）

> Compressed deep learning models are crucial for deploying computer vision systems on resource-constrained devices. However, model compression may affect robustness, especially under natural corruption. Therefore, it is important to consider robustness evaluation while validating computer vision systems. This paper presents a comprehensive evaluation of compression techniques - quantization, pruning, and weight clustering applied individually and in combination to convolutional neural networks (ResNet-50, VGG-19, and MobileNetV2). Using the CIFAR-10-C and CIFAR 100-C datasets, we analyze the trade-offs between robustness, accuracy, and compression ratio. Our results show that certain compression strategies not only preserve but can also improve robustness, particularly on networks with more complex architectures. Utilizing multiobjective assessment, we determine the best configurations, showing that customized technique combinations produce beneficial multi-objective results. This study provides insights into selecting compression methods for robust and efficient deployment of models in corrupted real-world environments.

