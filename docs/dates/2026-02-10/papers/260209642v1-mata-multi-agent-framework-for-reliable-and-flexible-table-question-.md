---
layout: default
title: MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering
---

# MATA: Multi-Agent Framework for Reliable and Flexible Table Question Answering
**arXiv**：[2602.09642v1](https://arxiv.org/abs/2602.09642) · [PDF](https://arxiv.org/pdf/2602.09642.pdf)  
**作者**：Sieun Hyeon, Jusang Oh, Sunghwan Steve Cho, Jaeyoung Do  

**一句话要点**：提出多智能体框架MATA以解决表格问答中的可靠性、可扩展性和效率问题。

**关键词**：表格问答, 多智能体框架, 推理路径优化, 效率提升, 开源工具

## 3 点简述
- 核心问题：大型语言模型在表格问答中面临可靠性、可扩展性和效率挑战，尤其在资源受限或隐私敏感环境中。
- 方法要点：MATA利用多智能体生成多样化推理路径，结合小型语言模型工具优化答案，并减少昂贵LLM调用以提升效率。
- 实验或效果：在多个基准测试和不同LLM上，MATA实现了最先进的准确性和高效推理，代码已开源。

## 摘要（原文）

> Recent advances in Large Language Models (LLMs) have significantly improved table understanding tasks such as Table Question Answering (TableQA), yet challenges remain in ensuring reliability, scalability, and efficiency, especially in resource-constrained or privacy-sensitive environments. In this paper, we introduce MATA, a multi-agent TableQA framework that leverages multiple complementary reasoning paths and a set of tools built with small language models. MATA generates candidate answers through diverse reasoning styles for a given table and question, then refines or selects the optimal answer with the help of these tools. Furthermore, it incorporates an algorithm designed to minimize expensive LLM agent calls, enhancing overall efficiency. MATA maintains strong performance with small, open-source models and adapts easily across various LLM types. Extensive experiments on two benchmarks of varying difficulty with ten different LLMs demonstrate that MATA achieves state-of-the-art accuracy and highly efficient reasoning while avoiding excessive LLM inference. Our results highlight that careful orchestration of multiple reasoning pathways yields scalable and reliable TableQA. The code is available at https://github.com/AIDAS-Lab/MATA.

