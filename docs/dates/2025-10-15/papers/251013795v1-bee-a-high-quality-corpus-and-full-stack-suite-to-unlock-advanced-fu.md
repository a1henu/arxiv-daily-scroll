---
layout: default
title: Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs
---

# Bee: A High-Quality Corpus and Full-Stack Suite to Unlock Advanced Fully Open MLLMs
**arXiv**：[2510.13795v1](https://arxiv.org/abs/2510.13795) · [PDF](https://arxiv.org/pdf/2510.13795.pdf)  
**作者**：Yi Zhang, Bolin Ni, Xin-Sheng Chen, Heng-Rui Zhang, Yongming Rao, Houwen Peng, Qinglin Lu, Han Hu, Meng-Hao Guo, Shi-Min Hu  

**一句话要点**：提出高质量数据集与全栈工具套件以提升全开放多模态大语言模型性能

**关键词**：多模态大语言模型, 监督微调数据集, 链式思维增强, 数据清洗管道, 全开放模型训练, 模型性能评估

## 3 点简述
- 全开放MLLMs性能落后，主要因SFT数据质量差，缺乏复杂推理数据如CoT。
- 引入Honey-Data-15M数据集，经多轮清洗和双级CoT增强，提升数据质量。
- 训练Bee-8B模型，实验显示其性能达到SOTA，可与半开放模型竞争。

## 摘要（原文）

> Fully open multimodal large language models (MLLMs) currently lag behind
> proprietary counterparts, primarily due to a significant gap in data quality
> for supervised fine-tuning (SFT). Existing open-source datasets are often
> plagued by widespread noise and a critical deficit in complex reasoning data,
> such as Chain-of-Thought (CoT), which hinders the development of advanced model
> capabilities. Addressing these challenges, our work makes three primary
> contributions. First, we introduce Honey-Data-15M, a new SFT dataset comprising
> approximately 15 million QA pairs, processed through multiple cleaning
> techniques and enhanced with a novel dual-level (short and long) CoT enrichment
> strategy. Second, we introduce HoneyPipe, the data curation pipeline, and its
> underlying framework DataStudio, providing the community with a transparent and
> adaptable methodology for data curation that moves beyond static dataset
> releases. Finally, to validate our dataset and pipeline, we train Bee-8B, an 8B
> model on Honey-Data-15M. Experiments show that Bee-8B establishes a new
> state-of-the-art (SOTA) for fully open MLLMs, achieving performance that is
> competitive with, and in some cases surpasses, recent semi-open models such as
> InternVL3.5-8B. Our work delivers to the community a suite of foundational
> resources, including: the Honey-Data-15M corpus; the full-stack suite
> comprising HoneyPipe and DataStudio; training recipes; an evaluation harness;
> and the model weights. This effort demonstrates that a principled focus on data
> quality is a key pathway to developing fully open MLLMs that are highly
> competitive with their semi-open counterparts.

