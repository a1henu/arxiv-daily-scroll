---
layout: default
title: SchröMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrödinger Bridge Problem
---

# SchröMind: Mitigating Hallucinations in Multimodal Large Language Models via Solving the Schrödinger Bridge Problem
**arXiv**：[2602.09528v1](https://arxiv.org/abs/2602.09528) · [PDF](https://arxiv.org/pdf/2602.09528.pdf)  
**作者**：Ziqiang Shi, Rujie Liu, Shanshan Yu, Satoshi Munakata, Koichi Shirahata  

**一句话要点**：提出SchröMind框架，通过求解薛定谔桥问题减少多模态大语言模型的幻觉问题

**关键词**：多模态大语言模型, 幻觉缓解, 薛定谔桥问题, 令牌级映射, 轻量级训练, 基准测试

## 3 点简述
- 核心问题：多模态大语言模型在医疗等高风险领域因幻觉问题受限，生成文本与视觉输入矛盾或忽略
- 方法要点：通过轻量级训练建立幻觉与真实激活间的令牌级映射，最小化传输成本，保持模型原有能力
- 实验或效果：在POPE和MME基准测试中实现最先进性能，计算开销极小

## 摘要（原文）

> Recent advancements in Multimodal Large Language Models (MLLMs) have achieved significant success across various domains. However, their use in high-stakes fields like healthcare remains limited due to persistent hallucinations, where generated text contradicts or ignores visual input. We contend that MLLMs can comprehend images but struggle to produce accurate token sequences. Minor perturbations can shift attention from truthful to untruthful states, and the autoregressive nature of text generation often prevents error correction. To address this, we propose SchröMind-a novel framework reducing hallucinations via solving the Schrödinger bridge problem. It establishes a token-level mapping between hallucinatory and truthful activations with minimal transport cost through lightweight training, while preserving the model's original capabilities. Extensive experiments on the POPE and MME benchmarks demonstrate the superiority of Schrödinger, which achieves state-of-the-art performance while introducing only minimal computational overhead.

