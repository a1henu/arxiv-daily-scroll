---
layout: default
title: HyperCLOVA X 8B Omni
---

# HyperCLOVA X 8B Omni
**arXiv**：[2601.01792v1](https://arxiv.org/abs/2601.01792) · [PDF](https://arxiv.org/pdf/2601.01792.pdf)  
**作者**：NAVER Cloud HyperCLOVA X Team  

**一句话要点**：提出HyperCLOVA X 8B Omni，作为首个支持文本、音频和视觉任意输入输出的全模态模型，以统一接口实现多模态理解与生成。

**关键词**：全模态模型, 任意输入输出, 多模态统一接口, 视觉音频编码, 韩语英语评估, 开放权重发布

## 3 点简述
- 核心问题：传统多模态模型常依赖独立模态管道，难以实现任意模态间的无缝交互与生成。
- 方法要点：通过共享下一个令牌预测接口统一模态，结合视觉和音频编码器注入连续嵌入以增强细粒度理解。
- 实验或效果：在韩语和英语的文本、音频、视觉组合任务中，与同类规模模型相比表现出竞争性性能。

## 摘要（原文）

> In this report, we present HyperCLOVA X 8B Omni, the first any-to-any omnimodal model in the HyperCLOVA X family that supports text, audio, and vision as both inputs and outputs. By consolidating multimodal understanding and generation into a single model rather than separate modality-specific pipelines, HyperCLOVA X 8B Omni serves as an 8B-scale omni-pathfinding point toward practical any-to-any omni assistants. At a high level, the model unifies modalities through a shared next-token prediction interface over an interleaved multimodal sequence, while vision and audio encoders inject continuous embeddings for fine-grained understanding and grounding. Empirical evaluations demonstrate competitive performance against comparably sized models across diverse input-output combinations spanning text, audio, and vision, in both Korean and English. We anticipate that the open-weight release of HyperCLOVA X 8B Omni will support a wide range of research and deployment scenarios.

