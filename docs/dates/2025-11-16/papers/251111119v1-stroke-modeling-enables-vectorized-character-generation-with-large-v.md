---
layout: default
title: Stroke Modeling Enables Vectorized Character Generation with Large Vectorized Glyph Model
---

# Stroke Modeling Enables Vectorized Character Generation with Large Vectorized Glyph Model
**arXiv**：[2511.11119v1](https://arxiv.org/abs/2511.11119) · [PDF](https://arxiv.org/pdf/2511.11119.pdf)  
**作者**：Xinyue Zhang, Haolong Li, Jiawei Ma, Chen Ye  

**一句话要点**：提出大型向量化字形模型，通过笔画建模实现向量化字符生成

**关键词**：向量化字形生成, 笔画建模, 大语言模型微调, SVG数据集, 字符生成

## 3 点简述
- 核心问题：向量化字形在设计中需高效生成，传统方法难以处理复杂笔画序列
- 方法要点：基于笔画嵌入，微调大语言模型预测下一笔画，生成完整字符
- 实验或效果：模型在数据规模上展现扩展性，生成结果经专家验证有效

## 摘要（原文）

> Vectorized glyphs are widely used in poster design, network animation, art display, and various other fields due to their scalability and flexibility. In typography, they are often seen as special sequences composed of ordered strokes. This concept extends to the token sequence prediction abilities of large language models (LLMs), enabling vectorized character generation through stroke modeling. In this paper, we propose a novel Large Vectorized Glyph Model (LVGM) designed to generate vectorized Chinese glyphs by predicting the next stroke. Initially, we encode strokes into discrete latent variables called stroke embeddings. Subsequently, we train our LVGM via fine-tuning DeepSeek LLM by predicting the next stroke embedding. With limited strokes given, it can generate complete characters, semantically elegant words, and even unseen verses in vectorized form. Moreover, we release a new large-scale Chinese SVG dataset containing 907,267 samples based on strokes for dynamically vectorized glyph generation. Experimental results show that our model has scaling behaviors on data scales. Our generated vectorized glyphs have been validated by experts and relevant individuals.

