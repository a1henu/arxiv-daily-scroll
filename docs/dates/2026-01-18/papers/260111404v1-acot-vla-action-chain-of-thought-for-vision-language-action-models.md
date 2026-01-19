---
layout: default
title: ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models
---

# ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models
**arXiv**：[2601.11404v1](https://arxiv.org/abs/2601.11404) · [PDF](https://arxiv.org/pdf/2601.11404.pdf)  
**作者**：Linqing Zhong, Yi Liu, Yifei Wei, Ziyu Xiong, Maoqing Yao, Si Liu, Guanghui Ren  

**一句话要点**：提出ACoT-VLA架构，通过动作链式思维范式提升视觉-语言-动作模型的精确动作执行能力。

**关键词**：视觉-语言-动作模型, 动作链式思维, 机器人策略, 显式推理, 隐式推理, 动作执行

## 3 点简述
- 核心问题：现有VLA模型中间推理间接，难以传达精确动作执行所需的细粒度信息。
- 方法要点：引入显式动作推理器和隐式动作推理器，形成动作链式思维以指导最终策略。
- 实验或效果：在LIBERO、LIBERO-Plus和VLABench上分别达到98.5%、84.1%和47.4%的性能。

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as essential generalist robot policies for diverse manipulation tasks, conventionally relying on directly translating multimodal inputs into actions via Vision-Language Model (VLM) embeddings. Recent advancements have introduced explicit intermediary reasoning, such as sub-task prediction (language) or goal image synthesis (vision), to guide action generation. However, these intermediate reasoning are often indirect and inherently limited in their capacity to convey the full, granular information required for precise action execution. Instead, we posit that the most effective form of reasoning is one that deliberates directly in the action space. We introduce Action Chain-of-Thought (ACoT), a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy. In this paper, we propose ACoT-VLA, a novel architecture that materializes the ACoT paradigm. Specifically, we introduce two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning. Extensive experiments in real-world and simulation environments demonstrate the superiority of our proposed method, which achieves 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively.

