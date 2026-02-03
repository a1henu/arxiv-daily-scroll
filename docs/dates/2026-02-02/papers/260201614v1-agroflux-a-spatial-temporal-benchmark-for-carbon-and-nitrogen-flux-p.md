---
layout: default
title: AgroFlux: A Spatial-Temporal Benchmark for Carbon and Nitrogen Flux Prediction in Agricultural Ecosystems
---

# AgroFlux: A Spatial-Temporal Benchmark for Carbon and Nitrogen Flux Prediction in Agricultural Ecosystems
**arXiv**：[2602.01614v1](https://arxiv.org/abs/2602.01614) · [PDF](https://arxiv.org/pdf/2602.01614.pdf)  
**作者**：Qi Cheng, Licheng Liu, Yao Zhang, Mu Hong, Yiqun Xie, Xiaowei Jia  

**一句话要点**：提出首个时空农业生态系统温室气体基准数据集AgroFlux，用于碳氮通量预测

**关键词**：农业生态系统, 温室气体通量预测, 时空基准数据集, 序列深度学习, 迁移学习, 碳氮通量

## 3 点简述
- 核心问题：农业生态系统温室气体排放量化面临数据稀疏、时空异质性和复杂过程等挑战，缺乏AI就绪基准数据集。
- 方法要点：整合基于物理的模型模拟和真实观测数据，构建时空基准数据集，并评估序列深度学习模型性能。
- 实验或效果：探索迁移学习以提升模型泛化能力，促进AI驱动农业生态系统模型发展。

## 摘要（原文）

> Agroecosystem, which heavily influenced by human actions and accounts for a quarter of global greenhouse gas emissions (GHGs), plays a crucial role in mitigating global climate change and securing environmental sustainability. However, we can't manage what we can't measure. Accurately quantifying the pools and fluxes in the carbon, nutrient, and water nexus of the agroecosystem is therefore essential for understanding the underlying drivers of GHG and developing effective mitigation strategies. Conventional approaches like soil sampling, process-based models, and black-box machine learning models are facing challenges such as data sparsity, high spatiotemporal heterogeneity, and complex subsurface biogeochemical and physical processes. Developing new trustworthy approaches such as AI-empowered models, will require the AI-ready benchmark dataset and outlined protocols, which unfortunately do not exist. In this work, we introduce a first-of-its-kind spatial-temporal agroecosystem GHG benchmark dataset that integrates physics-based model simulations from Ecosys and DayCent with real-world observations from eddy covariance flux towers and controlled-environment facilities. We evaluate the performance of various sequential deep learning models on carbon and nitrogen flux prediction, including LSTM-based models, temporal CNN-based model, and Transformer-based models. Furthermore, we explored transfer learning to leverage simulated data to improve the generalization of deep learning models on real-world observations. Our benchmark dataset and evaluation framework contribute to the development of more accurate and scalable AI-driven agroecosystem models, advancing our understanding of ecosystem-climate interactions.

