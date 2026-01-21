---
layout: default
title: Diffusion In Diffusion: Breaking the Autoregressive Bottleneck in Block Diffusion Models
---

# Diffusion In Diffusion: Breaking the Autoregressive Bottleneck in Block Diffusion Models
**arXiv**：[2601.13599v1](https://arxiv.org/abs/2601.13599) · [PDF](https://arxiv.org/pdf/2601.13599.pdf)  
**作者**：Linrui Ma, Yufei Cui, Kai Han, Yunhe Wang  

**一句话要点**：提出Diffusion in Diffusion框架以解决块扩散模型中的不可逆性和短视问题

**关键词**：块扩散模型, 扩散模型, 语言模型, 生成模型, 半自回归模型

## 3 点简述
- 块扩散模型存在严格单向块依赖，导致不可逆性和全局规划能力缺失
- 采用草案-精炼框架，先小块快速生成草案，再全局双向扩散精炼
- 在OpenWebText数据集上，仅用26%微调预算将生成困惑度从25.7降至21.9

## 摘要（原文）

> Block diffusion language models, operating as semi-autoregressive paradigms, combine the strengths of both autoregressive and diffusion paradigms. However, their strict unidirectional block dependencies introduce irreversibility and sacrifice the global planning capabilities for which diffusion models are renowned. In order to address these issues, we propose Diffusion in Diffusion, a draft-then-refine framework designed to overcome the irreversibility and myopia problems inherent in block diffusion models. Our approach first employs block diffusion to generate rapid drafts using small blocks, then refines these drafts through global bidirectional diffusion with a larger bidirectional receptive field. We utilise snapshot confidence remasking to identify the most critical tokens that require modification, and apply mix-scale training to expand the block diffusion model's global capabilities. Empirical results demonstrate that our approach sets a new benchmark for discrete diffusion models on the OpenWebText dataset. Using just 26% of the fine-tuning budget of baseline models, we reduce generative perplexity from 25.7 to 21.9, significantly narrowing the performance gap with autoregressive models.

