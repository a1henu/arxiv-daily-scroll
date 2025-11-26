---
layout: default
title: Latent Collaboration in Multi-Agent Systems
---

# Latent Collaboration in Multi-Agent Systems
**arXiv**：[2511.20639v1](https://arxiv.org/abs/2511.20639) · [PDF](https://arxiv.org/pdf/2511.20639.pdf)  
**作者**：Jiaru Zou, Xiyuan Yang, Ruizhong Qiu, Gaotang Li, Katherine Tieu, Pan Lu, Ke Shen, Hanghang Tong, Yejin Choi, Jingrui He, James Zou, Mengdi Wang, Ling Yang  

**一句话要点**：提出LatentMAS框架，实现多智能体在潜在空间直接协作，提升推理效率与质量。

**关键词**：多智能体系统, 潜在空间协作, 大语言模型, 推理效率, 无损信息交换

## 3 点简述
- 现有LLM多智能体系统依赖文本中介，导致效率低下和信息损失。
- LatentMAS通过潜在工作内存实现无损信息交换，无需训练即可协作。
- 实验显示在多个基准上准确率提升，输出令牌减少，推理速度加快。

## 摘要（原文）

> Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings. A shared latent working memory then preserves and transfers each agent's internal representations, ensuring lossless information exchange. We provide theoretical analyses establishing that LatentMAS attains higher expressiveness and lossless information preservation with substantially lower complexity than vanilla text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS consistently outperforms strong single-model and text-based MAS baselines, achieving up to 14.6% higher accuracy, reducing output token usage by 70.8%-83.7%, and providing 4x-4.3x faster end-to-end inference. These results demonstrate that our new latent collaboration framework enhances system-level reasoning quality while offering substantial efficiency gains without any additional training. Code and data are fully open-sourced at https://github.com/Gen-Verse/LatentMAS.

