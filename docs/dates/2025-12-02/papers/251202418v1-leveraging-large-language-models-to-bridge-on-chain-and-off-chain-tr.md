---
layout: default
title: Leveraging Large Language Models to Bridge On-chain and Off-chain Transparency in Stablecoins
---

# Leveraging Large Language Models to Bridge On-chain and Off-chain Transparency in Stablecoins
**arXiv**：[2512.02418v1](https://arxiv.org/abs/2512.02418) · [PDF](https://arxiv.org/pdf/2512.02418.pdf)  
**作者**：Yuexin Xiang, Yuchen Lei, SM Mahir Shazeed Rish, Yuanzhe Zhang, Qin Wang, Tsz Hon Yuen, Jiangshan Yu  

**一句话要点**：提出基于大语言模型的自动化框架，以弥合稳定币链上与链下透明度之间的鸿沟。

**关键词**：稳定币透明度, 大语言模型, 链上链下对齐, 自动化审计, 去中心化金融

## 3 点简述
- 核心问题：稳定币透明度分散于可验证的链上数据和未结构化的链下披露文本，两者缺乏连接。
- 方法要点：利用大语言模型通过文档解析和语义对齐，整合链上发行数据与链下披露声明，提取关键指标并映射。
- 实验或效果：框架揭示披露数据与可验证数据间的系统性差距，增强跨模态透明度，支持去中心化金融的自动化审计。

## 摘要（原文）

> Stablecoins such as USDT and USDC aspire to peg stability by coupling issuance controls with reserve attestations. In practice, however, the transparency is split across two worlds: verifiable on-chain traces and off-chain disclosures locked in unstructured text that are unconnected. We introduce a large language model (LLM)-based automated framework that bridges these two dimensions by aligning on-chain issuance data with off-chain disclosure statements. First, we propose an integrative framework using LLMs to capture and analyze on- and off-chain data through document parsing and semantic alignment, extracting key financial indicators from issuer attestations and mapping them to corresponding on-chain metrics. Second, we integrate multi-chain issuance records and disclosure documents within a model context protocol (MCP) framework that standardizes LLMs access to both quantitative market data and qualitative disclosure narratives. This framework enables unified retrieval and contextual alignment across heterogeneous stablecoin information sources and facilitates consistent analysis. Third, we demonstrate the capability of LLMs to operate across heterogeneous data modalities in blockchain analytics, quantifying discrepancies between reported and observed circulation and examining their implications for cross-chain transparency and price dynamics. Our findings reveal systematic gaps between disclosed and verifiable data, showing that LLM-assisted analysis enhances cross-modal transparency and supports automated, data-driven auditing in decentralized finance (DeFi).

