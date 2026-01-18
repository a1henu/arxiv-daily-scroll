---
layout: default
title: Toward Ultra-Long-Horizon Agentic Science: Cognitive Accumulation for Machine Learning Engineering
---

# Toward Ultra-Long-Horizon Agentic Science: Cognitive Accumulation for Machine Learning Engineering
**arXiv**：[2601.10402v1](https://arxiv.org/abs/2601.10402) · [PDF](https://arxiv.org/pdf/2601.10402.pdf)  
**作者**：Xinyu Zhu, Yuzhu Cai, Zexi Liu, Bingyang Zheng, Cheng Wang, Rui Ye, Jiaao Chen, Hanrui Wang, Wei-Chen Wang, Yuzhi Zhang, Linfeng Zhang, Weinan E, Di Jin, Siheng Chen  

**一句话要点**：提出分层认知缓存以解决超长时域自主性在机器学习工程中的瓶颈

**关键词**：超长时域自主性, 分层认知缓存, 机器学习工程, 认知积累, 自主代理

## 3 点简述
- 核心问题：LLMs在现实研究的高维延迟反馈环境中难以维持超长时域的战略一致性和迭代修正
- 方法要点：通过分层认知缓存动态提炼执行痕迹为稳定知识和跨任务智慧，解耦即时执行与长期策略
- 实验或效果：在OpenAI的MLE-Bench上以24小时预算实现56.44%的奖牌率，达到最先进水平

## 摘要（原文）

> The advancement of artificial intelligence toward agentic science is currently bottlenecked by the challenge of ultra-long-horizon autonomy, the ability to sustain strategic coherence and iterative correction over experimental cycles spanning days or weeks. While Large Language Models (LLMs) have demonstrated prowess in short-horizon reasoning, they are easily overwhelmed by execution details in the high-dimensional, delayed-feedback environments of real-world research, failing to consolidate sparse feedback into coherent long-term guidance. Here, we present ML-Master 2.0, an autonomous agent that masters ultra-long-horizon machine learning engineering (MLE) which is a representative microcosm of scientific discovery. By reframing context management as a process of cognitive accumulation, our approach introduces Hierarchical Cognitive Caching (HCC), a multi-tiered architecture inspired by computer systems that enables the structural differentiation of experience over time. By dynamically distilling transient execution traces into stable knowledge and cross-task wisdom, HCC allows agents to decouple immediate execution from long-term experimental strategy, effectively overcoming the scaling limits of static context windows. In evaluations on OpenAI's MLE-Bench under 24-hour budgets, ML-Master 2.0 achieves a state-of-the-art medal rate of 56.44%. Our findings demonstrate that ultra-long-horizon autonomy provides a scalable blueprint for AI capable of autonomous exploration beyond human-precedent complexities.

