---
layout: default
title: TerraCodec: Compressing Earth Observations
---

# TerraCodec: Compressing Earth Observations
**arXiv**：[2510.12670v1](https://arxiv.org/abs/2510.12670) · [PDF](https://arxiv.org/pdf/2510.12670.pdf)  
**作者**：Julen Costa-Watanabe, Isabelle Wittmann, Benedikt Blumenstiel, Konrad Schindler  

**一句话要点**：提出TerraCodec以压缩地球观测数据，提升存储与传输效率

**关键词**：地球观测压缩, 多光谱图像, 时序Transformer, 潜在重打包, 零样本修复

## 3 点简述
- 地球观测卫星产生海量多光谱图像时间序列，存储与传输面临挑战
- 开发图像和时序Transformer模型，利用时间依赖性和潜在重打包实现灵活率失真
- 在Sentinel-2数据上优于经典编解码器，压缩比提升3-10倍，并支持零样本云修复

## 摘要（原文）

> Earth observation (EO) satellites produce massive streams of multispectral
> image time series, posing pressing challenges for storage and transmission.
> Yet, learned EO compression remains fragmented, lacking publicly available
> pretrained models and misaligned with advances in compression for natural
> imagery. Image codecs overlook temporal redundancy, while video codecs rely on
> motion priors that fail to capture the radiometric evolution of largely static
> scenes. We introduce TerraCodec (TEC), a family of learned codecs tailored to
> EO. TEC includes efficient image-based variants adapted to multispectral
> inputs, as well as a Temporal Transformer model (TEC-TT) that leverages
> dependencies across time. To overcome the fixed-rate setting of today's neural
> codecs, we present Latent Repacking, a novel method for training flexible-rate
> transformer models that operate on varying rate-distortion settings. Trained on
> Sentinel-2 data, TerraCodec outperforms classical codecs, achieving 3-10x
> stronger compression at equivalent image quality. Beyond compression, TEC-TT
> enables zero-shot cloud inpainting, surpassing state-of-the-art methods on the
> AllClear benchmark. Our results establish bespoke, learned compression
> algorithms as a promising direction for Earth observation. Code and model
> weights will be released under a permissive license.

