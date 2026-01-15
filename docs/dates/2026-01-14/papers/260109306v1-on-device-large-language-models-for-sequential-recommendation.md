---
layout: default
title: On-Device Large Language Models for Sequential Recommendation
---

# On-Device Large Language Models for Sequential Recommendation
**arXiv**：[2601.09306v1](https://arxiv.org/abs/2601.09306) · [PDF](https://arxiv.org/pdf/2601.09306.pdf)  
**作者**：Xin Xia, Hongzhi Yin, Shane Culpepper  

**一句话要点**：提出OD-LLM框架，通过任务自适应压缩实现设备端大语言模型在序列推荐中的高效部署。

**关键词**：设备端推荐, 大语言模型压缩, 序列推荐, 低秩分解, 任务自适应优化

## 3 点简述
- 核心问题：大语言模型在资源受限设备上部署时面临内存和计算开销大的挑战。
- 方法要点：集成低秩结构压缩和令牌化归一化技术，结合渐进对齐算法优化参数。
- 实验或效果：在序列推荐基准测试中，模型大小减半时保持与原模型同等效果。

## 摘要（原文）

> On-device recommendation is critical for a number of real-world applications, especially in scenarios that have agreements on execution latency, user privacy, and robust functionality when internet connectivity is unstable or even impossible. While large language models (LLMs) can now provide exceptional capabilities that model user behavior for sequential recommendation tasks, their substantial memory footprint and computational overhead make the deployment on resource-constrained devices a high risk proposition. In this paper, we propose OD-LLM, the first task-adaptive compression framework explicitly designed to provide efficient and accurate on-device deployment of LLMs for sequential recommendation tasks. OD-LLM uniquely integrates two complementary compression strategies: a low-rank structural compression algorithm which uses Singular Value Decomposition (SVD) to significantly reduce parameter redundancy in the model, and a novel tokenization normalization technique that better complements the low-rank decomposition process being used. Additionally, to minimize any potential performance degradation when using higher compression ratios, a novel progressive alignment algorithm is used to iteratively refine the parameters required layerwise in the target model. Empirical evaluations conducted on sequential recommendation benchmarks show that OD-LLM exhibits no loss in effectiveness when compared to the original recommendation model, when the deployed model size is halved. These promising results demonstrate the efficacy and scalability of OD-LLM, making this novel solution a practical alternative for real-time, on-device solutions wishing to replace expensive, remotely executed LLMs.

