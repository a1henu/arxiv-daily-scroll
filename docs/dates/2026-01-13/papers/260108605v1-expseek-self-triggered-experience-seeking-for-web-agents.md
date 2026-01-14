---
layout: default
title: ExpSeek: Self-Triggered Experience Seeking for Web Agents
---

# ExpSeek: Self-Triggered Experience Seeking for Web Agents
**arXiv**：[2601.08605v1](https://arxiv.org/abs/2601.08605) · [PDF](https://arxiv.org/pdf/2601.08605.pdf)  
**作者**：Wenyuan Zhang, Xinghua Zhang, Haiyang Yu, Shuaiyi Nie, Bingli Wu, Juwei Yue, Tingwen Liu, Yongbin Li  

**一句话要点**：提出ExpSeek方法，通过步级主动经验寻求增强网络代理的动态适应能力。

**关键词**：网络代理, 经验干预, 步级主动寻求, 熵阈值, 动态适应, 性能提升

## 3 点简述
- 核心问题：现有方法在任务执行前被动注入经验，难以适应代理-环境交互中的动态上下文变化。
- 方法要点：基于模型内在信号估计步级熵阈值以确定干预时机，并设计步级定制化经验内容。
- 实验或效果：在Qwen3-8B和32B模型上，于四个基准测试中分别实现9.3%和7.5%的绝对性能提升。

## 摘要（原文）

> Experience intervention in web agents emerges as a promising technical paradigm, enhancing agent interaction capabilities by providing valuable insights from accumulated experiences. However, existing methods predominantly inject experience passively as global context before task execution, struggling to adapt to dynamically changing contextual observations during agent-environment interaction. We propose ExpSeek, which shifts experience toward step-level proactive seeking: (1) estimating step-level entropy thresholds to determine intervention timing using the model's intrinsic signals; (2) designing step-level tailor-designed experience content. Experiments on Qwen3-8B and 32B models across four challenging web agent benchmarks demonstrate that ExpSeek achieves absolute improvements of 9.3% and 7.5%, respectively. Our experiments validate the feasibility and advantages of entropy as a self-triggering signal, reveal that even a 4B small-scale experience model can significantly boost the performance of larger agent models.

