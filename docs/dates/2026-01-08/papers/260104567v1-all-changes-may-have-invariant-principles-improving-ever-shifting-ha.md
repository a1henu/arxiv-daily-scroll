---
layout: default
title: All Changes May Have Invariant Principles: Improving Ever-Shifting Harmful Meme Detection via Design Concept Reproduction
---

# All Changes May Have Invariant Principles: Improving Ever-Shifting Harmful Meme Detection via Design Concept Reproduction
**arXiv**：[2601.04567v1](https://arxiv.org/abs/2601.04567) · [PDF](https://arxiv.org/pdf/2601.04567.pdf)  
**作者**：Ziyou Jiang, Mingyang Li, Junjie Wang, Yuekai Huang, Jie Huang, Zhiyuan Chang, Zhaoyang Li, Qing Wang  

**一句话要点**：提出RepMD方法，通过设计概念复现改进不断演变的网络有害梗图检测

**关键词**：有害梗图检测, 设计概念复现, 多模态大语言模型, 攻击树, 类型演变, 时效演变

## 3 点简述
- 核心问题：网络有害梗图类型和时效性不断演变，导致检测困难
- 方法要点：基于攻击树定义设计概念图，复现历史梗图设计步骤以提取不变原则
- 实验或效果：在检测准确率达81.1%，对类型和时效演变梗图泛化性良好，提升人工发现效率

## 摘要（原文）

> Harmful memes are ever-shifting in the Internet communities, which are difficult to analyze due to their type-shifting and temporal-evolving nature. Although these memes are shifting, we find that different memes may share invariant principles, i.e., the underlying design concept of malicious users, which can help us analyze why these memes are harmful. In this paper, we propose RepMD, an ever-shifting harmful meme detection method based on the design concept reproduction. We first refer to the attack tree to define the Design Concept Graph (DCG), which describes steps that people may take to design a harmful meme. Then, we derive the DCG from historical memes with design step reproduction and graph pruning. Finally, we use DCG to guide the Multimodal Large Language Model (MLLM) to detect harmful memes. The evaluation results show that RepMD achieves the highest accuracy with 81.1% and has slight accuracy decreases when generalized to type-shifting and temporal-evolving memes. Human evaluation shows that RepMD can improve the efficiency of human discovery on harmful memes, with 15$\sim$30 seconds per meme.

