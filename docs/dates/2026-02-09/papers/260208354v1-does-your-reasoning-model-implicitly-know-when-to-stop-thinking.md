---
layout: default
title: Does Your Reasoning Model Implicitly Know When to Stop Thinking?
---

# Does Your Reasoning Model Implicitly Know When to Stop Thinking?
**arXiv**：[2602.08354v1](https://arxiv.org/abs/2602.08354) · [PDF](https://arxiv.org/pdf/2602.08354.pdf)  
**作者**：Zixuan Huang, Xin Xia, Yuxi Ren, Jianbin Zheng, Xuanda Wang, Zhixia Zhang, Hongyan Xie, Songshi Liang, Zehao Chen, Xuefeng Xiao, Fuzhen Zhuang, Jianxin Li, Yikun Ban, Deqing Wang  

**一句话要点**：提出SAGE采样范式以解决大推理模型冗余思考问题，提升推理效率与准确性

**关键词**：大推理模型, 思维链优化, 采样范式, 强化学习, 数学推理, 计算效率

## 3 点简述
- 核心问题：长思维链导致冗余，损害计算效率和实时应用准确性
- 方法要点：引入SAGE采样，释放模型隐含的停止思考能力，结合强化学习优化推理
- 实验或效果：在多个数学基准上显著提升推理准确性和效率

## 摘要（原文）

> Recent advancements in large reasoning models (LRMs) have greatly improved their capabilities on complex reasoning tasks through Long Chains of Thought (CoTs). However, this approach often results in substantial redundancy, impairing computational efficiency and causing significant delays in real-time applications. Recent studies show that longer reasoning chains are frequently uncorrelated with correctness and can even be detrimental to accuracy. In a further in-depth analysis of this phenomenon, we surprisingly uncover and empirically verify that LRMs implicitly know the appropriate time to stop thinking, while this capability is obscured by current sampling paradigms. Motivated by this, we introduce SAGE (Self-Aware Guided Efficient Reasoning), a novel sampling paradigm that unleashes this efficient reasoning potential. Furthermore, integrating SAGE as mixed sampling into group-based reinforcement learning (SAGE-RL) enables SAGE-RL to effectively incorporate SAGE-discovered efficient reasoning patterns into standard pass@1 inference, markedly enhancing both the reasoning accuracy and efficiency of LRMs across multiple challenging mathematical benchmarks.

