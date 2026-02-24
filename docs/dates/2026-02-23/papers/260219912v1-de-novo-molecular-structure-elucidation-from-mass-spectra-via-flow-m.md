---
layout: default
title: De novo molecular structure elucidation from mass spectra via flow matching
---

# De novo molecular structure elucidation from mass spectra via flow matching
**arXiv**：[2602.19912v1](https://arxiv.org/abs/2602.19912) · [PDF](https://arxiv.org/pdf/2602.19912.pdf)  
**作者**：Ghaith Mqawass, Tuan Le, Fabian Theis, Djork-Arné Clevert  

**一句话要点**：提出MSFlow两阶段流匹配生成模型，用于从质谱数据解析小分子结构。

**关键词**：质谱解析, 流匹配生成模型, 分子结构重建, Transformer编码, 小分子结构

## 3 点简述
- 核心问题：质谱解析为分子结构是困难且欠定义的逆问题，阻碍生物和化学研究。
- 方法要点：采用公式限制Transformer编码质谱，流匹配解码器从嵌入重建分子结构。
- 实验或效果：MSFlow准确解析45%质谱，比现有最佳方法提升高达14倍。

## 摘要（原文）

> Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

