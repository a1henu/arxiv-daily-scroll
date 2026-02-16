---
layout: default
title: Reliable Thinking with Images
---

# Reliable Thinking with Images
**arXiv**：[2602.12916v1](https://arxiv.org/abs/2602.12916) · [PDF](https://arxiv.org/pdf/2602.12916.pdf)  
**作者**：Haobin Li, Yutong Yang, Yijie Lin, Dai Xiang, Mouxing Yang, Xi Peng  

**一句话要点**：提出RTWI方法以解决多模态大语言模型中图像思考的噪声问题

**关键词**：多模态大语言模型, 图像思考, 噪声问题, 可靠性评估, 鲁棒过滤, 投票模块

## 3 点简述
- 核心问题：图像思考中的噪声问题，即视觉线索挖掘和答案推理不完美，导致错误累积
- 方法要点：以文本为中心统一评估视觉线索和文本推理的可靠性，采用鲁棒过滤和投票模块
- 实验或效果：在七个基准测试中验证了RTWI对噪声问题的有效性

## 摘要（原文）

> As a multimodal extension of Chain-of-Thought (CoT), Thinking with Images (TWI) has recently emerged as a promising avenue to enhance the reasoning capability of Multi-modal Large Language Models (MLLMs), which generates interleaved CoT by incorporating visual cues into the textual reasoning process. However, the success of existing TWI methods heavily relies on the assumption that interleaved image-text CoTs are faultless, which is easily violated in real-world scenarios due to the complexity of multimodal understanding. In this paper, we reveal and study a highly-practical yet under-explored problem in TWI, termed Noisy Thinking (NT). Specifically, NT refers to the imperfect visual cues mining and answer reasoning process. As the saying goes, ``One mistake leads to another'', erroneous interleaved CoT would cause error accumulation, thus significantly degrading the performance of MLLMs. To solve the NT problem, we propose a novel method dubbed Reliable Thinking with Images (RTWI). In brief, RTWI estimates the reliability of visual cues and textual CoT in a unified text-centric manner and accordingly employs robust filtering and voting modules to prevent NT from contaminating the final answer. Extensive experiments on seven benchmarks verify the effectiveness of RTWI against NT.

