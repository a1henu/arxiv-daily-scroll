---
layout: default
title: Does Less Hallucination Mean Less Creativity? An Empirical Investigation in LLMs
---

# Does Less Hallucination Mean Less Creativity? An Empirical Investigation in LLMs
**arXiv**：[2512.11509v1](https://arxiv.org/abs/2512.11509) · [PDF](https://arxiv.org/pdf/2512.11509.pdf)  
**作者**：Mohor Banerjee, Nadya Yuki Wangsajaya, Syed Ali Redha Alsagoff, Min Sen Tan, Zachary Choy Kit Chun, Alvin Chan Guo Wei  

**一句话要点**：探究幻觉减少技术对LLMs创造力的影响，为科学应用提供方法选择指导

**关键词**：幻觉减少, 创造力评估, 大语言模型, 科学发现, 发散思维

## 3 点简述
- 核心问题：幻觉减少技术如何影响LLMs的创造力，尤其在科学发现中需平衡事实准确性与创造性
- 方法要点：评估CoVe、DoLa和RAG三种技术对LLaMA、Qwen、Mistral等模型在NeoCoder和CS4基准上的创造力影响
- 实验或效果：CoVe增强发散思维，DoLa抑制发散思维，RAG影响最小，提供方法选择依据

## 摘要（原文）

> Large Language Models (LLMs) exhibit remarkable capabilities in natural language understanding and reasoning, but suffer from hallucination: the generation of factually incorrect content. While numerous methods have been developed to reduce hallucinations, their impact on creative generations remains unexplored. This gap is particularly critical for AI-assisted scientific discovery, which requires both factual accuracy and creative hypothesis generation. We investigate how three hallucination-reduction techniques: Chain of Verification (CoVe), Decoding by Contrasting Layers (DoLa), and Retrieval-Augmented Generation (RAG), affect creativity in LLMs. Evaluating multiple model families (LLaMA, Qwen, Mistral) at varying scales (1B - 70B parameters) on two creativity benchmarks (NeoCoder and CS4), we find that these methods have opposing effects on divergent creativity. CoVe enhances divergent thinking, DoLa suppresses it, and RAG shows minimal impact. Our findings provide guidance for selecting appropriate hallucination-reduction methods in scientific applications, where the balance between factual accuracy and creative exploration is crucial.

