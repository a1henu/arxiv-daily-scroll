---
layout: default
title: 2K-Characters-10K-Stories: A Quality-Gated Stylized Narrative Dataset with Disentangled Control and Sequence Consistency
---

# 2K-Characters-10K-Stories: A Quality-Gated Stylized Narrative Dataset with Disentangled Control and Sequence Consistency
**arXiv**：[2512.05557v1](https://arxiv.org/abs/2512.05557) · [PDF](https://arxiv.org/pdf/2512.05557.pdf)  
**作者**：Xingxi Yin, Yicheng Li, Gong Yan, Chenglin Li, Jian Zhao, Cong Huang, Yue Deng, Yin Zhang  

**一句话要点**：提出2K-Characters-10K-Stories数据集以解决可控视觉叙事中身份一致性与属性解耦的挑战

**关键词**：可控视觉叙事, 身份一致性, 属性解耦, 风格化数据集, 人类在环管道, 质量门控循环

## 3 点简述
- 核心问题：现有数据集在可控视觉叙事中缺乏身份一致性与属性解耦，限制结构化控制。
- 方法要点：通过人类在环管道和属性解耦控制，生成大规模风格化角色与故事数据。
- 实验或效果：微调模型在生成视觉叙事上性能接近闭源模型，验证数据集有效性。

## 摘要（原文）

> Sequential identity consistency under precise transient attribute control remains a long-standing challenge in controllable visual storytelling. Existing datasets lack sufficient fidelity and fail to disentangle stable identities from transient attributes, limiting structured control over pose, expression, and scene composition and thus constraining reliable sequential synthesis. To address this gap, we introduce \textbf{2K-Characters-10K-Stories}, a multi-modal stylized narrative dataset of \textbf{2{,}000} uniquely stylized characters appearing across \textbf{10{,}000} illustration stories. It is the first dataset that pairs large-scale unique identities with explicit, decoupled control signals for sequential identity consistency. We introduce a \textbf{Human-in-the-Loop pipeline (HiL)} that leverages expert-verified character templates and LLM-guided narrative planning to generate highly-aligned structured data. A \textbf{decoupled control} scheme separates persistent identity from transient attributes -- pose and expression -- while a \textbf{Quality-Gated loop} integrating MMLM evaluation, Auto-Prompt Tuning, and Local Image Editing enforces pixel-level consistency. Extensive experiments demonstrate that models fine-tuned on our dataset achieves performance comparable to closed-source models in generating visual narratives.

