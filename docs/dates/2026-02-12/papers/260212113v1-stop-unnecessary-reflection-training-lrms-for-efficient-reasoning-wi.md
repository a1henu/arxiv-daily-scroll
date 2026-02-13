---
layout: default
title: Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty
---

# Stop Unnecessary Reflection: Training LRMs for Efficient Reasoning with Adaptive Reflection and Length Coordinated Penalty
**arXiv**：[2602.12113v1](https://arxiv.org/abs/2602.12113) · [PDF](https://arxiv.org/pdf/2602.12113.pdf)  
**作者**：Zewei Yu, Lirong Gao, Yuke Zhu, Bo Zheng, Sheng Guo, Haobo Wang, Junbo Zhao  

**一句话要点**：提出ARLCP框架以解决大型推理模型在复杂任务中过度反思导致的效率低下问题

**关键词**：大型推理模型, 自适应反思, 长度惩罚, 强化学习框架, 数学推理基准, 效率-准确性权衡

## 3 点简述
- 核心问题：大型推理模型在复杂任务中生成过长思维链，包含不必要的反思步骤，增加计算开销且不提升准确率。
- 方法要点：引入自适应反思惩罚和长度协调惩罚，通过强化学习动态平衡推理效率与解决方案准确性。
- 实验或效果：在数学推理基准测试中，ARLCP显著减少响应长度并提高准确率，例如1.5B模型长度减少53.1%且准确率提升5.8%。

## 摘要（原文）

> Large Reasoning Models (LRMs) have demonstrated remarkable performance on complex reasoning tasks by employing test-time scaling. However, they often generate over-long chains-of-thought that, driven by substantial reflections such as repetitive self-questioning and circular reasoning, lead to high token consumption, substantial computational overhead, and increased latency without improving accuracy, particularly in smaller models. Our observation reveals that increasing problem complexity induces more excessive and unnecessary reflection, which in turn reduces accuracy and increases token overhead. To address this challenge, we propose Adaptive Reflection and Length Coordinated Penalty (ARLCP), a novel reinforcement learning framework designed to dynamically balance reasoning efficiency and solution accuracy. ARLCP introduces two key innovations: (1) a reflection penalty that adaptively curtails unnecessary reflective steps while preserving essential reasoning, and (2) a length penalty calibrated to the estimated complexity of the problem. By coordinating these penalties, ARLCP encourages the model to generate more concise and effective reasoning paths. We evaluate our method on five mathematical reasoning benchmarks using DeepSeek-R1-Distill-Qwen-1.5B and DeepSeek-R1-Distill-Qwen-7B models. Experimental results show that ARLCP achieves a superior efficiency-accuracy trade-off compared to existing approaches. For the 1.5B model, it reduces the average response length by 53.1% while simultaneously improving accuracy by 5.8%. For the 7B model, it achieves a 35.0% reduction in length with a 2.7% accuracy gain. The code is released at https://github.com/ZeweiYu1/ARLCP .

