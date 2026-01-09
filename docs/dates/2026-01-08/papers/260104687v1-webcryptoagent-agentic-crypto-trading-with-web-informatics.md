---
layout: default
title: WebCryptoAgent: Agentic Crypto Trading with Web Informatics
---

# WebCryptoAgent: Agentic Crypto Trading with Web Informatics
**arXiv**：[2601.04687v1](https://arxiv.org/abs/2601.04687) · [PDF](https://arxiv.org/pdf/2601.04687.pdf)  
**作者**：Ali Kurban, Wei Luo, Liangyu Zuo, Zeyu Zhang, Renda Han, Zhaolu Kang, Hao Tang  

**一句话要点**：提出WebCryptoAgent框架，通过多模态代理和分离控制架构解决加密货币交易中网络信息整合与实时风险管理的挑战。

**关键词**：加密货币交易, 多模态代理, 实时风险管理, 网络信息整合, 市场微观结构

## 3 点简述
- 核心问题：加密货币交易需整合多源网络信息和市场信号，但现有系统难以在噪声中稳健决策并应对秒级价格冲击。
- 方法要点：设计模态特定代理生成统一证据文档，并分离战略推理与实时风险模型以实现快速干预。
- 实验或效果：在真实市场实验中，该框架提升了交易稳定性、减少虚假活动并增强尾部风险处理能力。

## 摘要（原文）

> Cryptocurrency trading increasingly depends on timely integration of heterogeneous web information and market microstructure signals to support short-horizon decision making under extreme volatility. However, existing trading systems struggle to jointly reason over noisy multi-source web evidence while maintaining robustness to rapid price shocks at sub-second timescales. The first challenge lies in synthesizing unstructured web content, social sentiment, and structured OHLCV signals into coherent and interpretable trading decisions without amplifying spurious correlations, while the second challenge concerns risk control, as slow deliberative reasoning pipelines are ill-suited for handling abrupt market shocks that require immediate defensive responses. To address these challenges, we propose WebCryptoAgent, an agentic trading framework that decomposes web-informed decision making into modality-specific agents and consolidates their outputs into a unified evidence document for confidence-calibrated reasoning. We further introduce a decoupled control architecture that separates strategic hourly reasoning from a real-time second-level risk model, enabling fast shock detection and protective intervention independent of the trading loop. Extensive experiments on real-world cryptocurrency markets demonstrate that WebCryptoAgent improves trading stability, reduces spurious activity, and enhances tail-risk handling compared to existing baselines. Code will be available at https://github.com/AIGeeksGroup/WebCryptoAgent.

