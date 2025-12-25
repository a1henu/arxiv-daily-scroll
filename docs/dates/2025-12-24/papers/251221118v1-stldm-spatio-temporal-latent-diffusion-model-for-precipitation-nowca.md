---
layout: default
title: STLDM: Spatio-Temporal Latent Diffusion Model for Precipitation Nowcasting
---

# STLDM: Spatio-Temporal Latent Diffusion Model for Precipitation Nowcasting
**arXiv**：[2512.21118v1](https://arxiv.org/abs/2512.21118) · [PDF](https://arxiv.org/pdf/2512.21118.pdf)  
**作者**：Shi Quan Foo, Chi-Ho Wong, Zhihan Gao, Dit-Yan Yeung, Ka-Hing Wong, Wai-Kin Wong  

**一句话要点**：提出STLDM扩散模型，通过两阶段架构解决降水临近预报的模糊与精度问题。

**关键词**：降水临近预报, 扩散模型, 时空预测, 变分自编码器, 条件网络

## 3 点简述
- 降水临近预报面临复杂随机性，现有方法存在模糊预测或精度不足的挑战。
- STLDM结合变分自编码器和条件网络，分两阶段进行确定性预测与扩散增强。
- 在多个雷达数据集上验证，STLDM实现性能提升并提高推理效率。

## 摘要（原文）

> Precipitation nowcasting is a critical spatio-temporal prediction task for society to prevent severe damage owing to extreme weather events. Despite the advances in this field, the complex and stochastic nature of this task still poses challenges to existing approaches. Specifically, deterministic models tend to produce blurry predictions while generative models often struggle with poor accuracy. In this paper, we present a simple yet effective model architecture termed STLDM, a diffusion-based model that learns the latent representation from end to end alongside both the Variational Autoencoder and the conditioning network. STLDM decomposes this task into two stages: a deterministic forecasting stage handled by the conditioning network, and an enhancement stage performed by the latent diffusion model. Experimental results on multiple radar datasets demonstrate that STLDM achieves superior performance compared to the state of the art, while also improving inference efficiency. The code is available in https://github.com/sqfoo/stldm_official.

