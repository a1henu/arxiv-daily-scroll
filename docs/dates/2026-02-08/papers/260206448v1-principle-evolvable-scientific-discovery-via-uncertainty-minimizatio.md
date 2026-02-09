---
layout: default
title: Principle-Evolvable Scientific Discovery via Uncertainty Minimization
---

# Principle-Evolvable Scientific Discovery via Uncertainty Minimization
**arXiv**：[2602.06448v1](https://arxiv.org/abs/2602.06448) · [PDF](https://arxiv.org/pdf/2602.06448.pdf)  
**作者**：Yingming Pu, Tao Lin, Hongyu Chen  

**一句话要点**：提出PiEvo框架，通过不确定性最小化实现原理可演化的科学发现，以解决基于LLM的智能体因固定先验导致的低效问题。

**关键词**：科学发现, 贝叶斯优化, 不确定性最小化, 原理演化, LLM智能体, 信息导向选择

## 3 点简述
- 核心问题：基于LLM的科学智能体因依赖固定初始先验和静态假设空间，导致效率低下和计算浪费。
- 方法要点：将科学发现视为贝叶斯优化，在扩展的原理空间中集成信息导向假设选择和异常驱动增强机制。
- 实验或效果：在四个基准测试中，PiEvo平均解决方案质量达90.81%~93.15%，收敛步骤加速83.3%，并在不同领域和LLM骨干上保持稳健性能。

## 摘要（原文）

> Large Language Model (LLM)-based scientific agents have accelerated scientific discovery, yet they often suffer from significant inefficiencies due to adherence to fixed initial priors. Existing approaches predominantly operate within a static hypothesis space, which restricts the discovery of novel phenomena, resulting in computational waste when baseline theories fail. To address this, we propose shifting the focus from searching hypotheses to evolving the underlying scientific principles. We present PiEvo, a principle-evolvable framework that treats scientific discovery as Bayesian optimization over an expanding principle space. By integrating Information-Directed Hypothesis Selection via Gaussian Process and an anomaly-driven augmentation mechanism, PiEvo enables agents to autonomously refine their theoretical worldview. Evaluation across four benchmarks demonstrates that PiEvo (1) achieves an average solution quality of up to 90.81%~93.15%, representing a 29.7%~31.1% improvement over the state-of-the-art, (2) attains an 83.3% speedup in convergence step via significantly reduced sample complexity by optimizing the compact principle space, and (3) maintains robust performance across diverse scientific domains and LLM backbones.

