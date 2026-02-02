---
layout: default
title: Alignment among Language, Vision and Action Representations
---

# Alignment among Language, Vision and Action Representations
**arXiv**：[2601.22948v1](https://arxiv.org/abs/2601.22948) · [PDF](https://arxiv.org/pdf/2601.22948.pdf)  
**作者**：Nicola Milano, Stefano Nolfi  

**一句话要点**：探究语言、视觉与动作表征在具身AI中的跨模态对齐，揭示共享语义结构

**关键词**：跨模态对齐, 具身AI, 表征学习, 行为克隆, 语义结构, Transformer智能体

## 3 点简述
- 核心问题：不同学习模态（语言、视觉、动作）是否产生共享内部表征，挑战传统专门化假设。
- 方法要点：在BabyAI平台训练基于Transformer的智能体，通过行为克隆生成动作基础的语言嵌入，并与LLM和VLM表征比较。
- 实验或效果：观察到动作表征与解码器语言模型和BLIP强对齐，支持模态无关语义组织，促进跨域迁移。

## 摘要（原文）

> A fundamental question in cognitive science and AI concerns whether different learning modalities: language, vision, and action, give rise to distinct or shared internal representations. Traditional views assume that models trained on different data types develop specialized, non-transferable representations. However, recent evidence suggests unexpected convergence: models optimized for distinct tasks may develop similar representational geometries. We investigate whether this convergence extends to embodied action learning by training a transformer-based agent to execute goal-directed behaviors in response to natural language instructions. Using behavioral cloning on the BabyAI platform, we generated action-grounded language embeddings shaped exclusively by sensorimotor control requirements. We then compared these representations with those extracted from state-of-the-art large language models (LLaMA, Qwen, DeepSeek, BERT) and vision-language models (CLIP, BLIP). Despite substantial differences in training data, modality, and objectives, we observed robust cross-modal alignment. Action representations aligned strongly with decoder-only language models and BLIP (precision@15: 0.70-0.73), approaching the alignment observed among language models themselves. Alignment with CLIP and BERT was significantly weaker. These findings indicate that linguistic, visual, and action representations converge toward partially shared semantic structures, supporting modality-independent semantic organization and highlighting potential for cross-domain transfer in embodied AI systems.

