---
layout: default
title: Toward Graph-Tokenizing Large Language Models with Reconstructive Graph Instruction Tuning
---

# Toward Graph-Tokenizing Large Language Models with Reconstructive Graph Instruction Tuning
**arXiv**：[2603.01385v1](https://arxiv.org/abs/2603.01385) · [PDF](https://arxiv.org/pdf/2603.01385.pdf)  
**作者**：Zhongjian Zhang, Xiao Wang, Mengmei Zhang, Jiarui Tan, Chuan Shi  

**一句话要点**：提出RGLM以解决图-语言对齐中的文本主导偏差问题

**关键词**：图-语言对齐, 重构指令调优, 图-标记化大语言模型, 信息论分析, 图监督

## 3 点简述
- 现有图-标记化大语言模型仅依赖文本监督，导致图信息利用不足
- 通过重构图信息引入显式图监督，提升图-语言对齐效果
- 在多个基准和任务场景中验证了RGLM的有效性

## 摘要（原文）

> The remarkable success of large language models (LLMs) has motivated researchers to adapt them as universal predictors for various graph-related tasks, with the ultimate goal of developing a graph foundation model that generalizes diverse scenarios. The key challenge is to align graph data with language spaces so that LLMs can better comprehend graphs. As a popular paradigm, Graph-Tokenizing LLMs (GTokenLLMs) encode complex structures and lengthy texts into a graph token sequence, and then align them with text tokens via language instructions tuning. Despite their initial success, our information-theoretic analysis reveals that existing GTokenLLMs rely solely on text supervision from language instructions, which achieve only implicit graph-text alignment, resulting in a text-dominant bias that underutilizes graph context. To overcome this limitation, we first prove that the alignment objective is upper-bounded by the mutual information between the input graphs and their hidden representations in the LLM, which motivates us to improve this upper bound to achieve better alignment. To this end, we further propose a reconstructive graph instruction tuning pipeline, RGLM. Our key idea is to reconstruct the graph information from the LLM's graph token outputs, explicitly incorporating graph supervision to constrain the alignment process. Technically, we embody RGLM by exploring three distinct variants from two complementary perspectives: RGLM-Decoder from the input space; RGLM-Similarizer and RGLM-Denoiser from the latent space. Additionally, we theoretically analyze the alignment effectiveness of each variant. Extensive experiments on various benchmarks and task scenarios validate the effectiveness of the proposed RGLM, paving the way for new directions in GTokenLLMs' alignment research.

