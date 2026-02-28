---
layout: default
title: Efficient Dialect-Aware Modeling and Conditioning for Low-Resource Taiwanese Hakka Speech Processing
---

# Efficient Dialect-Aware Modeling and Conditioning for Low-Resource Taiwanese Hakka Speech Processing
**arXiv**：[2602.22522v1](https://arxiv.org/abs/2602.22522) · [PDF](https://arxiv.org/pdf/2602.22522.pdf)  
**作者**：An-Ci Peng, Kuan-Tang Huang, Tien-Hong Lo, Hung-Shin Lee, Hsin-Min Wang, Berlin Chen  

**一句话要点**：提出方言感知建模与参数高效预测网络，以解决低资源台湾客家话语音识别中的方言变异和双书写系统挑战。

**关键词**：方言感知建模, 低资源语音识别, 台湾客家话, 双书写系统ASR, 参数高效预测网络, RNN-T框架

## 3 点简述
- 核心问题：台湾客家话方言变异大且存在汉字和拼音双书写系统，传统ASR模型易混淆语言内容与方言风格。
- 方法要点：基于RNN-T框架，引入方言感知建模分离方言风格与语言内容，并采用参数高效预测网络联合建模汉字和拼音ASR。
- 实验或效果：在HAT语料库上，汉字和拼音ASR相对错误率分别降低57.00%和40.41%，首次系统研究方言变异影响并实现单模型联合处理。

## 摘要（原文）

> Taiwanese Hakka is a low-resource, endangered language that poses significant challenges for automatic speech recognition (ASR), including high dialectal variability and the presence of two distinct writing systems (Hanzi and Pinyin). Traditional ASR models often encounter difficulties in this context, as they tend to conflate essential linguistic content with dialect-specific variations across both phonological and lexical dimensions. To address these challenges, we propose a unified framework grounded in the Recurrent Neural Network Transducers (RNN-T). Central to our approach is the introduction of dialect-aware modeling strategies designed to disentangle dialectal "style" from linguistic "content", which enhances the model's capacity to learn robust and generalized representations. Additionally, the framework employs parameter-efficient prediction networks to concurrently model ASR (Hanzi and Pinyin). We demonstrate that these tasks create a powerful synergy, wherein the cross-script objective serves as a mutual regularizer to improve the primary ASR tasks. Experiments conducted on the HAT corpus reveal that our model achieves 57.00% and 40.41% relative error rate reduction on Hanzi and Pinyin ASR, respectively. To our knowledge, this is the first systematic investigation into the impact of Hakka dialectal variations on ASR and the first single model capable of jointly addressing these tasks.

