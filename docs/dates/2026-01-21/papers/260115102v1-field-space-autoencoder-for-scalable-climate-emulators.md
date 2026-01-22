---
layout: default
title: Field-Space Autoencoder for Scalable Climate Emulators
---

# Field-Space Autoencoder for Scalable Climate Emulators
**arXiv**：[2601.15102v1](https://arxiv.org/abs/2601.15102) · [PDF](https://arxiv.org/pdf/2601.15102.pdf)  
**作者**：Johannes Meuer, Maximilian Witte, Étiénne Plésiat, Thomas Ludwig, Christopher Kadow  

**一句话要点**：提出Field-Space Autoencoder以解决千米级气候模型计算成本高和数据量大的问题

**关键词**：气候模拟, 球面压缩, Field-Space Attention, 生成扩散模型, 零样本超分辨

## 3 点简述
- 千米级地球系统模型计算昂贵且输出数据量大，限制概率风险评估等应用
- 基于球面压缩模型，利用Field-Space Attention避免几何失真，优于卷积基线
- 生成结构化压缩场，支持零样本超分辨和生成扩散模型，融合低分辨率和高分辨率数据

## 摘要（原文）

> Kilometer-scale Earth system models are essential for capturing local climate change. However, these models are computationally expensive and produce petabyte-scale outputs, which limits their utility for applications such as probabilistic risk assessment. Here, we present the Field-Space Autoencoder, a scalable climate emulation framework based on a spherical compression model that overcomes these challenges. By utilizing Field-Space Attention, the model efficiently operates on native climate model output and therefore avoids geometric distortions caused by forcing spherical data onto Euclidean grids. This approach preserves physical structures significantly better than convolutional baselines. By producing a structured compressed field, it serves as a good baseline for downstream generative emulation. In addition, the model can perform zero-shot super-resolution that maps low-resolution large ensembles and scarce high-resolution data into a shared representation. We train a generative diffusion model on these compressed fields. The model can simultaneously learn internal variability from abundant low-resolution data and fine-scale physics from sparse high-resolution data. Our work bridges the gap between the high volume of low-resolution ensemble statistics and the scarcity of high-resolution physical detail.

