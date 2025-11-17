---
layout: default
title: ImAgent: A Unified Multimodal Agent Framework for Test-Time Scalable Image Generation
---

# ImAgent: A Unified Multimodal Agent Framework for Test-Time Scalable Image Generation
**arXiv**：[2511.11483v1](https://arxiv.org/abs/2511.11483) · [PDF](https://arxiv.org/pdf/2511.11483.pdf)  
**作者**：Kaishen Wang, Ruibo Chen, Tong Zheng, Heng Huang  

**一句话要点**：提出ImAgent统一多模态代理框架，以解决测试时扩展中图像生成的随机性和不一致性问题。

**关键词**：文本到图像生成, 多模态代理, 测试时扩展, 图像编辑, 自评估框架

## 3 点简述
- 核心问题：文本到图像模型在提示模糊时生成随机且不一致的图像，现有方法效率低。
- 方法要点：集成推理、生成和自评估于单一框架，通过策略控制器动态交互提升效率。
- 实验或效果：在图像生成和编辑任务中，ImAgent超越骨干模型和其他基线，提高保真度和语义对齐。

## 摘要（原文）

> Recent text-to-image (T2I) models have made remarkable progress in generating visually realistic and semantically coherent images. However, they still suffer from randomness and inconsistency with the given prompts, particularly when textual descriptions are vague or underspecified. Existing approaches, such as prompt rewriting, best-of-N sampling, and self-refinement, can mitigate these issues but usually require additional modules and operate independently, hindering test-time scaling efficiency and increasing computational overhead. In this paper, we introduce ImAgent, a training-free unified multimodal agent that integrates reasoning, generation, and self-evaluation within a single framework for efficient test-time scaling. Guided by a policy controller, multiple generation actions dynamically interact and self-organize to enhance image fidelity and semantic alignment without relying on external models. Extensive experiments on image generation and editing tasks demonstrate that ImAgent consistently improves over the backbone and even surpasses other strong baselines where the backbone model fails, highlighting the potential of unified multimodal agents for adaptive and efficient image generation under test-time scaling.

