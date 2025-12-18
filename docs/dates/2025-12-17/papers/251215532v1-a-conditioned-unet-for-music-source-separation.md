---
layout: default
title: A Conditioned UNet for Music Source Separation
---

# A Conditioned UNet for Music Source Separation
**arXiv**：[2512.15532v1](https://arxiv.org/abs/2512.15532) · [PDF](https://arxiv.org/pdf/2512.15532.pdf)  
**作者**：Ken O'Hanlon, Basil Woods, Lin Wang, Mark Sandler  

**一句话要点**：提出QSCNet，一种基于条件UNet的音乐源分离方法，以解决传统方法依赖固定乐器词汇的问题。

**关键词**：音乐源分离, 条件UNet, 稀疏压缩网络, 音频查询, MoisesDb数据集, 参数效率

## 3 点简述
- 核心问题：传统音乐源分离依赖固定乐器词汇，限制了实际应用；条件方法因数据不足而潜力未充分展现。
- 方法要点：QSCNet结合条件UNet和稀疏压缩网络，通过音频查询实现灵活源分离，无需预定义词汇。
- 实验或效果：在MoisesDb数据集上，QSCNet以少于一半参数超越Banquet方法，SNR提升超过1dB。

## 摘要（原文）

> In this paper we propose a conditioned UNet for Music Source Separation (MSS). MSS is generally performed by multi-output neural networks, typically UNets, with each output representing a particular stem from a predefined instrument vocabulary. In contrast, conditioned MSS networks accept an audio query related to a stem of interest alongside the signal from which that stem is to be extracted. Thus, a strict vocabulary is not required and this enables more realistic tasks in MSS. The potential of conditioned approaches for such tasks has been somewhat hidden due to a lack of suitable data, an issue recently addressed with the MoisesDb dataset. A recent method, Banquet, employs this dataset with promising results seen on larger vocabularies. Banquet uses Bandsplit RNN rather than a UNet and the authors state that UNets should not be suitable for conditioned MSS. We counter this argument and propose QSCNet, a novel conditioned UNet for MSS that integrates network conditioning elements in the Sparse Compressed Network for MSS. We find QSCNet to outperform Banquet by over 1dB SNR on a couple of MSS tasks, while using less than half the number of parameters.

