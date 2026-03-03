---
layout: default
title: Probing Materials Knowledge in LLMs: From Latent Embeddings to Reliable Predictions
---

# Probing Materials Knowledge in LLMs: From Latent Embeddings to Reliable Predictions
**arXiv**：[2603.01834v1](https://arxiv.org/abs/2603.01834) · [PDF](https://arxiv.org/pdf/2603.01834.pdf)  
**作者**：Vineeth Venugopal, Soroush Mahjoubi, Elsa Olivetti  

**一句话要点**：探究LLMs在材料科学中的知识编码与可靠性，揭示输出模态对模型行为的影响及LLM头部瓶颈

**关键词**：材料科学, 大语言模型, 知识编码, 模型可靠性, 嵌入提取, 性能变化

## 3 点简述
- 评估25个LLMs在材料科学任务中的表现，发现输出模态（符号与数值）决定模型行为差异
- 对于数值任务，微调提升准确性但模型仍不一致，直接提取中间层嵌入可绕过LLM头部瓶颈
- 纵向研究显示GPT模型性能随时间变化9-43%，对科学应用的可重复性构成挑战

## 摘要（原文）

> Large language models are increasingly applied to materials science, yet fundamental questions remain about their reliability and knowledge encoding. Evaluating 25 LLMs across four materials science tasks -- over 200 base and fine-tuned configurations -- we find that output modality fundamentally determines model behavior. For symbolic tasks, fine-tuning converges to consistent, verifiable answers with reduced response entropy, while for numerical tasks, fine-tuning improves prediction accuracy but models remain inconsistent across repeated inference runs, limiting their reliability as quantitative predictors. For numerical regression, we find that better performance can be obtained by extracting embeddings directly from intermediate transformer layers than from model text output, revealing an ``LLM head bottleneck,'' though this effect is property- and dataset-dependent. Finally, we present a longitudinal study of GPT model performance in materials science, tracking four models over 18 months and observing 9--43\% performance variation that poses reproducibility challenges for scientific applications.

