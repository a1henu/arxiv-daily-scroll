---
layout: default
title: Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning
---

# Toward Culturally Aligned LLMs through Ontology-Guided Multi-Agent Reasoning
**arXiv**：[2601.21700v1](https://arxiv.org/abs/2601.21700) · [PDF](https://arxiv.org/pdf/2601.21700.pdf)  
**作者**：Wonduk Seo, Wonseok Choi, Junseo Koh, Juhyeon Lee, Hyunjin An, Minhyeong Yu, Jian Park, Qingshan Zhou, Seunghyun Lee, Yi Bu  

**一句话要点**：提出OG-MAR框架，通过本体引导的多智能体推理提升LLMs的文化对齐能力。

**关键词**：文化对齐, 本体构建, 多智能体推理, 世界价值观调查, LLM微调

## 3 点简述
- 核心问题：LLMs在文化敏感决策中常因训练数据偏差和缺乏结构化价值表示而失准。
- 方法要点：基于世界价值观调查构建全球文化本体，并利用多智能体进行推理和一致性合成。
- 实验或效果：在四个LLM骨干上，OG-MAR在区域社会调查基准中提高了文化对齐和鲁棒性。

## 摘要（原文）

> Large Language Models (LLMs) increasingly support culturally sensitive decision making, yet often exhibit misalignment due to skewed pretraining data and the absence of structured value representations. Existing methods can steer outputs, but often lack demographic grounding and treat values as independent, unstructured signals, reducing consistency and interpretability. We propose OG-MAR, an Ontology-Guided Multi-Agent Reasoning framework. OG-MAR summarizes respondent-specific values from the World Values Survey (WVS) and constructs a global cultural ontology by eliciting relations over a fixed taxonomy via competency questions. At inference time, it retrieves ontology-consistent relations and demographically similar profiles to instantiate multiple value-persona agents, whose outputs are synthesized by a judgment agent that enforces ontology consistency and demographic proximity. Experiments on regional social-survey benchmarks across four LLM backbones show that OG-MAR improves cultural alignment and robustness over competitive baselines, while producing more transparent reasoning traces.

