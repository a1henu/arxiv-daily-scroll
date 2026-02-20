---
layout: default
title: TimeOmni-VL: Unified Models for Time Series Understanding and Generation
---

# TimeOmni-VL: Unified Models for Time Series Understanding and Generation
**arXiv**：[2602.17149v1](https://arxiv.org/abs/2602.17149) · [PDF](https://arxiv.org/pdf/2602.17149.pdf)  
**作者**：Tong Guan, Sheng Pan, Johan Barthelemy, Zhao Li, Yujun Cai, Cesare Alippi, Ming Jin, Shirui Pan  

**一句话要点**：提出TimeOmni-VL框架，通过视觉中心方法统一时间序列理解与生成，解决现有模型分割问题。

**关键词**：时间序列理解, 时间序列生成, 多模态模型, 视觉中心框架, 保真映射, 理解引导生成

## 3 点简述
- 核心问题：时间序列建模存在生成与理解的分割，生成模型依赖表面模式匹配，理解模型难以输出高保真数值。
- 方法要点：引入保真双向映射（Bi-TSI）和理解引导生成，结合TSUMM-Suite数据集和校准思维链。
- 实验或效果：统一方法显著提升语义理解和数值精度，为多模态时间序列建模开辟新前沿。

## 摘要（原文）

> Recent time series modeling faces a sharp divide between numerical generation and semantic understanding, with research showing that generation models often rely on superficial pattern matching, while understanding-oriented models struggle with high-fidelity numerical output. Although unified multimodal models (UMMs) have bridged this gap in vision, their potential for time series remains untapped. We propose TimeOmni-VL, the first vision-centric framework that unifies time series understanding and generation through two key innovations: (1) Fidelity-preserving bidirectional mapping between time series and images (Bi-TSI), which advances Time Series-to-Image (TS2I) and Image-to-Time Series (I2TS) conversions to ensure near-lossless transformations. (2) Understanding-guided generation. We introduce TSUMM-Suite, a novel dataset consists of six understanding tasks rooted in time series analytics that are coupled with two generation tasks. With a calibrated Chain-of-Thought, TimeOmni-VL is the first to leverage time series understanding as an explicit control signal for high-fidelity generation. Experiments confirm that this unified approach significantly improves both semantic understanding and numerical precision, establishing a new frontier for multimodal time series modeling.

