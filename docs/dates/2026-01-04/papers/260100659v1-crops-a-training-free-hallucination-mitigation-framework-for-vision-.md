---
layout: default
title: CRoPS: A Training-Free Hallucination Mitigation Framework for Vision-Language Models
---

# CRoPS: A Training-Free Hallucination Mitigation Framework for Vision-Language Models
**arXiv**：[2601.00659v1](https://arxiv.org/abs/2601.00659) · [PDF](https://arxiv.org/pdf/2601.00659.pdf)  
**作者**：Neeraj Anand, Samyak Jha, Udbhav Bamba, Rahul Rahaman  

**一句话要点**：提出CRoPS框架以缓解视觉语言模型幻觉，无需训练，通过选择性移除文本令牌和广义对比解码提升可靠性。

**关键词**：视觉语言模型, 幻觉缓解, 免训练框架, 对比解码, 文本令牌移除, 可靠性提升

## 3 点简述
- 核心问题：大型视觉语言模型易生成幻觉内容，现有免训练方法假设窄且效果在生成后期下降。
- 方法要点：构建幻觉模型通过选择性移除关键文本令牌捕获幻觉效应，并集成多个模型以代表多样幻觉源。
- 实验或效果：在六个基准和三个模型家族上提升CHAIR分数20%，优于现有免训练方法。

## 摘要（原文）

> Despite the rapid success of Large Vision-Language Models (LVLMs), a persistent challenge is their tendency to generate hallucinated content, undermining reliability in real-world use. Existing training-free methods address hallucinations but face two limitations: (i) they rely on narrow assumptions about hallucination sources, and (ii) their effectiveness declines toward the end of generation, where hallucinations are most likely to occur. A common strategy is to build hallucinated models by completely or partially removing visual tokens and contrasting them with the original model. Yet, this alone proves insufficient, since visual information still propagates into generated text. Building on this insight, we propose a novel hallucinated model that captures hallucination effects by selectively removing key text tokens. We further introduce Generalized Contrastive Decoding, which integrates multiple hallucinated models to represent diverse hallucination sources. Together, these ideas form CRoPS, a training-free hallucination mitigation framework that improves CHAIR scores by 20% and achieves consistent gains across six benchmarks and three LVLM families, outperforming state-of-the-art training-free methods.

