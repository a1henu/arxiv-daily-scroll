---
layout: default
title: SQuTR: A Robustness Benchmark for Spoken Query to Text Retrieval under Acoustic Noise
---

# SQuTR: A Robustness Benchmark for Spoken Query to Text Retrieval under Acoustic Noise
**arXiv**：[2602.12783v1](https://arxiv.org/abs/2602.12783) · [PDF](https://arxiv.org/pdf/2602.12783.pdf)  
**作者**：Yuejie Li, Ke Yang, Yueying Hua, Berlin Chen, Jianhao Nie, Yueping He, Caixin Kang  

**一句话要点**：提出SQuTR基准以评估语音查询检索在复杂噪声下的鲁棒性

**关键词**：语音查询检索, 鲁棒性基准, 噪声合成, 检索系统评估, 多语言数据集

## 3 点简述
- 现有语音查询检索数据集在受限噪声条件下评估不足，无法反映真实复杂环境
- SQuTR整合多领域查询，使用真实语音和噪声合成大规模数据集，支持可控SNR评估
- 实验显示检索性能随噪声增加而下降，不同系统差异显著，鲁棒性仍是关键瓶颈

## 摘要（原文）

> Spoken query retrieval is an important interaction mode in modern information retrieval. However, existing evaluation datasets are often limited to simple queries under constrained noise conditions, making them inadequate for assessing the robustness of spoken query retrieval systems under complex acoustic perturbations. To address this limitation, we present SQuTR, a robustness benchmark for spoken query retrieval that includes a large-scale dataset and a unified evaluation protocol. SQuTR aggregates 37,317 unique queries from six commonly used English and Chinese text retrieval datasets, spanning multiple domains and diverse query types. We synthesize speech using voice profiles from 200 real speakers and mix 17 categories of real-world environmental noise under controlled SNR levels, enabling reproducible robustness evaluation from quiet to highly noisy conditions. Under the unified protocol, we conduct large-scale evaluations on representative cascaded and end-to-end retrieval systems. Experimental results show that retrieval performance decreases as noise increases, with substantially different drops across systems. Even large-scale retrieval models struggle under extreme noise, indicating that robustness remains a critical bottleneck. Overall, SQuTR provides a reproducible testbed for benchmarking and diagnostic analysis, and facilitates future research on robustness in spoken query to text retrieval.

