---
layout: default
title: Yes FLoReNce, I Will Do Better Next Time! Agentic Feedback Reasoning for Humorous Meme Detection
---

# Yes FLoReNce, I Will Do Better Next Time! Agentic Feedback Reasoning for Humorous Meme Detection
**arXiv**：[2601.07232v1](https://arxiv.org/abs/2601.07232) · [PDF](https://arxiv.org/pdf/2601.07232.pdf)  
**作者**：Olivia Shanhong Liu, Pai Chet Ng, De Wen Soh, Konstantinos N. Plataniotis  

**一句话要点**：提出FLoReNce框架，通过反馈推理提升幽默梗图检测性能

**关键词**：幽默梗图检测, 反馈推理, 多模态学习, 自适应提示, 非参数知识库

## 3 点简述
- 幽默梗图检测需理解意图而非表面关联，现有模型缺乏自我批判能力
- FLoReNce采用闭环学习与开环推理，通过反馈调节提示实现自适应推理
- 在PrideMM数据集上，FLoReNce提升了预测性能和解释质量

## 摘要（原文）

> Humorous memes blend visual and textual cues to convey irony, satire, or social commentary, posing unique challenges for AI systems that must interpret intent rather than surface correlations. Existing multimodal or prompting-based models generate explanations for humor but operate in an open loop,lacking the ability to critique or refine their reasoning once a prediction is made. We propose FLoReNce, an agentic feedback reasoning framework that treats meme understanding as a closed-loop process during learning and an open-loop process during inference. In the closed loop, a reasoning agent is critiqued by a judge; the error and semantic feedback are converted into control signals and stored in a feedback-informed, non-parametric knowledge base. At inference, the model retrieves similar judged experiences from this KB and uses them to modulate its prompt, enabling better, self-aligned reasoning without finetuning. On the PrideMM dataset, FLoReNce improves both predictive performance and explanation quality over static multimodal baselines, showing that feedback-regulated prompting is a viable path to adaptive meme humor understanding.

