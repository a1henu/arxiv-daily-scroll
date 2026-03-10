---
layout: default
title: AutoTraces: Autoregressive Trajectory Forecasting via Multimodal Large Language Models
---

# AutoTraces: Autoregressive Trajectory Forecasting via Multimodal Large Language Models
**arXiv**：[2603.07989v1](https://arxiv.org/abs/2603.07989) · [PDF](https://arxiv.org/pdf/2603.07989.pdf)  
**作者**：Teng Wang, Yanting Lu, Ruize Wang  

**一句话要点**：提出AutoTraces，通过多模态大语言模型实现机器人轨迹预测，以建模复杂人类行为。

**关键词**：轨迹预测, 多模态大语言模型, 自回归生成, 链式思维, 轻量编码器-解码器, 跨场景泛化

## 3 点简述
- 核心问题：在人群环境中预测机器人轨迹，需建模复杂人类行为。
- 方法要点：创新轨迹标记化方案，结合轻量编码器-解码器，扩展LLM到物理坐标空间。
- 实验或效果：实现SOTA预测精度，尤其在长时预测，支持跨场景泛化和灵活长度预测。

## 摘要（原文）

> We present AutoTraces, an autoregressive vision-language-trajectory model for robot trajectory forecasting in humam-populated environments, which harnesses the inherent reasoning capabilities of large language models (LLMs) to model complex human behaviors. In contrast to prior works that rely solely on textual representations, our key innovation lies in a novel trajectory tokenization scheme, which represents waypoints with point tokens as categorical and positional markers while encoding waypoint numerical values as corresponding point embeddings, seamlessly integrated into the LLM's space through a lightweight encoder-decoder architecture. This design preserves the LLM's native autoregressive generation mechanism while extending it to physical coordinate spaces, facilitates modeling of long-term interactions in trajectory data. We further introduce an automated chain-of-thought (CoT) generation mechanism that leverages a multimodal LLM to infer spatio-temporal relationships from visual observations and trajectory data, eliminating reliance on manual annotation. Through a two-stage training strategy, our AutoTraces achieves SOTA forecasting accuracy, particularly in long-horizon prediction, while exhibiting strong cross-scene generalization and supporting flexible-length forecasting.

