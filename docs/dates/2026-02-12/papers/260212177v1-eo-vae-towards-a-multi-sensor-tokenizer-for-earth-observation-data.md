---
layout: default
title: EO-VAE: Towards A Multi-sensor Tokenizer for Earth Observation Data
---

# EO-VAE: Towards A Multi-sensor Tokenizer for Earth Observation Data
**arXiv**：[2602.12177v1](https://arxiv.org/abs/2602.12177) · [PDF](https://arxiv.org/pdf/2602.12177.pdf)  
**作者**：Nils Lehmann, Yi Wang, Zhitong Xiong, Xiaoxiang Zhu  

**一句话要点**：提出EO-VAE作为多传感器地球观测数据的统一分词器，以应对传感器多样性和光谱通道可变性挑战。

**关键词**：地球观测数据, 多传感器分词器, 变分自编码器, 动态超网络, 遥感生成建模, 重建保真度

## 3 点简述
- 地球观测数据因传感器规格多样和光谱通道可变，传统RGB生成模型的分词器难以直接应用。
- EO-VAE采用动态超网络，单一模型可编码和重建灵活通道组合，避免为每种模态训练独立分词器。
- 在TerraMesh数据集上，EO-VAE相比TerraMind分词器实现更优重建保真度，为遥感潜在生成建模奠定基础。

## 摘要（原文）

> State-of-the-art generative image and video models rely heavily on tokenizers that compress high-dimensional inputs into more efficient latent representations. While this paradigm has revolutionized RGB generation, Earth observation (EO) data presents unique challenges due to diverse sensor specifications and variable spectral channels. We propose EO-VAE, a multi-sensor variational autoencoder designed to serve as a foundational tokenizer for the EO domain. Unlike prior approaches that train separate tokenizers for each modality, EO-VAE utilizes a single model to encode and reconstruct flexible channel combinations via dynamic hypernetworks. Our experiments on the TerraMesh dataset demonstrate that EO-VAE achieves superior reconstruction fidelity compared to the TerraMind tokenizers, establishing a robust baseline for latent generative modeling in remote sensing.

