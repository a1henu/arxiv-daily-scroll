---
layout: default
title: A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning
---

# A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning
**arXiv**：[2512.14442v1](https://arxiv.org/abs/2512.14442) · [PDF](https://arxiv.org/pdf/2512.14442.pdf)  
**作者**：Zixin Zhang, Kanghao Chen, Hanqing Wang, Hongfei Zhang, Harold Haodong Chen, Chenfei Liao, Litao Guo, Ying-Cong Chen  

**一句话要点**：提出A4-Agent框架，通过解耦推理实现零样本可及性预测，提升泛化能力。

**关键词**：可及性预测, 零样本学习, 代理框架, 基础模型协调, 视觉语言模型, 泛化能力

## 3 点简述
- 核心问题：现有端到端模型耦合推理与定位，依赖标注数据，泛化能力差。
- 方法要点：训练免费代理框架，分三阶段协调基础模型，无需微调。
- 实验或效果：零样本方法在多个基准上超越监督方法，泛化至真实场景。

## 摘要（原文）

> Affordance prediction, which identifies interaction regions on objects based on language instructions, is critical for embodied AI. Prevailing end-to-end models couple high-level reasoning and low-level grounding into a single monolithic pipeline and rely on training over annotated datasets, which leads to poor generalization on novel objects and unseen environments. In this paper, we move beyond this paradigm by proposing A4-Agent, a training-free agentic framework that decouples affordance prediction into a three-stage pipeline. Our framework coordinates specialized foundation models at test time: (1) a $\textbf{Dreamer}$ that employs generative models to visualize $\textit{how}$ an interaction would look; (2) a $\textbf{Thinker}$ that utilizes large vision-language models to decide $\textit{what}$ object part to interact with; and (3) a $\textbf{Spotter}$ that orchestrates vision foundation models to precisely locate $\textit{where}$ the interaction area is. By leveraging the complementary strengths of pre-trained models without any task-specific fine-tuning, our zero-shot framework significantly outperforms state-of-the-art supervised methods across multiple benchmarks and demonstrates robust generalization to real-world settings.

