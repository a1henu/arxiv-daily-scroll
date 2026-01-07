---
layout: default
title: Multi-channel multi-speaker transformer for speech recognition
---

# Multi-channel multi-speaker transformer for speech recognition
**arXiv**：[2601.02688v1](https://arxiv.org/abs/2601.02688) · [PDF](https://arxiv.org/pdf/2601.02688.pdf)  
**作者**：Guo Yifan, Tian Yao, Suo Hongbin, Wan Yulong  

**一句话要点**：提出多通道多说话人Transformer，用于远场多说话人语音识别，提升分离与识别性能。

**关键词**：远场语音识别, 多说话人分离, 多通道Transformer, 端到端系统, 词错误率降低

## 3 点简述
- 核心问题：远场多说话人语音识别中，说话人干扰导致高维声学特征编码困难。
- 方法要点：基于多通道Transformer，扩展为多说话人模型，增强对混合音频的分离能力。
- 实验或效果：在SMS-WSJ基准上，相对词错误率降低优于多个基线系统，最高达52.2%。

## 摘要（原文）

> With the development of teleconferencing and in-vehicle voice assistants, far-field multi-speaker speech recognition has become a hot research topic. Recently, a multi-channel transformer (MCT) has been proposed, which demonstrates the ability of the transformer to model far-field acoustic environments. However, MCT cannot encode high-dimensional acoustic features for each speaker from mixed input audio because of the interference between speakers. Based on these, we propose the multi-channel multi-speaker transformer (M2Former) for far-field multi-speaker ASR in this paper. Experiments on the SMS-WSJ benchmark show that the M2Former outperforms the neural beamformer, MCT, dual-path RNN with transform-average-concatenate and multi-channel deep clustering based end-to-end systems by 9.2%, 14.3%, 24.9%, and 52.2% respectively, in terms of relative word error rate reduction.

