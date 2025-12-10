---
layout: default
title: De novo generation of functional terpene synthases using TpsGPT
---

# De novo generation of functional terpene synthases using TpsGPT
**arXiv**：[2512.08772v1](https://arxiv.org/abs/2512.08772) · [PDF](https://arxiv.org/pdf/2512.08772.pdf)  
**作者**：Hamsini Ramanathan, Roman Bushuiev, Matouš Soldát, Jirí Kohout, Téo Hebra, Joshua David Smith, Josef Sivic, Tomáš Pluskal  

**一句话要点**：提出TpsGPT以解决萜烯合酶从头设计的成本与效率问题

**关键词**：蛋白质语言模型, 酶设计, 生成模型, 萜烯合酶, 从头设计, 实验验证

## 3 点简述
- 萜烯合酶设计依赖定向进化，过程昂贵且缓慢
- 基于ProtGPT2微调，构建生成模型TpsGPT，用于从头设计酶序列
- 通过多指标验证和实验，确认生成序列具有功能性活性

## 摘要（原文）

> Terpene synthases (TPS) are a key family of enzymes responsible for generating the diverse terpene scaffolds that underpin many natural products, including front-line anticancer drugs such as Taxol. However, de novo TPS design through directed evolution is costly and slow. We introduce TpsGPT, a generative model for scalable TPS protein design, built by fine-tuning the protein language model ProtGPT2 on 79k TPS sequences mined from UniProt. TpsGPT generated de novo enzyme candidates in silico and we evaluated them using multiple validation metrics, including EnzymeExplorer classification, ESMFold structural confidence (pLDDT), sequence diversity, CLEAN classification, InterPro domain detection, and Foldseek structure alignment. From an initial pool of 28k generated sequences, we identified seven putative TPS enzymes that satisfied all validation criteria. Experimental validation confirmed TPS enzymatic activity in at least two of these sequences. Our results show that fine-tuning of a protein language model on a carefully curated, enzyme-class-specific dataset, combined with rigorous filtering, can enable the de novo generation of functional, evolutionarily distant enzymes.

