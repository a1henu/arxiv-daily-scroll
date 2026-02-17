---
layout: default
title: Unlocking Reasoning Capability on Machine Translation in Large Language Models
---

# Unlocking Reasoning Capability on Machine Translation in Large Language Models
**arXiv**：[2602.14763v1](https://arxiv.org/abs/2602.14763) · [PDF](https://arxiv.org/pdf/2602.14763.pdf)  
**作者**：Sara Rajaee, Sebastian Vincent, Alexandre Berard, Marzieh Fadaee, Kelly Marchisio, Tom Kocmi  

**一句话要点**：提出结构化推理框架以提升大语言模型在机器翻译中的性能

**关键词**：机器翻译, 大语言模型, 结构化推理, 推理轨迹, 翻译质量, 后训练

## 3 点简述
- 发现推理导向大语言模型在机器翻译中启用显式推理会降低翻译质量
- 分析显示机器翻译推理轨迹高度线性，缺乏修订和探索替代翻译
- 提出多步骤草稿、充分性精炼、流畅性改进和选择性迭代修订的结构化推理框架，实验显示显著改进

## 摘要（原文）

> Reasoning-oriented large language models (RLMs) achieve strong gains on tasks such as mathematics and coding by generating explicit intermediate reasoning. However, their impact on machine translation (MT) remains underexplored. We systematically evaluate several open- and closed-weights RLMs on the WMT24++ benchmark and find that enabling explicit reasoning consistently degrades translation quality across languages and models. Analysis reveals that MT reasoning traces are highly linear, lacking revision, self-correction and exploration of alternative translations, which limits their usefulness. Furthermore, injecting higher-quality reasoning traces from stronger models does not reliably improve weaker models' performance. To address this mismatch, we propose a structured reasoning framework tailored to translation, based on multi-step drafting, adequacy refinement, fluency improvement, and selective iterative revision. We curate a synthetic dataset of dynamic structured reasoning traces and post-train a large reasoning model on this data. Experiments show significant improvements over standard translation fine-tuning and injected generic reasoning baselines. Our findings demonstrate that reasoning must be task-structured to benefit MT.

