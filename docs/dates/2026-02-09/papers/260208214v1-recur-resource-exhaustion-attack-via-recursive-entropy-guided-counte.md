---
layout: default
title: RECUR: Resource Exhaustion Attack via Recursive-Entropy Guided Counterfactual Utilization and Reflection
---

# RECUR: Resource Exhaustion Attack via Recursive-Entropy Guided Counterfactual Utilization and Reflection
**arXiv**：[2602.08214v1](https://arxiv.org/abs/2602.08214) · [PDF](https://arxiv.org/pdf/2602.08214.pdf)  
**作者**：Ziwei Wang, Yuanhe Zhang, Jing Chen, Zhenhong Zhou, Ruichao Liang, Ruiying Du, Ju Jia, Cong Wu, Yang Liu  

**一句话要点**：提出RECUR攻击方法，通过递归熵引导的反事实利用与反思，揭示大型推理模型的资源耗尽漏洞。

**关键词**：大型推理模型, 资源耗尽攻击, 递归熵, 反事实利用, 反思过程, 推理安全

## 3 点简述
- 核心问题：大型推理模型的反思过程可能导致过度反思，消耗过多计算资源，但相关安全风险研究不足。
- 方法要点：引入递归熵量化反思中的资源消耗风险，并基于此构建反事实问题以实施资源耗尽攻击。
- 实验或效果：RECUR攻击能显著增加输出长度（最高11倍）并降低吞吐量（90%），验证了推理过程本身的安全隐患。

## 摘要（原文）

> Large Reasoning Models (LRMs) employ reasoning to address complex tasks. Such explicit reasoning requires extended context lengths, resulting in substantially higher resource consumption. Prior work has shown that adversarially crafted inputs can trigger redundant reasoning processes, exposing LRMs to resource-exhaustion vulnerabilities. However, the reasoning process itself, especially its reflective component, has received limited attention, even though it can lead to over-reflection and consume excessive computing power. In this paper, we introduce Recursive Entropy to quantify the risk of resource consumption in reflection, thereby revealing the safety issues inherent in inference itself. Based on Recursive Entropy, we introduce RECUR, a resource exhaustion attack via Recursive Entropy guided Counterfactual Utilization and Reflection. It constructs counterfactual questions to verify the inherent flaws and risks of LRMs. Extensive experiments demonstrate that, under benign inference, recursive entropy exhibits a pronounced decreasing trend. RECUR disrupts this trend, increasing the output length by up to 11x and decreasing throughput by 90%. Our work provides a new perspective on robust reasoning.

