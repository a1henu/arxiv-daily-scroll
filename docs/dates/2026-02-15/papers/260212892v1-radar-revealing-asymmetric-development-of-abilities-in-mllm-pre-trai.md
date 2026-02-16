---
layout: default
title: RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training
---

# RADAR: Revealing Asymmetric Development of Abilities in MLLM Pre-training
**arXiv**：[2602.12892v1](https://arxiv.org/abs/2602.12892) · [PDF](https://arxiv.org/pdf/2602.12892.pdf)  
**作者**：Yunshuang Nie, Bingqian Lin, Minzhe Niu, Kun Xiang, Jianhua Han, Guowei Huang, Xingyue Quan, Hang Xu, Bokui Chen, Xiaodan Liang  

**一句话要点**：提出RADAR框架以高效评估多模态大语言模型预训练中的能力不对称发展

**关键词**：多模态大语言模型, 预训练评估, 能力诊断, 软判别分数, 多模态混合基准, 零样本评估

## 3 点简述
- 当前缺乏高效评估框架，难以诊断MLLM预训练的性能瓶颈。
- RADAR包括软判别分数和新基准，无需微调即可量化感知与推理能力。
- 实验揭示预训练MLLM在数据量、模型大小和策略下的能力不对称发展。

## 摘要（原文）

> Pre-trained Multi-modal Large Language Models (MLLMs) provide a knowledge-rich foundation for post-training by leveraging their inherent perception and reasoning capabilities to solve complex tasks. However, the lack of an efficient evaluation framework impedes the diagnosis of their performance bottlenecks. Current evaluation primarily relies on testing after supervised fine-tuning, which introduces laborious additional training and autoregressive decoding costs. Meanwhile, common pre-training metrics cannot quantify a model's perception and reasoning abilities in a disentangled manner. Furthermore, existing evaluation benchmarks are typically limited in scale or misaligned with pre-training objectives. Thus, we propose RADAR, an efficient ability-centric evaluation framework for Revealing Asymmetric Development of Abilities in MLLM pRe-training. RADAR involves two key components: (1) Soft Discrimination Score, a novel metric for robustly tracking ability development without fine-tuning, based on quantifying nuanced gradations of the model preference for the correct answer over distractors; and (2) Multi-Modal Mixture Benchmark, a new 15K+ sample benchmark for comprehensively evaluating pre-trained MLLMs' perception and reasoning abilities in a 0-shot manner, where we unify authoritative benchmark datasets and carefully collect new datasets, extending the evaluation scope and addressing the critical gaps in current benchmarks. With RADAR, we comprehensively reveal the asymmetric development of perceptual and reasoning capabilities in pretrained MLLMs across diverse factors, including data volume, model size, and pretraining strategy. Our RADAR underscores the need for a decomposed perspective on pre-training ability bottlenecks, informing targeted interventions to advance MLLMs efficiently. Our code is publicly available at https://github.com/Nieysh/RADAR.

