---
layout: default
title: ChainV: Atomic Visual Hints Make Multimodal Reasoning Shorter and Better
---

# ChainV: Atomic Visual Hints Make Multimodal Reasoning Shorter and Better
**arXiv**：[2511.17106v1](https://arxiv.org/abs/2511.17106) · [PDF](https://arxiv.org/pdf/2511.17106.pdf)  
**作者**：Yuan Zhang, Ming Lu, Junwen Pan, Tao Huang, Kuan Cheng, Qi She, Shanghang Zhang  

**一句话要点**：提出ChainV框架，通过动态视觉提示优化多模态推理的准确性与效率

**关键词**：多模态推理, 视觉提示选择, 推理效率优化, 注意力机制, 数学推理基准

## 3 点简述
- 核心问题：多模态推理模型存在冗余自反思，导致推理链过长且效率低下
- 方法要点：动态选择原子视觉提示，基于注意力强度与一致性评估优化推理过程
- 实验或效果：在MathVista等基准上提升准确率2.3%，降低延迟51.4%和输出长度24.5%

## 摘要（原文）

> Recent advances in multimodal reasoning models have demonstrated impressive capabilities across text and vision. However, even leading models exhibit redundant self-reflection when generating lengthy reasoning chains. While training-free CoT compression methods have emerged in the LLMs domain, they rely on static visual references and thus provide limited gains for multimodal reasoning. Therefore, we propose ChainV, a framework that dynamically integrates visual hints into the reasoning process, thereby making multimodal reasoning shorter and better. Specifically, ChainV first performs a coarse visual patch selection based on the previous reasoning step, then refines it by identifying the most representative atomic visual hint according to the averaged attention intensity. Additionally, ChainV introduces a consistency-based evaluation mechanism to assess the reliability of the chosen hint, guiding the model to adaptively adjust its level of self-reflection. Eventually, the pixel coordinates of the selected visual hint and its reliability are incorporated into thinking with a Bernoulli stochastic process. Experiments indicate that our method significantly improves reasoning accuracy and efficiency, especially on math-intensive benchmarks where visual hints are crucial for multi-step symbolic reasoning. For example, ChainV achieves $2.3\%$ improvement on the MathVista within MIMO-VL-RL, while reducing inference latency by $51.4\%$ and shortening output token length by $24.5\%$.

