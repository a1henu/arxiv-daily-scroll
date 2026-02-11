---
layout: default
title: ESTAR: Early-Stopping Token-Aware Reasoning For Efficient Inference
---

# ESTAR: Early-Stopping Token-Aware Reasoning For Efficient Inference
**arXiv**：[2602.10004v1](https://arxiv.org/abs/2602.10004) · [PDF](https://arxiv.org/pdf/2602.10004.pdf)  
**作者**：Junda Wang, Zhichao Yang, Dongxu Zhang, Sanjit Singh Batra, Robert E. Tillman  

**一句话要点**：提出ESTAR方法以解决大型推理模型在生成长链思维时的计算冗余问题

**关键词**：推理效率, 早期停止, 强化学习, 计算冗余, 大型推理模型

## 3 点简述
- 核心问题：大型推理模型生成长链思维时，在达到正确答案后仍产生冗余推理，浪费计算资源。
- 方法要点：结合轨迹分类器、监督微调生成自停止信号，以及基于停止信号的强化学习来提前终止推理。
- 实验效果：在四个推理数据集上，推理长度减少约3.7倍，准确率基本保持，展示跨域泛化能力。

## 摘要（原文）

> Large reasoning models (LRMs) achieve state-of-the-art performance by generating long chains-of-thought, but often waste computation on redundant reasoning after the correct answer has already been reached. We introduce Early-Stopping for Token-Aware Reasoning (ESTAR), which detects and reduces such reasoning redundancy to improve efficiency without sacrificing accuracy. Our method combines (i) a trajectory-based classifier that identifies when reasoning can be safely stopped, (ii) supervised fine-tuning to teach LRMs to propose self-generated <stop> signals, and (iii) <stop>-aware reinforcement learning that truncates rollouts at self-generated stop points with compute-aware rewards. Experiments on four reasoning datasets show that ESTAR reduces reasoning length by about 3.7x (from 4,799 to 1,290) while preserving accuracy (74.9% vs. 74.2%), with strong cross-domain generalization. These results highlight early stopping as a simple yet powerful mechanism for improving reasoning efficiency in LRMs.

