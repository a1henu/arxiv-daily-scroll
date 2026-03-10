---
layout: default
title: Gradually Excavating External Knowledge for Implicit Complex Question Answering
---

# Gradually Excavating External Knowledge for Implicit Complex Question Answering
**arXiv**：[2603.08148v1](https://arxiv.org/abs/2603.08148) · [PDF](https://arxiv.org/pdf/2603.08148.pdf)  
**作者**：Chang Liu, Xiaoguang Li, Lifeng Shang, Xin Jiang, Qun Liu, Edmund Y. Lam, Ngai Wong  

**一句话要点**：提出渐进知识挖掘框架以解决开放域隐式复杂问答问题

**关键词**：开放域问答, 知识挖掘, 渐进推理, 隐式问题, 外部知识集成, LLMs应用

## 3 点简述
- 核心问题：LLMs在开放域隐式问答中面临知识覆盖不足和一次性生成限制
- 方法要点：通过迭代查询外部知识和逻辑推理逐步构建答案
- 实验或效果：在StrategyQA数据集上以较少参数实现78.17%准确率

## 摘要（原文）

> Recently, large language models (LLMs) have gained much attention for the emergence of human-comparable capabilities and huge potential. However, for open-domain implicit question-answering problems, LLMs may not be the ultimate solution due to the reasons of: 1) uncovered or out-of-date domain knowledge, 2) one-shot generation and hence restricted comprehensiveness. To this end, this work proposes a gradual knowledge excavation framework for open-domain complex question answering, where LLMs iteratively and actively acquire external information, and then reason based on acquired historical knowledge. Specifically, during each step of the solving process, the model selects an action to execute, such as querying external knowledge or performing a single logical reasoning step, to gradually progress toward a final answer. Our method can effectively leverage plug-and-play external knowledge and dynamically adjust the strategy for solving complex questions. Evaluated on the StrategyQA dataset, our method achieves 78.17% accuracy with less than 6% parameters of its competitors, setting new SOTA for ~10B-scale LLMs.

