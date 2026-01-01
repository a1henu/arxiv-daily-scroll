---
layout: default
title: SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM System
---

# SynRAG: A Large Language Model Framework for Executable Query Generation in Heterogeneous SIEM System
**arXiv**：[2512.24571v1](https://arxiv.org/abs/2512.24571) · [PDF](https://arxiv.org/pdf/2512.24571.pdf)  
**作者**：Md Hasan Saju, Austin Page, Akramul Azim, Jeff Gardiner, Farzaneh Abazari, Frank Eargle  

**一句话要点**：提出SynRAG框架以解决异构SIEM系统中跨平台查询生成难题

**关键词**：SIEM系统, 查询生成, 威胁检测, 事件调查, 大语言模型, 跨平台兼容性

## 3 点简述
- 核心问题：SIEM平台多样性导致分析师需手动编写多平台查询，增加培训与人力成本。
- 方法要点：基于平台无关规范，自动生成针对Qradar、SecOps等系统的威胁检测或事件调查查询。
- 实验或效果：相比GPT、Llama等先进模型，在Qradar和SecOps上生成查询效果显著更优。

## 摘要（原文）

> Security Information and Event Management (SIEM) systems are essential for large enterprises to monitor their IT infrastructure by ingesting and analyzing millions of logs and events daily. Security Operations Center (SOC) analysts are tasked with monitoring and analyzing this vast data to identify potential threats and take preventive actions to protect enterprise assets. However, the diversity among SIEM platforms, such as Palo Alto Networks Qradar, Google SecOps, Splunk, Microsoft Sentinel and the Elastic Stack, poses significant challenges. As these systems differ in attributes, architecture, and query languages, making it difficult for analysts to effectively monitor multiple platforms without undergoing extensive training or forcing enterprises to expand their workforce. To address this issue, we introduce SynRAG, a unified framework that automatically generates threat detection or incident investigation queries for multiple SIEM platforms from a platform-agnostic specification. SynRAG can generate platformspecific queries from a single high-level specification written by analysts. Without SynRAG, analysts would need to manually write separate queries for each SIEM platform, since query languages vary significantly across systems. This framework enables seamless threat detection and incident investigation across heterogeneous SIEM environments, reducing the need for specialized training and manual query translation. We evaluate SynRAG against state-of-the-art language models, including GPT, Llama, DeepSeek, Gemma, and Claude, using Qradar and SecOps as representative SIEM systems. Our results demonstrate that SynRAG generates significantly better queries for crossSIEM threat detection and incident investigation compared to the state-of-the-art base models.

