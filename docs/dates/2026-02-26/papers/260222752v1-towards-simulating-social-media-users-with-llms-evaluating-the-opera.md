---
layout: default
title: Towards Simulating Social Media Users with LLMs: Evaluating the Operational Validity of Conditioned Comment Prediction
---

# Towards Simulating Social Media Users with LLMs: Evaluating the Operational Validity of Conditioned Comment Prediction
**arXiv**：[2602.22752v1](https://arxiv.org/abs/2602.22752) · [PDF](https://arxiv.org/pdf/2602.22752.pdf)  
**作者**：Nils Schwager, Simon Münker, Alistair Plum, Achim Rettinger  

**一句话要点**：提出条件评论预测框架，评估大语言模型在社交媒体用户行为模拟中的操作有效性。

**关键词**：条件评论预测, 大语言模型评估, 社交媒体模拟, 操作有效性, 监督微调, 低资源语言

## 3 点简述
- 核心问题：大语言模型作为社会科学中主动硅主体的操作有效性缺乏广泛验证。
- 方法要点：通过条件评论预测任务，比较生成输出与真实数字痕迹，评估模型能力。
- 实验或效果：在低资源设置下，监督微调导致形式与内容解耦，显式条件在微调后变得冗余。

## 摘要（原文）

> The transition of Large Language Models (LLMs) from exploratory tools to active "silicon subjects" in social science lacks extensive validation of operational validity. This study introduces Conditioned Comment Prediction (CCP), a task in which a model predicts how a user would comment on a given stimulus by comparing generated outputs with authentic digital traces. This framework enables a rigorous evaluation of current LLM capabilities with respect to the simulation of social media user behavior. We evaluated open-weight 8B models (Llama3.1, Qwen3, Ministral) in English, German, and Luxembourgish language scenarios. By systematically comparing prompting strategies (explicit vs. implicit) and the impact of Supervised Fine-Tuning (SFT), we identify a critical form vs. content decoupling in low-resource settings: while SFT aligns the surface structure of the text output (length and syntax), it degrades semantic grounding. Furthermore, we demonstrate that explicit conditioning (generated biographies) becomes redundant under fine-tuning, as models successfully perform latent inference directly from behavioral histories. Our findings challenge current "naive prompting" paradigms and offer operational guidelines prioritizing authentic behavioral traces over descriptive personas for high-fidelity simulation.

