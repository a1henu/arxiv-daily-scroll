---
layout: default
title: D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation
---

# D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation
**arXiv**：[2603.01780v1](https://arxiv.org/abs/2603.01780) · [PDF](https://arxiv.org/pdf/2603.01780.pdf)  
**作者**：Zhao Yang, Hengchang Liu, Chuan Cao, Bing Su  

**一句话要点**：提出D3LM离散DNA扩散语言模型，统一双向DNA理解与生成能力。

**关键词**：DNA基础模型, 扩散语言模型, 双向表示学习, DNA序列生成, 掩码扩散训练, 调控元件生成

## 3 点简述
- 早期DNA基础模型缺乏生成能力，自回归模型双向建模不足。
- D3LM采用NT v2架构，通过掩码扩散训练实现双向表示学习与生成。
- 在理解任务上优于NT v2，生成任务SFID接近真实DNA，显著超越自回归模型。

## 摘要（原文）

> Early DNA foundation models adopted BERT-style training, achieving good performance on DNA understanding tasks but lacking generative capabilities. Recent autoregressive models enable DNA generation, but employ left-to-right causal modeling that is suboptimal for DNA where regulatory relationships are inherently bidirectional. We present D3LM (\textbf{D}iscrete \textbf{D}NA \textbf{D}iffusion \textbf{L}anguage \textbf{M}odel), which unifies bidirectional representation learning and DNA generation through masked diffusion. D3LM directly adopts the Nucleotide Transformer (NT) v2 architecture but reformulates the training objective as masked diffusion in discrete DNA space, enabling both bidirectional understanding and generation capabilities within a single model. Compared to NT v2 of the same size, D3LM achieves improved performance on understanding tasks. Notably, on regulatory element generation, D3LM achieves an SFID of 10.92, closely approaching real DNA sequences (7.85) and substantially outperforming the previous best result of 29.16 from autoregressive models. Our work suggests diffusion language models as a promising paradigm for unified DNA foundation models. We further present the first systematic study of masked diffusion models in the DNA domain, investigating practical design choices such as tokenization schemes and sampling strategies, thereby providing empirical insights and a solid foundation for future research. D3LM has been released at https://huggingface.co/collections/Hengchang-Liu/d3lm.

