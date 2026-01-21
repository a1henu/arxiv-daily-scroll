---
layout: default
title: TimeART: Towards Agentic Time Series Reasoning via Tool-Augmentation
---

# TimeART: Towards Agentic Time Series Reasoning via Tool-Augmentation
**arXiv**：[2601.13653v1](https://arxiv.org/abs/2601.13653) · [PDF](https://arxiv.org/pdf/2601.13653.pdf)  
**作者**：Xingjian Wu, Junkai Lu, Zhengyu Li, Xiangfei Qiu, Jilin Hu, Chenjuan Guo, Christian S. Jensen, Bin Yang  

**一句话要点**：提出TimeART框架，融合工具与LLM实现自动化时间序列问答，以降低人工成本。

**关键词**：时间序列问答, 工具增强, 大语言模型, 自动化推理, 专家轨迹训练

## 3 点简述
- 核心问题：时间序列分析依赖人工，自动化不足，成本高。
- 方法要点：结合现成工具与LLM，通过专家轨迹和四阶段训练提升推理能力。
- 实验或效果：8B模型在多个任务上达到SOTA，验证框架有效性。

## 摘要（原文）

> Time series data widely exist in real-world cyber-physical systems. Though analyzing and interpreting them contributes to significant values, e.g, disaster prediction and financial risk control, current workflows mainly rely on human data scientists, which requires significant labor costs and lacks automation. To tackle this, we introduce TimeART, a framework fusing the analytical capability of strong out-of-the-box tools and the reasoning capability of Large Language Models (LLMs), which serves as a fully agentic data scientist for Time Series Question Answering (TSQA). To teach the LLM-based Time Series Reasoning Models (TSRMs) strategic tool-use, we also collect a 100k expert trajectory corpus called TimeToolBench. To enhance TSRMs' generalization capability, we then devise a four-stage training strategy, which boosts TSRMs through learning from their own early experiences and self-reflections. Experimentally, we train an 8B TSRM on TimeToolBench and equip it with the TimeART framework, and it achieves consistent state-of-the-art performance on multiple TSQA tasks, which pioneers a novel approach towards agentic time series reasoning.

