---
layout: default
title: Operationalising the Superficial Alignment Hypothesis via Task Complexity
---

# Operationalising the Superficial Alignment Hypothesis via Task Complexity
**arXiv**：[2602.15829v1](https://arxiv.org/abs/2602.15829) · [PDF](https://arxiv.org/pdf/2602.15829.pdf)  
**作者**：Tomás Vergara-Browne, Darshan Patil, Ivan Titov, Siva Reddy, Tiago Pimentel, Marius Mosbach  

**一句话要点**：提出任务复杂度指标以形式化浅层对齐假说，并验证预训练大幅降低任务复杂度

**关键词**：任务复杂度, 浅层对齐假说, 预训练模型, 后训练, 程序长度, 任务适应

## 3 点简述
- 核心问题：浅层对齐假说缺乏精确定义，导致支持论据分歧和重要批评
- 方法要点：定义任务复杂度为达到目标性能的最短程序长度，统一假说解释
- 实验或效果：在数学推理等任务中，预训练后复杂度降低数个数量级，适应仅需千字节信息

## 摘要（原文）

> The superficial alignment hypothesis (SAH) posits that large language models learn most of their knowledge during pre-training, and that post-training merely surfaces this knowledge. The SAH, however, lacks a precise definition, which has led to (i) different and seemingly orthogonal arguments supporting it, and (ii) important critiques to it. We propose a new metric called task complexity: the length of the shortest program that achieves a target performance on a task. In this framework, the SAH simply claims that pre-trained models drastically reduce the complexity of achieving high performance on many tasks. Our definition unifies prior arguments supporting the SAH, interpreting them as different strategies to find such short programs. Experimentally, we estimate the task complexity of mathematical reasoning, machine translation, and instruction following; we then show that these complexities can be remarkably low when conditioned on a pre-trained model. Further, we find that pre-training enables access to strong performances on our tasks, but it can require programs of gigabytes of length to access them. Post-training, on the other hand, collapses the complexity of reaching this same performance by several orders of magnitude. Overall, our results highlight that task adaptation often requires surprisingly little information -- often just a few kilobytes.

