---
layout: default
title: T2S-Bench & Structure-of-Thought: Benchmarking and Prompting Comprehensive Text-to-Structure Reasoning
---

# T2S-Bench & Structure-of-Thought: Benchmarking and Prompting Comprehensive Text-to-Structure Reasoning
**arXiv**：[2603.03790v1](https://arxiv.org/abs/2603.03790) · [PDF](https://arxiv.org/pdf/2603.03790.pdf)  
**作者**：Qinsi Wang, Hancheng Ye, Jinhee Kim, Jinghan Ke, Yifei Wang, Martin Kuo, Zishan Shao, Dongting Li, Yueqian Lin, Ting Jiang, Chiyue Wei, Qi Qian, Wei Wen, Helen Li, Yiran Chen  

**一句话要点**：提出Structure-of-Thought提示技术与T2S-Bench基准，以提升大语言模型的文本到结构推理能力。

**关键词**：文本到结构推理, 提示技术, 基准评测, 大语言模型, 科学领域

## 3 点简述
- 核心问题：大语言模型能否通过显式构建文本结构来增强文本处理性能？
- 方法要点：引入SoT提示技术指导模型构建中间文本结构，并创建T2S-Bench基准评估模型能力。
- 实验或效果：SoT在Qwen2.5-7B-Instruct上平均提升5.7%，结合T2S-Bench微调后提升至8.6%。

## 摘要（原文）

> Think about how human handles complex reading tasks: marking key points, inferring their relationships, and structuring information to guide understanding and responses. Likewise, can a large language model benefit from text structure to enhance text-processing performance? To explore it, in this work, we first introduce Structure of Thought (SoT), a prompting technique that explicitly guides models to construct intermediate text structures, consistently boosting performance across eight tasks and three model families. Building upon this insight, we present T2S-Bench, the first benchmark designed to evaluate and improve text-to-structure capabilities of models. T2S-Bench includes 1.8K samples across 6 scientific domains and 32 structural types, rigorously constructed to ensure accuracy, fairness, and quality. Evaluation on 45 mainstream models reveals substantial improvement potential: the average accuracy on the multi-hop reasoning task is only 52.1%, and even the most advanced model achieves 58.1% node accuracy in end-to-end extraction. Furthermore, on Qwen2.5-7B-Instruct, SoT alone yields an average +5.7% improvement across eight diverse text-processing tasks, and fine-tuning on T2S-Bench further increases this gain to +8.6%. These results highlight the value of explicit text structuring and the complementary contributions of SoT and T2S-Bench. Dataset and eval code have been released at https://t2s-bench.github.io/T2S-Bench-Page/.

