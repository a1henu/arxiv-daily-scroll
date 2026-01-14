---
layout: default
title: Reasoning Matters for 3D Visual Grounding
---

# Reasoning Matters for 3D Visual Grounding
**arXiv**：[2601.08811v1](https://arxiv.org/abs/2601.08811) · [PDF](https://arxiv.org/pdf/2601.08811.pdf)  
**作者**：Hsiang-Wei Huang, Kuang-Ming Chen, Wenhao Chai, Cheng-Yen Yang, Jen-Hao Cheng, Jenq-Neng Hwang  

**一句话要点**：提出自动合成3D视觉定位数据管道及Reason3DVG-8B模型，以增强推理能力解决3D视觉定位挑战。

**关键词**：3D视觉定位, 大语言模型, 数据合成, 推理增强, 微调训练, 跨模态融合

## 3 点简述
- 核心问题：现有3D视觉定位模型推理能力有限，依赖大量标注数据，性能提升与数据成本不成比例。
- 方法要点：开发自动合成3D视觉定位数据管道，生成带推理过程的数据，并用于LLM微调。
- 实验或效果：Reason3DVG-8B仅用1.6%训练数据即超越3D-GRAND，验证数据有效性和推理重要性。

## 摘要（原文）

> The recent development of Large Language Models (LLMs) with strong reasoning ability has driven research in various domains such as mathematics, coding, and scientific discovery. Meanwhile, 3D visual grounding, as a fundamental task in 3D understanding, still remains challenging due to the limited reasoning ability of recent 3D visual grounding models. Most of the current methods incorporate a text encoder and visual feature encoder to generate cross-modal fuse features and predict the referring object. These models often require supervised training on extensive 3D annotation data. On the other hand, recent research also focus on scaling synthetic data to train stronger 3D visual grounding LLM, however, the performance gain remains limited and non-proportional to the data collection cost. In this work, we propose a 3D visual grounding data pipeline, which is capable of automatically synthesizing 3D visual grounding data along with corresponding reasoning process. Additionally, we leverage the generated data for LLM fine-tuning and introduce Reason3DVG-8B, a strong 3D visual grounding LLM that outperforms previous LLM-based method 3D-GRAND using only 1.6% of their training data, demonstrating the effectiveness of our data and the importance of reasoning in 3D visual grounding.

